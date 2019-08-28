import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_proxy_file(host):
    f = host.file('/etc/profile.d/proxy.sh')

    assert f.is_file


def test_proxy_env_var(host):
    cmd_out = host.run('{}'.format(
        '. /etc/profile.d/proxy.sh && echo $http_proxy'))
    assert cmd_out.stdout.strip() == 'http://127.0.0.1.xip.io:3128'
