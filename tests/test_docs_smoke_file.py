import pytest
from pathlib import Path

# Define the expected file path and content
EXPECTED_FILE_PATH = Path("docs/code_agent_smoke.md")
EXPECTED_CONTENT = "Smoke test for PR automation."

def test_code_agent_smoke_file_exists():
    """
    Verify that the docs/code_agent_smoke.md file exists after implementation.
    """
    assert EXPECTED_FILE_PATH.exists(), f"File {EXPECTED_FILE_PATH} does not exist."

def test_code_agent_smoke_file_content_is_correct():
    """
    Verify that the content of docs/code_agent_smoke.md is exactly as specified.
    """
    # Ensure the file exists before trying to read it
    assert EXPECTED_FILE_PATH.exists(), f"File {EXPECTED_FILE_PATH} does not exist, cannot check content."

    with open(EXPECTED_FILE_PATH, "r") as f:
        content = f.read().strip() # .strip() to handle potential trailing newlines

    assert content == EXPECTED_CONTENT, \
        f"Content of {EXPECTED_FILE_PATH} is incorrect. Expected '{EXPECTED_CONTENT}', got '{content}'."
