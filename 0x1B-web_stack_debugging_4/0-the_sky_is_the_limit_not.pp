
#  getting a huge amount of failed requests.

exec {'comment ULIMIT':
    path     => ['/usr/bin'],
    command  => "sudo sed -i 's/ULIMIT=/#ULIMIT=/g' /etc/default/nginx; sudo service nginx restart",
    provider => 'shell',
}
