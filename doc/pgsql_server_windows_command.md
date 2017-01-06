

pg_ctl initdb c:/pgdata
createuser postgres
psql -U postgres 
alter user postgres with password '111111'
add entry into pg_hba.conf ( 0.0.0.0/0 md5)
edit postgresql.conf   ( listen_address="*")
pg_ctl -D "c:/pgdata" -l logfile start 

createdb testdb 
pg_restore -d testdb c:/testdb.backup