#!/bin/bash

# Ensure the skins/vandal directory exists
mkdir -p skins/phantom

# Read the JSON file and iterate through each key-value pair
jq -r 'to_entries[] | "\(.key) \(.value)"' data/phantom.json | while read -r key url; do
  # Replace spaces with underscores in the key to create a valid filename
  filename=$(echo "$key" | tr ' ' '_')
  # Download the image and save it with the key as the filename
  curl -o "skins/phantom/${filename}.png" "$url"
done