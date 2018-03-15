# proxy-common

## Basic Usage

This role will common proxy settings.  It will optionally install it
in yum's default configuration, optionally install it in bash's defualt profile,
and export it for use in other Ansible roles.

There are many configurable options -- see defaults/main.yml

Role Variables
--------------

You may optionally set the following:

`common_proxy_host`

When this variable remains unset, the entire role essentially does nothing.
This can be useful, for example, to set an entire environment to use a proxy,
but set one host (or a group, tier etc) as the exception and NOT use a proxy
-- by simply setting `proxy_host` to `''` or `~` (YAML for nil)

`common_proxy_port`

If `common_proxy_host` is set, then the port must also be set - there is no
default

`common_proxy_user`

Optional, no default

`common_proxy_pass`

Optional, no default

`common_proxy_set_yum`

Will add the proxy setting to yum.conf.  Default is true

`common_proxy_set_bash`

Will add settings to /etc/profile.d/proxy.sh.  Default is true


Note that you can specify a vault password like this
`common_proxy_pass: "{{ vault_common_proxy_pass }}"`
or inline (preferred), which requires Ansible >= 2.3
```
common_proxy_pass: !vault |
           $ANSIBLE_VAULT;1.1;AES256
           junkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunk
           junkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunk
           junkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunk
           junkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunkjunk
           junk
```


In addition to the variables you set of course, you will also gain
(within the same playbook execution) the `common_proxy`, and `common_proxy_env`
variables.  The former is useful for access to the entire proxy string, while
latter may be read into the environment to set all typical environment variables
at once, like so:

```
environment:
  foo: bar
  http_proxy: "{{ common_proxy }}"
  no_proxy: "{{ common_no_proxy }}"
```

```
environment:
  "{{ common_proxy_env }}"
```

The first is useful when you already have environment variables defined and
you just want to inject the proxy.  The second will cause the environment
to gain: http_proxy, HTTP_PROXY, https_proxy,
HTTPS_PROXY, no_proxy, NO_PROXY


Requirements
------------

N/A

Dependencies
------------

N/A


Example Playbooks
----------------


#### Basic

```
- hosts: all
  tasks:
    - include_role:
      name: rubyisbeautiful.proxy_common
```

License
-------

MIT


Author Information
------------------

rubyisbeautiful
