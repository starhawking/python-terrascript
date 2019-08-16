## Creating a new release

Steps for creating a new release of Terrascript. **DRAFT**

* Create a new branch ``release-x.x.x`` from ``develop-x.x``. 
* Update ``__version__`` in ``terrascript.__init__.py``.
* Update ``CHANGELOG.md``.
* Run ``make test`` inside the ``tests/`` folder to verify that the JSON configurations are valid.
* Commit the branch ``release-x.x.x`` to Github.
* Check whether all tests on Travis-CI pass.
* Merge the branch ``release-x.x.x`` into ``master``.
* Tag the revision ``x.x.x``.
* Push ``master`` and tag to Github.
* Merge ``master`` back in to ``develop-x.x``.
* Create and upload package to PyPi. 
* Update the ``CHANGELOG.md`` of the ``develop`` branch.
* Delete branch ``release-x.x.x``.