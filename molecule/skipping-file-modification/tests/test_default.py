import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_proxy_file(host):
    f = host.file('/etc/profile.d/proxy.sh')

    assert f.is_file


def test_yum_config(host):

    regex = r"http://127\.0\.0\.1\.xip\.io:3128"
    try:
        with open('/etc/yum.conf', 'r', encoding='utf-8') as f:
            contents = f.read
            assert not re.search(regex, contents, re.IGNORECASE)
    except FileNotFoundError:
        assert True


def test_proxy_env_var(host):
    cmd_out = host.run('{}'.format(
        '. /etc/profile.d/proxy.sh && echo $http_proxy'))
    assert cmd_out.stdout.strip() == 'http://127.0.0.1.xip.io:3128'
