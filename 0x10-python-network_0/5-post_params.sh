#!/bin/bash
#send delete req and get body res
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

