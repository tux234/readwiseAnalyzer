import subprocess
import re

def analyze_with_fabric(content, pattern):
    """
    Send content to Fabric for analysis using a specific pattern.

    Args:
        content (str): The text content to analyze.
        pattern (str): The pattern used by Fabric for analysis.

    Returns:
        str: The output from the Fabric analysis.

    Raises:
        Exception: If the Fabric command fails.
    """
    if not re.match(r'^[\w-]+$', pattern):
        raise ValueError(f"Invalid pattern: {pattern!r}")

    command = ["fabric", "--pattern", pattern]
    result = subprocess.run(
        command,
        input=content,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        raise Exception(f"Fabric analysis failed: {result.stderr}")