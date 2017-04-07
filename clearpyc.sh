#!/bin/sh
cdir=$(pwd)
#remove all the .pyc file under the directory
find . -name '*.pyc' -type f -delete
