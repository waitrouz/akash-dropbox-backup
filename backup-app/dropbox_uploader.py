#!/usr/bin/env python3

import sys
import os
import dropbox
from dropbox.files import WriteMode

def upload_to_dropbox(file_path, access_token):
    try:
        dbx = dropbox.Dropbox(access_token)
        
        # Extract filename from path
        file_name = os.path.basename(file_path)
        dropbox_path = f'/backups/{file_name}'
        
        with open(file_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
        
        print(f"Successfully uploaded {file_name} to Dropbox")
        return True
        
    except Exception as e:
        print(f"Error uploading to Dropbox: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dropbox_uploader.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    access_token = os.environ.get('DROPBOX_ACCESS_TOKEN')
    
    if not access_token:
        print("DROPBOX_ACCESS_TOKEN environment variable not set")
        sys.exit(1)
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
    
    success = upload_to_dropbox(file_path, access_token)
    sys.exit(0 if success else 1)
