ec2
=========

Create EC2 instances for my lab environment

Requirements
------------

- boto
- boto3
- botocore
- python >= 2.6

Tested with Ansible 2.9.15


Role Variables
--------------

create: <TYPE>


Dependencies
------------

vpc


Example Playbook
----------------

```
---
- hosts: localhost
  gather_facts: false
  connection: local
  roles:
    - role: ec2
      vars:
        create: "apdb_rhel7"
```

License
-------

BSD

Author Information
------------------

Takashi Sugimura @sugitk
