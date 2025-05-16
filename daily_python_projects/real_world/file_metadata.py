# This project is designed for learners who know Python fundamentals and are learning to build real-world programs.
# This Python command-line tool extracts metadata from files in a specified directory and displays it.
# Metadata includes the file size, creation date, modification date, and file type.
# Users can see a list of all files in a directory, including files in subdirectories, along with their metadata.
# The results can also be saved into a CSV file for later use or analysis.

import os
import csv
from datetime import datetime

def get_file_metadata(file_path):
    """Get metadata for a given file."""
    try:
        # Get file size in bytes
        file_size = os.path.getsize(file_path)
        # Get creation and modification time
        creation_time = os.path.getctime(file_path)
        modification_time = os.path.getmtime(file_path)

        # Convert timestamps to human-readable format
        creation_time = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        modification_time = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
        # Get file extension/type
        file_type = os.path.splitext(file_path)[-1]
        return {
            "file_path": file_path,
            "file_size": file_size,
            "creation_time": creation_time,
            "modification_time": modification_time,
            "file_type": file_type
        }
    except Exception as e:
        print(f"Error getting metadata for {file_path}: {e}")
        return None

def scan_directory(directory):
    """Scan the given directory and subdirectories for files."""
    file_metadata = []
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            metadata = get_file_metadata(file_path)
            if metadata:
                file_metadata.append(metadata)
    return file_metadata

def save_metadata_to_csv(file_metadata, output_file):
    """Save file metadata to a CSV file."""
    try:
        with open(output_file,mode='w', newline='') as file:
            writer = csv.DictWriter(file,fieldnames=file_metadata[0].keys())
            writer.writeheader()
            writer.writerows(file_metadata)
            print(f"Metadata saved to {output_file}")
    except Exception as e:
        print(f"Error saving metadata to CSV: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path to scan: ")
    file_metadata = scan_directory(directory)

    print("\nMetadata for all files:")
    for data in file_metadata:
        print(f"Path: {data['file_path']}, Size: {data['file_size']} bytes, Created: {data['creation_time']}, Modified: {data['modification_time']}, Type: {data['file_type']}")

    # Save metadata to CSV
    save_to_csv = input("\nDo you want to save the metadata to a CSV file? (y/n): ").lower()
    if save_to_csv == 'y':
        output_file = input("Enter the output CSV file name (e.g., metadata.csv): ")
        save_metadata_to_csv(file_metadata, output_file)



