# Go CD Agent

Please see the Sansible readme for information on how to
[contribure](https://github.com/sansible/sansible)

Master: [![Build Status](https://travis-ci.org/sansible/gocd_agent.svg?branch=master)](https://travis-ci.org/sansible/gocd_agent)  
Develop: [![Build Status](https://travis-ci.org/sansible/gocd_agent.svg?branch=develop)](https://travis-ci.org/sansible/gocd_agent)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Go CD Agent, for GO CD Server installation please
see the [Sansible GO CD Server Role](https://github.com/sansible/gocd_server)

For more information about GO CD please visit
[https://www.gocd.org/](https://www.gocd.org/).


## Installation and Dependencies

This role has a "java" dependency. You can let this role install Oracle
Java 8, or install it yourself and set
`sansible_gocd_agent_dependencies_skip_java` to `yes`.

AWS CLI tools are also installed by default, you can turn this feature off
by setting `sansible_gocd_agent_aws_install_cli` to `no`.

To install this role run `ansible-galaxy install sansible.gocd_agent`
or add this to your `roles.yml`

```YAML
- name: sansible.gocd_agent
  version: v3.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Go CD agent and all it's dependencies.
* `configure` - Configure and ensures that the agents are running.


## Examples

To simply install GO CD agent:

```YAML
- name: Install GO CD Agent
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - name: sansible.gocd_agent
      sansible_gocd_agent_server_url: https://127.0.0.1:8154/go (Change the IP address 127.0.0.1 to the hostname or IP address of your GoCD server.)
```

Build GO CD agent for AWS ASG:

```YAML
- name: Install GO CD Agent
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - name: sansible.gocd_agent
      sansible_gocd_agent_aws_gocd_server_lookup_filters:
        "tag:environment": prd
        "tag:role": gocd_server
        vpc-id: vpc-123456
      sansible_gocd_agent_aws_s3_secret_files:
        - s3_path: s3://config.my.org.domain/gocd_agent/prd/ssh/id_rsa
          local_path: /home/go/.ssh
          mode: 0600
        - s3_path: s3://config.my.org.domain/gocd_agent/prd/ssh/id_rsa.pub
          local_path: /home/go/.ssh
          mode: 0600
```

Build Go CD agent with AWS profile configured

```YAML
- name: Install GO CD Agent
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - name: sansible.gocd_agent
      sansible_gocd_agent_aws_gocd_server_lookup_filters:
        "tag:environment": prd
        "tag:role": gocd_server
        vpc-id: vpc-123456
      sansible_gocd_agent_aws_profiles:
        - name: production_access
          config:
            role_arn: "arn:aws:iam::123456654321:role/ReleaseBot"
            source_profile: default
            s3:
              max_queue_size: 1000
```

This will create the following `~/.aws/credentials`.

```
[production_access]
s3 =
  max_queue_size = 1000
role_arn = arn:aws:iam::123456654321:role/ReleaseBot
source_profile = default
```
