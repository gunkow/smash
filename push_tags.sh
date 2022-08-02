#!/usr/bin/env bash

set -e
echo "$export"
input="tags.txt"
while IFS= read -r line
do
  echo "$line"
  git tag $line
  git push origin $line
done < "$input"