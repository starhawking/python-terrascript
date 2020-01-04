Installing Terrascript
----------------------

Terarscript is available from the Python Package Repository PyPi_ or
alternatively from its Github_ repository.

.. _PyPi: https://pypi.org/project/terrascript/#history
.. _Github: https://github.com/mjuenema/python-terrascript


Installing Terrascript from PyPi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is easiest to install Terrascript directly from the Python Package Index.

.. code-block:: console

   $ pip install terrascript

Installing Terrascript from Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Terrascript can also be installed from its Github_ repository.

.. code-block:: console

   $ git clone https://github.com/mjuenema/python-terrascript.git
   $ cd python-terrascript/
   $ git fetch
   $ git fetch --tags
   
The ``master`` branch should be identical to the version on PyPi.

.. code-block:: console

   $ git checkout master
   $ python3 setup.py install

The ``develop`` branch includes the latest changes but may not always
in a stable state. Do not use the ``develop`` branch unless you want 
to submit a merge request on github.

.. code-block:: console

   $ git checkout develop
   $ python3 setup.py install
