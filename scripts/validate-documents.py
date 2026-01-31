#!/usr/bin/env python3
"""
ドキュメント検証スクリプト
PRD, SRS (IEEE 830), Test Spec (IEEE 829) のスキーマ検証を行う
"""

import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    print("Error: jsonschema package is required. Install with: pip install jsonschema")
    sys.exit(1)


class DocumentValidator:
    """ドキュメント検証クラス"""

    SCHEMA_DIR = Path(__file__).parent.parent / "schemas"

    SCHEMA_FILES = {
        "prd": "prd.schema.json",
        "srs": "srs-ieee830.schema.json",
        "test": "test-spec-ieee829.schema.json",
    }

    def __init__(self):
        self.schemas: dict[str, dict] = {}
        self._load_schemas()

    def _load_schemas(self) -> None:
        """スキーマファイルを読み込む"""
        for doc_type, filename in self.SCHEMA_FILES.items():
            schema_path = self.SCHEMA_DIR / filename
            if schema_path.exists():
                with open(schema_path, "r", encoding="utf-8") as f:
                    self.schemas[doc_type] = json.load(f)
            else:
                print(f"Warning: Schema file not found: {schema_path}")

    def validate(self, doc_type: str, document: dict[str, Any]) -> tuple[bool, list[str]]:
        """
        ドキュメントを検証する

        Args:
            doc_type: ドキュメントタイプ (prd, srs, test)
            document: 検証対象のドキュメント

        Returns:
            (is_valid, errors): 検証結果とエラーリスト
        """
        if doc_type not in self.schemas:
            return False, [f"Unknown document type: {doc_type}"]

        schema = self.schemas[doc_type]
        validator = Draft202012Validator(schema)
        errors = []

        for error in sorted(validator.iter_errors(document), key=lambda e: e.path):
            path = ".".join(str(p) for p in error.path) if error.path else "(root)"
            errors.append(f"[{path}] {error.message}")

        return len(errors) == 0, errors

    def validate_file(self, doc_type: str, file_path: Path) -> tuple[bool, list[str]]:
        """
        ファイルからドキュメントを読み込んで検証する

        Args:
            doc_type: ドキュメントタイプ
            file_path: ドキュメントファイルパス

        Returns:
            (is_valid, errors): 検証結果とエラーリスト
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                document = json.load(f)
            return self.validate(doc_type, document)
        except json.JSONDecodeError as e:
            return False, [f"Invalid JSON: {e}"]
        except FileNotFoundError:
            return False, [f"File not found: {file_path}"]

    def get_completeness_score(self, doc_type: str, document: dict[str, Any]) -> dict[str, Any]:
        """
        ドキュメントの完成度スコアを計算する

        Args:
            doc_type: ドキュメントタイプ
            document: 検証対象のドキュメント

        Returns:
            完成度レポート
        """
        if doc_type not in self.schemas:
            return {"error": f"Unknown document type: {doc_type}"}

        schema = self.schemas[doc_type]
        required_fields = schema.get("required", [])
        optional_fields = [
            k for k in schema.get("properties", {}).keys()
            if k not in required_fields
        ]

        # 必須フィールドのチェック
        required_present = sum(1 for f in required_fields if f in document)
        required_score = (required_present / len(required_fields) * 100) if required_fields else 100

        # オプションフィールドのチェック
        optional_present = sum(1 for f in optional_fields if f in document)
        optional_score = (optional_present / len(optional_fields) * 100) if optional_fields else 100

        # 全体スコア (必須: 70%, オプション: 30%)
        overall_score = required_score * 0.7 + optional_score * 0.3

        return {
            "required": {
                "total": len(required_fields),
                "present": required_present,
                "missing": [f for f in required_fields if f not in document],
                "score": round(required_score, 1),
            },
            "optional": {
                "total": len(optional_fields),
                "present": optional_present,
                "score": round(optional_score, 1),
            },
            "overall_score": round(overall_score, 1),
            "is_complete": required_score == 100,
        }


def validate_traceability(
    prd: dict[str, Any],
    srs: dict[str, Any],
    test_spec: dict[str, Any]
) -> tuple[bool, list[str]]:
    """
    PRD → SRS → Test Spec のトレーサビリティを検証する

    Args:
        prd: PRDドキュメント
        srs: SRSドキュメント
        test_spec: Test Specドキュメント

    Returns:
        (is_valid, warnings): 検証結果と警告リスト
    """
    warnings = []

    # PRD要件IDの収集
    prd_requirement_ids = set()
    for req in prd.get("requirements", {}).get("functional", []):
        prd_requirement_ids.add(req.get("id", ""))
    for req in prd.get("requirements", {}).get("non_functional", []):
        prd_requirement_ids.add(req.get("id", ""))

    # SRS要件IDの収集とPRD参照チェック
    srs_requirement_ids = set()
    srs_to_prd_refs = {}
    for req in srs.get("specific_requirements", {}).get("functional_requirements", []):
        req_id = req.get("id", "")
        srs_requirement_ids.add(req_id)
        source = req.get("source", "")
        if source:
            srs_to_prd_refs[req_id] = source
            if source not in prd_requirement_ids:
                warnings.append(f"SRS {req_id} references unknown PRD requirement: {source}")

    # Test Spec → SRS トレーサビリティチェック
    test_case_ids = set()
    for tc in test_spec.get("test_cases", []):
        tc_id = tc.get("id", "")
        test_case_ids.add(tc_id)
        srs_ref = tc.get("srs_reference", "")
        if srs_ref and srs_ref not in srs_requirement_ids:
            warnings.append(f"Test case {tc_id} references unknown SRS requirement: {srs_ref}")

    # トレーサビリティマトリクスのチェック
    for trace in test_spec.get("traceability_matrix", []):
        req_id = trace.get("requirement_id", "")
        if req_id not in srs_requirement_ids:
            warnings.append(f"Traceability matrix references unknown SRS requirement: {req_id}")

    # カバレッジチェック
    covered_srs = set()
    for trace in test_spec.get("traceability_matrix", []):
        covered_srs.add(trace.get("requirement_id", ""))

    uncovered = srs_requirement_ids - covered_srs
    if uncovered:
        warnings.append(f"SRS requirements without test coverage: {', '.join(uncovered)}")

    return len(warnings) == 0, warnings


def print_report(title: str, is_valid: bool, messages: list[str]) -> None:
    """検証レポートを出力する"""
    status = "✅ PASS" if is_valid else "❌ FAIL"
    print(f"\n{'='*60}")
    print(f"{title}: {status}")
    print("=" * 60)

    if messages:
        for msg in messages:
            prefix = "⚠️ " if is_valid else "❌ "
            print(f"  {prefix}{msg}")
    else:
        print("  No issues found.")


def main():
    """メイン関数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate PRD, SRS, and Test Spec documents against schemas"
    )
    parser.add_argument(
        "--prd",
        type=Path,
        help="Path to PRD JSON file"
    )
    parser.add_argument(
        "--srs",
        type=Path,
        help="Path to SRS JSON file"
    )
    parser.add_argument(
        "--test",
        type=Path,
        help="Path to Test Spec JSON file"
    )
    parser.add_argument(
        "--traceability",
        action="store_true",
        help="Check traceability between documents (requires all three documents)"
    )
    parser.add_argument(
        "--completeness",
        action="store_true",
        help="Show completeness scores"
    )
    parser.add_argument(
        "--json-output",
        action="store_true",
        help="Output results as JSON"
    )

    args = parser.parse_args()

    if not any([args.prd, args.srs, args.test]):
        parser.print_help()
        sys.exit(1)

    validator = DocumentValidator()
    results = {
        "validations": {},
        "traceability": None,
        "overall": True,
    }

    # 各ドキュメントの検証
    documents = {}
    for doc_type, file_path in [("prd", args.prd), ("srs", args.srs), ("test", args.test)]:
        if file_path:
            is_valid, errors = validator.validate_file(doc_type, file_path)
            results["validations"][doc_type] = {
                "file": str(file_path),
                "is_valid": is_valid,
                "errors": errors,
            }
            results["overall"] = results["overall"] and is_valid

            # 完成度スコア
            if args.completeness and is_valid:
                with open(file_path, "r", encoding="utf-8") as f:
                    doc = json.load(f)
                    documents[doc_type] = doc
                    results["validations"][doc_type]["completeness"] = \
                        validator.get_completeness_score(doc_type, doc)

            if not args.json_output:
                print_report(f"{doc_type.upper()} Validation", is_valid, errors)

    # トレーサビリティチェック
    if args.traceability:
        if len(documents) == 3:
            is_valid, warnings = validate_traceability(
                documents["prd"],
                documents["srs"],
                documents["test"]
            )
            results["traceability"] = {
                "is_valid": is_valid,
                "warnings": warnings,
            }
            results["overall"] = results["overall"] and is_valid

            if not args.json_output:
                print_report("Traceability Check", is_valid, warnings)
        else:
            if not args.json_output:
                print("\n⚠️  Traceability check requires all three documents (--prd, --srs, --test)")

    # 結果出力
    if args.json_output:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print("\n" + "=" * 60)
        overall_status = "✅ ALL CHECKS PASSED" if results["overall"] else "❌ SOME CHECKS FAILED"
        print(f"Overall Result: {overall_status}")
        print("=" * 60)

    sys.exit(0 if results["overall"] else 1)


if __name__ == "__main__":
    main()
