#!/bin/bash

echo "Killed container $(docker kill backend-api)"
echo "Removed container $(docker rm backend-api)"