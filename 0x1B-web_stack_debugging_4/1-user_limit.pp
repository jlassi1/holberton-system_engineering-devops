# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.                                                           
exec {'holberton hard':
path     => ['/usr/bin/'],
command  => "sudo sed -i 's/^holberton hard /holberton hard nofile git 32000/g' /etc/security/limits.conf",
provider => 'shell',
}

exec {'holberton soft':
path     => ['/usr/bin/'],
command  => "sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 32000/g' /etc/security/limits.conf",
provider => 'shell',
}
