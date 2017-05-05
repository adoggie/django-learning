


su - postgres -c " pg_ctl initdb -D /data/pgsql"
su - postgres -c " pg_ctl  -D /var/lib/pgsql/9.4/data -l logfile start"
su - postgres -c " pg_ctl start|stop|status -D /var/lib/pgsql/9.4/data"

pg_ctl -D /data/pgsql -l logfile start


'''
pwd=$(cd `dirname $0`;pwd)

echo 'waiting for database is ok..'
sleep 4
echo 'create database lemon..'
su - postgres -c "createdb lemon"
echo 'alter user role..'
su - postgres -c "psql -c \"alter user postgres with password '111111'\" "

echo "create tables.."
cd /opt/lemon/model/django
python manage.py syncdb --noinput
cd -
sleep 1
echo "init data scripts.."
cd /opt/lemon/test
python init_org_user.py
cd -

'''




pg_ctl initdb c:/pgdata
createuser postgres
psql -U postgres 
alter user postgres with password '111111'
add entry edit pg_hba.conf ( 0.0.0.0/0 md5)
edit postgresql.conf   ( listen_address="*")
pg_ctl -D "c:/pgdata" -l logfile start 
createdb testdb 
pg_restore -d testdb c:/testdb.backup
