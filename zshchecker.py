import subprocess
import sys

def check_zsh_syntax(file_path):
    try:
        # Run the zsh with the file as input to check for syntax errors
        result = subprocess.run(
            ['zsh', '-n', file_path], 
            capture_output=True, text=True
        )
        # If zsh returns an error, it will be captured in stderr
        if result.returncode != 0:
            # Extract error line from stderr
            error_message = result.stderr
            for line in error_message.splitlines():
                if 'compdef' in line or 'syntax error' in line:
                    print(f"Syntax Error: {line}")
            return error_message
        else:
            print("No syntax errors found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_zsh_syntax.py <path_to_zsh_completion_file>")
    else:
        print("working")
        check_zsh_syntax(sys.argv[1])
