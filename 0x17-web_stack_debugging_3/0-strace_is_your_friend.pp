
# Using strace, find out why Apache is returning a 500 error.
#Once you find the issue, fix it and then automate it using Puppet
exec { 'debugging':
path     => '/usr/bin/:/bin/:/usr/sbin/',
provider => 'shell',
command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
