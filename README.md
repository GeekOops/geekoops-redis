[![Test deployment](https://github.com/GeekOops/geekoops-redis/actions/workflows/CI.yml/badge.svg)](https://github.com/GeekOops/geekoops-redis/actions/workflows/CI.yml)

# redis role

Configurable ansible role for setting up the redis object store. Works with

- openSUSE Leap 15.4 -> tested


## Role Variables
--------------

You can set the following variables to configure the role. Here listed are the variables and their default settings.


| Value | Description | Default |
|-------|-------------|---------|
| redis_instancename | name of the instance |'default'|
| redis_port| TCP port |  6379 |
| redis_bind_interface| TCP listen interface| 127.0.0.1|
| redis_timeout | | 0 |
| redis_loglevel| | "notice" |
| redis_logdir | output directory of logfiles | /var/log/redis/ |
| redis_databases | 16 |
| redis_rdbcompression| | "yes" |
| redis_dbdir | | /var/lib/redis

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: jellyfish
      roles:
         - { role: geekoops-redis, redis_instancename: "default"}

An advanced example for the imaginary `jellyfish` test server

    - hosts: jellyfish
      roles:
         - role: geekoops-redis
           vars:
             redis_instancename: "cloud"
         - role: geekoops-redis
           vars:
             redis_instancename: "www"

## License

MIT

# Development
- Test on 15.3
