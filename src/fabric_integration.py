import subprocess

def analyze_with_fabric(content, pattern):
    """Send content to Fabric for analysis using a specific pattern."""
    # Construct the command without a file, using input redirection
    command = f"fabric --pattern {pattern}"

    # Use subprocess to send the content to Fabric's stdin
    result = subprocess.run(
        command,
        input=content,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        raise Exception(f"Fabric analysis failed: {result.stderr}")