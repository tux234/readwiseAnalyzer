import pytest
import subprocess

from fabric_integration import analyze_with_fabric


@pytest.mark.parametrize("pattern", ["valid_pattern", "another-valid"])
def test_analyze_with_fabric_valid(monkeypatch, pattern):
    class DummyResult:
        def __init__(self, returncode, stdout, stderr):
            self.returncode = returncode
            self.stdout = stdout
            self.stderr = stderr

    def fake_run(cmd, input, capture_output, text):
        assert cmd == ["fabric", "--pattern", pattern]
        return DummyResult(0, "OK", "")

    monkeypatch.setattr(subprocess, 'run', fake_run)
    result = analyze_with_fabric("content", pattern)
    assert result == "OK"


@pytest.mark.parametrize("pattern", ["bad pattern", "invalid;rm -rf /"])
def test_analyze_with_fabric_bad_pattern(pattern):
    with pytest.raises(ValueError):
        analyze_with_fabric("content", pattern)


def test_analyze_with_fabric_subprocess_error(monkeypatch):
    class DummyResult:
        def __init__(self):
            self.returncode = 1
            self.stdout = ""
            self.stderr = "error"

    def fake_run(cmd, input, capture_output, text):
        return DummyResult()

    monkeypatch.setattr(subprocess, 'run', fake_run)
    with pytest.raises(Exception) as excinfo:
        analyze_with_fabric("content", "validpattern")
    assert 'Fabric analysis failed' in str(excinfo.value)