#Creates Sets up client SSH configuration file
file_line { 'ssh_config':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'PasswordAuthentication no',
    multiple => 'true'
}
file_line { 'ssh_config_2':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => 'IdentityFile ~/.ssh/holberton',
    multiple => 'true'
}
