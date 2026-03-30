"""
Custom test runner for Python Tutor exercises.
Outputs human-readable pass/fail results without requiring pytest.
Returns JSON for Claude to parse.

Usage:
    python3 test_runner.py <test_file> [<exercise_file>]

Output:
    JSON with results + human-readable summary to stderr
"""

import sys
import os
import json
import importlib.util
import traceback


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_tests(test_path, exercise_path=None):
    results = {"passed": 0, "failed": 0, "errors": 0, "tests": []}

    # Ensure exercise directory is importable
    test_dir = os.path.dirname(os.path.abspath(test_path))
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)

    # Load test module
    try:
        test_mod = load_module(test_path, "test_module")
    except Exception as e:
        results["errors"] = 1
        results["error_message"] = f"Could not load test file: {e}"
        return results

    # Find all test functions
    test_funcs = [
        name for name in dir(test_mod)
        if name.startswith("test_") and callable(getattr(test_mod, name))
    ]

    if not test_funcs:
        results["error_message"] = "No test functions found"
        return results

    for name in sorted(test_funcs):
        test_result = {"name": name, "status": "passed", "message": ""}
        try:
            getattr(test_mod, name)()
            results["passed"] += 1
        except AssertionError as e:
            test_result["status"] = "failed"
            test_result["message"] = str(e) if str(e) else "Assertion failed"
            results["failed"] += 1
        except Exception as e:
            test_result["status"] = "error"
            test_result["message"] = f"{type(e).__name__}: {e}"
            results["errors"] += 1

        results["tests"].append(test_result)

    results["total"] = len(test_funcs)
    return results


def format_human(results):
    lines = []
    total = results.get("total", 0)
    passed = results["passed"]

    lines.append(f"Results: {passed}/{total} passing")
    lines.append("")

    for t in results["tests"]:
        icon = "+" if t["status"] == "passed" else "-"
        line = f"  {icon} {t['name']}"
        if t["message"]:
            line += f" -- {t['message']}"
        lines.append(line)

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 test_runner.py <test_file>", file=sys.stderr)
        sys.exit(1)

    test_file = sys.argv[1]
    exercise_file = sys.argv[2] if len(sys.argv) > 2 else None

    results = run_tests(test_file, exercise_file)

    # Human-readable to stderr
    print(format_human(results), file=sys.stderr)

    # JSON to stdout for Claude
    print(json.dumps(results))
