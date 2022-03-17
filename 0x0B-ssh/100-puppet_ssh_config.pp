#  make changes to configuration file

file { '/etc/ssh/ssh_config':
  ensure => present,
}
-> exec { 'Declare identity file':
    command => 'echo "    IdentityFile ~/.ssh/school" >>  /etc/ssh/ssh_config',
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec { 'Turn off passwd auth':
    command => 'echo "    PasswordAuthentication no" >>  /etc/ssh/ssh_config',
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
