#!/usr/bin/env bash
#task 0 with pupppet
exec {'http header':
command  => 'sudo apt-get update -y;
sudo apt-get install nginx -y;
sudo echo "server {                                                                  
    listen 80;                                                                  
    listen [::]:80 default_server;                                              
    root   /var/www//html;                                                      
    index index.nginx-debian.html index.nginx-debian.html;
    add_header X-Served-By $HOSTNAME;                    
                                                                     
}" > /etc/nginx/sites-available/default;
service nginx restart',
provider => shell,
}
