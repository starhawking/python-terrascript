Installing Terrascript
----------------------

Terarscript is available from the Python Package Repository PyPi_ or
alternatively from its Github_.

As Terraform introduced major changes in their 0.12 release there are 
currently different versions of Terrascript for 0.11.x and 0.12.x 
releases of Terraform. 

.. _PyPi: https://pypi.org/project/terrascript/#history
.. _Github: https://github.com/mjuenema/python-terrascript


Installing Terrascript from PyPi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Terrascript versions 0.6.x support Terraform 0.11.x.

.. code-block:: console

   $ pip install terrascript==0.6.1
   
Terrascript versions 0.7.x support Terraform 0.12.x.

.. note:: Terrascript 0.7.0 has not been released yet.

.. code-block:: console

   $ pip install terrascript==0.7.0


Installing Terrascript from Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Terrascript can also be installed from its Github_ repository.

.. code-block:: console

   $ git clone git@github.com:mjuenema/python-terrascript.git
   $ cd python-terrascript/
   $ git fetch
   $ git fetch --tags
   
Like the installation from PyPi_ one currently has to choose the right
version to match Terraform 0.11.x or Terrform 0.12x.

Terrascript versions 0.6.x support Terraform 0.11.x.

.. code-block:: console

   $ git checkout 0.6.1
   $ python3 setup.py install
   
Terrascript versions 0.7.x support Terraform 0.12.x.

.. note:: Terrascript 0.7.0 has not been released yet.

.. code-block:: console

   $ git checkout 0.7.0
   $ python3 setup.py install
   
There are also separate ``develop-0.6`` and ``develop-0.7`` branches that
include the latest code changes. And for completeness the ``develop`` branch
currently contains work towards Terrascript 0.8.0. Check the ``README.md``
file for more details. 