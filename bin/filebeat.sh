#!/bin/bash

BASE=$(readlink -f $(dirname $0))/..

pushd $BASE

docker-compose run \
    --rm \
    filebeat \
        -e -c /usr/share/filebeat/filebeat.yml -d "execute"

popd