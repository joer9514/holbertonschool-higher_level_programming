#!/bin/bash
# Bash script
curl -sI "$1" | grep "Allow" | cut -d" " -f2-
