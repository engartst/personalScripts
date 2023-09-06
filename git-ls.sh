#!/bin/bash

for f in $(git ls-files); do git --no-pager log --color -1 --date=short --pretty=format:'%C(cyan)%ai%Creset' -- $f ; echo  " $f"; done |sort -r
