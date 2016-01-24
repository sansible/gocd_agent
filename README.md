# Go CD Agent

Master: [![Build Status](https://travis-ci.org/ansible-city/gocd_agent.svg?branch=master)](https://travis-ci.org/ansible-city/gocd_agent)  
Develop: [![Build Status](https://travis-ci.org/ansible-city/gocd_agent.svg?branch=develop)](https://travis-ci.org/ansible-city/gocd_agent)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Go CD Agent.

For more information about GO CD please visit [go.cd/](http://www.go.cd/).




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

This role has a "java" dependency. You can let this role install Oracle
Java 7, or install it yourself and set `gocd_agent.dependencies.skip_java`
to `yes`.

To install this role run `ansible-galaxy install ansible-city.gocd_agent`
or add this to your `roles.yml`

```YAML
- name: ansible-city.gocd_agent
  version: v1.0
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
    - name: ansible-city.gocd_agent
      gocd_agent:
        server: IP.OR.URL.OF.THE.GOCD.SERVER
```
