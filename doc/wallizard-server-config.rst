
wallizard.com 
--------------

service loading: 
  1. nginx
  2. docker start webgis / website 
  3. docker exec -it webgis /bin/bash 
     bash /home/run/start.sh 
  4. docker exec -it webgis /bin/bash
     bash /home/binpack/nginx/start.sh 
     bash /home/binpack/postgresql/start.sh 
     
  5. shellinaboxd 
     sudo shellinaboxd -b  -s /:SSH -c /var/lib/shellinabox -u shellinabox
