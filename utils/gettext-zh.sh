#! /bin/sh

iconv -t UTF-8 | sed 's/[a-zA-Z0-9[:punct:][:space:]]//g' | grep -v  '^\s*$'
