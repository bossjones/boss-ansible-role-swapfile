import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_etc_fstab_file(host):
    fstab = host.file("/etc/fstab")
    assert fstab.contains("/swapfile   none    swap    sw    0   0")
    assert fstab.user == "root"
    assert fstab.group == "root"
    assert fstab.mode == 0o644


def test_swapfile(host):
    swapfile = host.file("/swapfile")
    assert swapfile.user == "root"
    assert swapfile.group == "root"
    assert swapfile.mode == 0o600
    assert swapfile.size == 512000000
