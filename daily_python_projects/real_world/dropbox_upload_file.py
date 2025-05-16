# This python program will upload file into Drop box folder

import dropbox
import os

# Replace this with your Dropbox access token
ACCESS_TOKEN = ""

def upload_to_dropbox(file_path, dropbox_path):
    """Uploads a file to Dropbox."""
    try:
        # Connect to drop box
        dbx = dropbox.Dropbox(ACCESS_TOKEN)

        # Open the file to upload
        with open(file_path, "rb") as f:
            # Upload the file
            dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
        print(f"File '{file_path}' uploaded successfully to '{dropbox_path}' in Dropbox.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except dropbox.exceptions.AuthError:
        print("Error: Invalid Dropbox access token.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__== "__main__":
    # local file to upload
    local_file = "websites.txt"
    # Path in Dropbox (e.g., root folder or subfolder path)
    dropbox_destination = "/Apps/websites.txt"
    # Call the upload function
    upload_to_dropbox(local_file, dropbox_destination)




