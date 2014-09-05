
## Postgres

DB_DIR=/tmp/postgres_db_tmp
mkdir -p $DB_DIR
initdb $DB_DIR
postgres -D $DB_DIR

psql -d postgres
