# renames file (changes extension from php to phpp)
exec { 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp':
path => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
