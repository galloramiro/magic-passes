#!/bin/bash

IMAGE=magic_passes 

# Running JupyterLab
docker run --rm --network="host" -p 8888:8888 --name $IMAGE -e GRANT_SUDO=yes -e JUPYTER_ENABLE_LAB=yes --user root -v $PWD/../work:/home/jovyan/work $IMAGE

