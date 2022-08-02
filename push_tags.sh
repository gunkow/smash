#!/usr/bin/env bash

set -e

input="tags.txt"
while IFS= read -r line
do
  echo "$line"
  git tag $line
  git push $line
done < "$input"