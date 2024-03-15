Notes on development process
============================

Tried to do this script with best practises.

First step - Development setup
------------------------------

1. Setup postgresql server `script <https://raw.githubusercontent.com/linuxacademy/content-python3-sysadmin/master/helpers/db_setup.sh>`_
2. Setup postgresql client `Postgresql download site <https://www.postgresql.org/download/linux/redhat/>`_
    * check connection to server:

        ``psql postgres://user:password@IP.address.of.server``

3. Make a development directory, eg:

    ``mkdir ~/dev/pgbackup && cd ~/dev/pgbackup``
    
4. Install pipenv (virtual enviroment management tool) [pipenv site](https://pipenv.pypa.io/en/latest/)

    ``pip install --user pipenv``
    
5. Create virtual enviroment for project
    * **which** must be installed

        ``pipenv --python $(which python3.6)``

This should make an virtual enviroment in a ~/usr/local/share/virtualenvs/ directory, and additionally it creates Pipfile to track dependencies and reqiurements in current directory (pgbackup)

NOTE: if something went wrong during creation of venv - remove current virtualenv and re-create it using more specific python notation

        ``sudo python3.6 -m pip install pipenv``

        ``python3.6 -m pipenv --rm``

        ``python3.6 -m pipenv install --python=$(which python3.6)``

Second step - README Driven Development
---------------------------------------

Creation of this README

NOTE: Documentation in Python ecosystem is most often written in [reStructuredText](https://docutils.sourceforge.io/rst.html)