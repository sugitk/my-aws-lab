Manage my AWS lab using Ansible
=================================

To create VPC:

```
$ ansible-playbook vpc.yml -e create=true
```

To remove VPC:

```
$ ansible-playbook vpc.yml -e create=false
```

To add EC2 instances in VPC:

```
$ ansible-playbook ec2.yml -e create=true
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

![lab diagram](my_lab.png)

