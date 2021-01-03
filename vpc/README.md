vpc
=========

Create / remove VPCs for my lab environment

Requirements
------------

- boto
- boto3
- botocore
- python >= 2.6

Tested with Ansible 2.9.15


Role Variables
--------------

create: true/false


Dependencies
------------

None


Example Playbook
----------------

```
---
- hosts: localhost
  gather_facts: false
  connection: local
  roles:
    - role: vpc
      vars:
        create: true
```

License
-------

BSD

Author Information
------------------

Takashi Sugimura @sugitk

