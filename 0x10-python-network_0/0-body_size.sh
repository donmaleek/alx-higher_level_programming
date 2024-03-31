#!/bin/bash
if [ $# -ne 1 ]; then echo "Usage: $0 <URL>"; exit 1; fi
echo "Size of the response body: $(curl -sS --output /dev/null --write-out "%{size_download}" "$1") bytes"



