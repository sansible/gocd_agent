# GO CD Server

Master: ![Build Status](https://travis-ci.org/ansible-city/gocd_agent.svg?branch=master)  
Develop: ![Build Status](https://travis-ci.org/ansible-city/gocd_agent.svg?branch=develop)

* [ansible.cfg](#ansible-cfg)
* [Dependencies](#dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs GO CD agent.

For more information about GO CD please visit [go.cd/](http://www.go.cd/).




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Dependencies

To install dependencies, add this to your roles.yml

```YAML
---

- name: ansible-city.gocd_agent
  src: git+git@github.com:ansible-city/gocd_agent.git
  version: origin/master # or any other tag/branch
```

and run `ansible-galaxy install -p . -r roles.yml`




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
        server: IP.OR.URL.OF.THE.SERVER
```
