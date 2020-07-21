# GoCD Agent

Please see the Sansible readme for information on how to
[contribure](https://github.com/sansible/sansible)

Master: [![Build Status](https://travis-ci.org/sansible/gocd_agent.svg?branch=master)](https://travis-ci.org/sansible/gocd_agent)  
Develop: [![Build Status](https://travis-ci.org/sansible/gocd_agent.svg?branch=develop)](https://travis-ci.org/sansible/gocd_agent)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs GoCD Agent, for GoCD Server installation please
see the [Sansible GoCD Server Role](https://github.com/sansible/gocd_server).
Multiple agents are installed by default (see ```sansible_gocd_agent_no_of_agents```
in defaults.yml).

For more information about GoCD please visit
[https://www.gocd.org/](https://www.gocd.org/).


## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.gocd_agent`
or add this to your `roles.yml`

```YAML
- name: sansible.gocd_agent
  version: v5.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`.

The `sansible.users_and_groups` role is required to use this
role.


## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs GoCD agent and all it's dependencies.
* `configure` - Configure and ensures that the agents are running.


## Examples

To simply install GoCD agent and specify number of agents
(the default is 2):

```YAML
- name: Install GoCD Agent
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
      sansible_gocd_agent_no_of_agents: 4
      sansible_gocd_agent_server_url: https://go-server:8154/go
```

Build GoCD agent with AWS profile configured

```YAML
- name: Install GoCD Agent
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
