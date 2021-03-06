Manage my AWS lab using Ansible
=================================

To create VPC:

```
$ ansible-playbook vpc_create.yml
```

To remove VPC:

```
$ ansible-playbook vpc_delete.yml
```

To add EC2 instances in VPC for example:

```
$ ansible-playbook ec2_cluster_rhel8.yml
```

To remove all EC2 instances:
```
$ ansible-playbook ec2_wipe.yml
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


VPC diagram
----
![lab diagram](my_lab.png)


