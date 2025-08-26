#!/bin/bash

# Set default backup interval to 24 hours (86400 seconds) if not provided
BACKUP_INTERVAL=${BACKUP_INTERVAL_SECONDS:-86400}

while true; do
# Set timestamp for backup file
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE=/dev/shm/backup_${TIMESTAMP}.sql.gz

# Create PostgreSQL backup
echo "Creating PostgreSQL backup..."
pg_dump -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_DB | gzip > $BACKUP_FILE

# Check if backup was successful
if [ $? -eq 0 ]; then
  echo "Backup created successfully: $BACKUP_FILE"
  
  # Upload to Dropbox
  echo "Uploading to Dropbox..."
  python3 dropbox_uploader.py $BACKUP_FILE
  
  # Clean up
  rm $BACKUP_FILE
  echo "Backup process completed successfully."
else
  echo "Backup creation failed!"
  exit 1
fi

# Sleep for the configured interval
echo "Sleeping for $BACKUP_INTERVAL seconds before next backup..."
sleep $BACKUP_INTERVAL
done
