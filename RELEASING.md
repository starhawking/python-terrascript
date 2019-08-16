## Creating a new release

Steps for creating a new release of Terrascript (as of August 2019).

* Create a new branch ``release-x.x.x`` from ``develop-x.x``. 
```
git checkout -b release-0.6.1
```
* Update ``__version__`` in ``terrascript.__init__.py``.
* Update ``CHANGELOG.md`` in the ``develop`` branch and copy file into this ``release-x.x.x`` branch.
* Run ``make test`` inside the ``tests/`` folder to verify that the JSON configurations are valid.
* Commit and push the branch ``release-x.x.x`` to Github.
```
git commit -a -m 'Preparing release 0.6.1'
git push origin release-0.6.1
```
* Check whether all tests on [Travis-CI](https://www.travis-ci.org/mjuenema/python-terrascript) pass.
* Fix any problems before continuing.
* Tag the revision ``x.x.x`` and push the tag to Github.
```
git tag -a 0.6.1 -m 'Release 0.6.1'
git push --tags
```
* Upload the release to [PyPi Test](https://test.pypi.org/project/terrascript/).
```
python3 setup.py sdist bdist_wheel
ls dist/
/usr/bin/python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
* **TODO**: Test installing package from PyPi Test.
* Upload the release to [PyPi](https://pypi.org/project/terrascript/).
```
/usr/bin/python3 -m twine upload  dist/*
```
* Merge the branch ``release-x.x.x`` into ``develop-x.x`` and push to Github.
```
git checkout develop-0.6
git merge release-0.6.1
git push origin develop-0.6
```
* Merge the branch ``release-x.x.x`` into ``master`` and push to Github (currently only done for 0.8.x releases).
```
git checkout master
git merge release-0.6.1
git push origin master
git checkout develop-0.6
```
* Delete branch ``release-x.x.x``.
```
git push --delete origin release-0.6.1
```
* Review and update the link to PyPi in ``README.md`` in the ``develop`` branch.
