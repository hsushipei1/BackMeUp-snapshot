#!/bin/bash

#----------------
# Slash searcher 
#----------------
# Use grep to find any "slash" in all *.py files

# Go to main directory
cd ../

# Search for every file
echo "Searching 'slash'..."
grep -R 'slash' *.py

echo "Searching 'SLASH()'..."
grep -R 'SLASH()' *.py
