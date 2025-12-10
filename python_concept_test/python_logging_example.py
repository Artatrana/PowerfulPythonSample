# This script read a file, process it's content, and handles several failure scenarios.
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def read_file(filepath):
    logging.debug(f"Attempting to read the file: {filepath}")

    # INFO: Normal expected step
    if not os.path.exists(filepath):
        logging.error(f"File not found: {filepath}")
        return None

    try:
        logging.info("Opeing file... ")
        with open(filepath, "r") as f:
            content = f.read()
        logging.debug(f"File content length: {len(content)} characters")
        return content
    except PermissionError:
        logging.critical("Permission denied! Cannot read the file.")
    except Exception as e:
        logging.error(f"Unexpected error while reading the file: {e}")

def process_content(content):
    logging.debug("Starting content processing...")

    if not content:
        logging.warning("No content provided! Skipping processing.")
        return None

    # Simulate processing
    try:
        words = content.split()
        logging.info(f"Processing complete. Word count = {len(words)}")
        return words
    except Exception as e:
        logging.error(f"Processing error: {e}")


# --- Driver code ---

print("---- Running File Processing System ----")
#filepath = "sample.txt"
filepath = "python_logging_example.py"

content = read_file(filepath)
words = process_content(content)

logging.info("Script finished.")



