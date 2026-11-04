#!/bin/bash

read -p "Enter the command: " command

if command -v "$command" >/dev/null 2>&1; then
    "$command"
    echo "Command executed successfully."
else
    echo "Wrong command!"
fi