


su - postgres -c " pg_ctl initdb -D /data/pgsql"
su - postgres -c " pg_ctl start|stop|status -D /var/lib/pgsql/9.4/data"

pg_ctl -D /data/pgsql -l logfile start





pg_ctl initdb c:/pgdata
createuser postgres
psql -U postgres 
alter user postgres with password '111111'
add entry edit pg_hba.conf ( 0.0.0.0/0 md5)
edit postgresql.conf   ( listen_address="*")
pg_ctl -D "c:/pgdata" -l logfile start 
createdb testdb 
pg_restore -d testdb c:/testdb.backup
