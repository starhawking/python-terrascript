## Creating a new release

Steps for creating a new release of Terrascript (as of August 2019).

* Create a new branch ``release-x.x.x`` from ``develop-x.x``. 
```
git checkout -b release-x.x.x
```
* Update ``__version__`` in ``terrascript.__init__.py``.
* Update version in ``docs/conf.py``.
* Review ``setup.py``.
* Update ``CHANGELOG.md``.
* Update ``CONTRIBUTORS.md``.
* Update ``DEVELOPMENT.md``.
* Update ``.travis.yml``.
* Run ``make test``.
* Commit and push the branch ``release-x.x.x`` to Github.
```
git commit -a -m 'Preparing release x.x.x'
git push origin release-x.x.x
```
* Check whether all tests on [Travis-CI](https://www.travis-ci.org/mjuenema/python-terrascript) pass.
* Fix any problems before continuing.
* Tag the revision ``x.x.x`` and push the tag to Github.
```
git tag -a x.x.x -m 'Release x.x.x'
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
* Merge the branch ``release-x.x.x`` into ``master`` and push to Github.
```
git checkout master
git merge release-x.x.x
git push origin master
```
* Delete branch ``release-x.x.x``.
```
git push --delete origin release-0.6.1
```
* Review and update the link to PyPi in ``README.md`` in the ``develop`` branch.
