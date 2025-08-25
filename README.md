# Akash to Dropbox Backup Solution

This project demonstrates a reliable backup solution from Akash to Dropbox using PostgreSQL as the primary service and a custom backup application as the secondary service, utilizing Akash's shared memory (shm) feature for efficient file transfer between services.

## Setup Instructions

### 1. Build the Backup Application Docker Image
```
cd backup-app
docker build -t your-dockerhub-username/akash-dropbox-backup:0.1 .
docker push your-dockerhub-username/akash-dropbox-backup:0.1
```

### 2. Create a Dropbox App and Get an Access Token
- Go to https://www.dropbox.com/developers/apps
- Create a new app with App folder access
- Generate an access token

### 3. Update the deploy.yaml File
- Replace `your-dockerhub-username/akash-dropbox-backup:latest` with your actual Docker image
- Replace `your_dropbox_token_here` with your Dropbox access token

## Deploy to Akash via Akash Console
1. Visit https://console.akash.network/
2. Click Deploy
3. Upload your SDL file
4. Follow the instructions on the site

## How It Works

### 1. PostgreSQL Service
- Runs a PostgreSQL database with persistent storage

### 2. Backup Service
- Uses shared memory (`/dev/shm`) for temporary storage of backup files
- Creates compressed backups of the PostgreSQL database
- Uploads backups to Dropbox using the Dropbox API
- Runs on a schedule (currently set to 24-hour intervals)

## Key Features

- **Shared Memory Utilization**: Uses Akash's shm feature for efficient file transfer between services
- **Secure Backups**: Compressed and encrypted transfers to Dropbox
- **Persistent Storage**: PostgreSQL data is stored on persistent volume
- **Automated Process**: Regular backups without manual intervention

## Notes

- Remember to secure your Dropbox access token and database credentials
- Adjust backup frequency based on your needs
- Consider adding backup rotation policies on Dropbox
- Test the backup restoration process regularly

This solution provides a reliable way to backup PostgreSQL databases from Akash deployments to Dropbox, leveraging Akash's shared memory feature for efficient operation.
