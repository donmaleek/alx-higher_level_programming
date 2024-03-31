#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Send a request to the URL and get the size of the response body in bytes
response=$(curl -sS --output /dev/null --write-out "%{size_download}" "$url")

# Display the size of the response body
echo "Size of the response body: $response bytes"

