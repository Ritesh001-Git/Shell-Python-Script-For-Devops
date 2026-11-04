#!/bin/bash

dir="/Users/riteshswain/Downloads"

printf 'dir = <%q>\n' "$dir"

ls -ld "$dir"

echo "Expansion test:"
printf '<%s>\n' "$dir"/*