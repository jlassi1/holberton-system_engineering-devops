#!/usr/bin/env bash
#task 0 with pupppet
exec {'http header':
command  => 'sudo apt-get update -y;
sudo apt-get install nginx -y;
sudo sed -i "45i \\\n\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf;
service nginx restart',
provider => shell,
}
