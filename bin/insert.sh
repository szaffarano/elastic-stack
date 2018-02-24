#!/bin/bash

if [ $# -ne 3 ]; then
	echo "MOdo de uso: $0 <id> <fecha> <comentario>"
	exit 1
fi

SQL=$(cat << EOF
insert into test values('$1', to_date('$2', 'DDMMYYYY HH24:MI:SS'), '$3')
EOF
)

docker exec \
	-it elk_db_1 \
	psql -U poc -c "$SQL"
