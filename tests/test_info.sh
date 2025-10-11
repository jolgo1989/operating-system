#!/bin/bash

echo "=================================================="
echo "Bash Script Test"
echo "=================================================="
echo "Bash version: $BASH_VERSION"
echo "Current directory: $(pwd)"
echo "Files in directory:"
for file in *; do
    echo "  - $file"
done
echo "=================================================="