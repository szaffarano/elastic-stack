#!/bin/bash

docker exec \
	-it elk_db_1 \
	psql -U poc -c "$@"
