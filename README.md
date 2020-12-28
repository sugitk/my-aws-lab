Manage my AWS lab using Ansible
=================================

To create:

```
$ ansible-playbook playbook.yml -e create=true
```


To remote:

```
$ ansible-playbook playbook.yml -e create=false
```

Requirements
------------

- boto
- boto3
- botocore
- python >= 2.6

Tested with Ansible 2.9.15

You need to configure a credential to connect AWS.

For example, at ~/.awx/credentials

```
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```


License
-------

BSD

Author Information
------------------

Takashi Sugimura @sugitk

