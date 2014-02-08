# [Ansible WebPlaybooks](http://mgcrea.github.io/ansible-web-playbooks) [![Build Status](https://secure.travis-ci.org/mgcrea/ansible-web-playbooks.png?branch=master)](http://travis-ci.org/#!/mgcrea/ansible-web-playbooks)

Set of playbook roles to orchestrate your web servers, powered by Ansible.

>
    $ tree roles -L 2
    roles
    ├── ansible
    │   ├── accelerated
    │   ├── facts
    │   └── fireball
    ├── databases
    │   ├── beanstalkd
    │   ├── mongodb
    │   ├── mysql
    │   └── redis
    └── webservers
        ├── apache2
        ├── nginx
        ├── nodejs
        └── php5

## Documentation and examples

+ Check the [documentation](http://mgcrea.github.io/ansible-web-playbooks) and [changelog](https://github.com/mgcrea/ansible-web-playbooks/releases).



## Quick start

+ You can run the playbooks with [Vagrant](http://www.vagrantup.com/)

>
    $ vagrant up
    $ ansible-playbook -i vagrant_inventory playbook.yml --tag apt_update,mongodb,nodejs


## Developers

Clone the repo, `git clone git://github.com/mgcrea/ansible-web-playbooks.git`, [download the latest release](https://github.com/mgcrea/ansible-web-playbooks/zipball/master) or install with npm `npm install ansible-web-playbooks`.

WebPlaybooks is tested with `vagrant` against the latest stable release of Ansible.

>
    $ vagrant up
    $ ansible-playbook -i vagrant_ansible_inventory_default playbook.yml



## Contributing

Please submit all pull requests the against master branch. Thanks!



## Authors

**Olivier Louvignes**

+ http://olouv.com
+ http://github.com/mgcrea



## Copyright and license

    The MIT License

    Copyright (c) 2013-2014 Olivier Louvignes

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
