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

NOTE: to upgrade python version for  virtual enviroment use:
    1. ``pipenv --rm`` to destroy the existing virtualenv

    2. Edit the python_version line of your Pipfile to the desired Python version

    3. ``pipenv update`` to create the new virtualenv and update your dependencies

Second step - README Driven Development
---------------------------------------

Creation of this README

NOTE: Documentation in Python ecosystem is most often written in [reStructuredText](https://docutils.sourceforge.io/rst.html)

Third step - Directories and base files
---------------------------------------

    /
        src/                        - source directory
            
            pgbackup/               - project files

                __init__.py         - file for Python to figure out: structure and packages/modules of project, and potentailly contain submodules

            test/                   - automated tests directory



    `setup.py <https://setuptools.pypa.io/en/latest/setuptools.html#basic-use>`_            - file for sake of this app being installable (used for setup tools lib)

    `Makefile <https://www.gnu.org/software/make/manual/make.html>`_ - file for installing dependencies for script

Note: To check if setup.py is correct in ``pipenv shell`` run ``pip install -e .``
      Then to remove this package in venv use: ``pip uninstall pgbackup``

Development process
-------------------

Test driven development was used (RED > GREEN > REFACTOR). At first tests were created.

Baisiclly how it works: run tests -> fix everything asap -> check tests /if okey proceed -> refacor code 

At start: ``pipenv install --dev pytest`` as a development dependency

Creating the cli interface first - write test for (un)expected use cases and debug from there
Make test a bit more flexible thanks to ``@pytest.fixture``

