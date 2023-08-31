#!/bin/bash
#Get content-length of http headers
curl -s -I "$1" | wc -c

