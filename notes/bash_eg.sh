#!/bin/bash

# --- 1. Variables ---
USER_NAME=$(whoami)
CURRENT_DATE=$(date +%D)
TEMP_DIR="./temp_cleanup"

# --- 2. The Greeting ---
echo "Hello, $USER_NAME! Today is $CURRENT_DATE."
echo "Starting the mini-cleanup process..."

# --- 3. Logic: Creating a directory and a dummy file ---
if [ ! -d "$TEMP_DIR" ]; then
    mkdir "$TEMP_DIR"
    echo "Created directory: $TEMP_DIR"
fi

touch "$TEMP_DIR/log_$(date +%s).txt"
echo "Log file generated in $TEMP_DIR."

# --- 4. Conclusion ---
echo "Task complete. You're ready to rock!"
