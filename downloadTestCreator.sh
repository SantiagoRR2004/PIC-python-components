#!/bin/bash

# Set the repository URL and directory
REPO_URL="https://github.com/SantiagoRR2004/GRIA-TestCreator.git"
DIR_NAME="TestCreator"

# Function to update the repository
update_repo() {
    echo "Updating repository..."
    git pull
}

# Check if the directory exists
if [ -d "$DIR_NAME" ]; then
    echo "Directory '$DIR_NAME' exists. Checking for updates..."
    cd "$DIR_NAME" || exit
    # Check if there are any changes to pull
    git remote update
    LOCAL=$(git rev-parse @)
    REMOTE=$(git rev-parse @{u})
    BASE=$(git merge-base @ @{u})

    if [ "$LOCAL" = "$REMOTE" ]; then
        echo "Repository is up-to-date. No action required."
    elif [ "$LOCAL" = "$BASE" ]; then
        echo "Local repository is behind. Updating..."
        update_repo
    else
        echo "Repository is ahead of remote or diverged. Please resolve manually."
    fi
else
    echo "Directory '$DIR_NAME' does not exist. Cloning repository..."
    git clone "$REPO_URL" "$DIR_NAME"
    cd "$DIR_NAME" || exit
fi
