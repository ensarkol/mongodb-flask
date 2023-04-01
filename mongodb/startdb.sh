#!/bin/bash

docker-compose up -d

slesep 5

docker exec mongo1 /scripts/rs-init.sh