#!/bin/bash

BASE=$(readlink -f $(dirname $0))

docker exec \
	-it elk_db_1 \
	psql -U poc -c 'drop table if exists test'

docker exec \
	-it elk_db_1 \
	psql -U poc -c 'create table if not exists test (id integer not null primary key, txdate timestamp, description varchar(256))'


$BASE/insert.sh 1 "20012018 10:22:10" "hola a"
$BASE/insert.sh 2 "21012018 11:02:00" "hola b"
$BASE/insert.sh 3 "22012018 11:31:00" "hola c"
$BASE/insert.sh 4 "23012018 12:33:00" "hola d"
$BASE/insert.sh 5 "24012018 10:12:15" "hola e"
