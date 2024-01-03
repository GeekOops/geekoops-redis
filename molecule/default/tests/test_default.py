#!/usr/bin/python3
# -*- coding: utf-8 -*-

import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_pingpong(host):
	cmd = host.run("redis-cli -s /var/run/redis/default.sock ping")
	print(cmd.stdout)
	assert "PONG" in cmd.stdout
