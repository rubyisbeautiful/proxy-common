import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_proxy_file(host):
    f = host.file('/etc/profile.d/proxy.sh')

    assert not f.is_file
