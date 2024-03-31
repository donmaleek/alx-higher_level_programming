#!/bin/bash
# Usage: ./check_response_size.sh <URL>
echo "$(curl -sS --output /dev/null --write-out "%{size_download}" "$1")"




