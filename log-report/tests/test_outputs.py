import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "no report.json found"
    try:
        report = json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError(f"report.json is not valid JSON: {exc}") from exc
    assert isinstance(report, dict), "report.json must contain a JSON object"
    return report


def test_report_schema():
    """Success criterion 1: /app/report.json is a JSON object with exactly the required keys."""
    report = load_report()
    assert set(report) == {"total_requests", "unique_ips", "top_path"}
    assert isinstance(report["total_requests"], int)
    assert isinstance(report["unique_ips"], int)
    assert isinstance(report["top_path"], str)


def test_total_requests():
    """Success criterion 2: total_requests is the number of non-empty access log entries."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips is the count of distinct client IP addresses."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequently requested path."""
    assert load_report()["top_path"] == "/index.html"
