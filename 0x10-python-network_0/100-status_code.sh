#!/bin/bash
# Bash script
curl -so /dev/null -w "%{http_code}" "$1"
