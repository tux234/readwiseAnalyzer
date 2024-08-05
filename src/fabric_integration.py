import subprocess
import os

def analyze_with_fabric(content, pattern):
    """Send content to Fabric for analysis using a specific pattern."""
    temp_filename = 'temp_content.txt'

    # Write content to a temporary file
    with open(temp_filename, 'w') as file:
        file.write(content)

    # Debug statement
    print(f"Content written to {temp_filename}:")
    with open(temp_filename, 'r') as file:
        print(file.read())

    # Call the Fabric application using the file
    command = f"fabric --pattern {pattern} --text {temp_filename}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Remove the temporary file
    os.remove(temp_filename)

    if result.returncode == 0:
        return result.stdout
    else:
        raise Exception(f"Fabric analysis failed: {result.stderr}")