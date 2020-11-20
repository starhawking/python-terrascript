## Creating a new release

Steps for creating a new release of Terrascript (as of November 2020).

* Create a new branch ``release/x.x.x`` from ``develop``.
    ```
    git checkout -b release/x.x.x
    ```
* Update ``__version__`` in ``terrascript.__init__.py``.
* Update version in ``docs/conf.py``.
* Review ``setup.py``.
* Update ``CHANGELOG.md``.
* Update ``CONTRIBUTORS.md``.
* Update ``DEVELOPMENT.md``.
* Update ``.travis.yml``.
* Run ``make black``.
* Run ``make test``.
* Run ``make docs``.
* Commit and push the branch ``release/x.x.x`` to Github.
    ```
    git commit -a -m 'Preparing release x.x.x'
    git push origin release/x.x.x
    ```
* Commit (or merge in) any outstanding changes that will got into the next release.
* Check whether all tests on [Travis-CI](https://www.travis-ci.org/mjuenema/python-terrascript) pass.
* Fix any problems before continuing.
* Tag a release candidate for the revision ``x.x.x`` and push the tag to Github.
    ```
    git tag -a x.x.xrc1 -m 'Release candidate 1 for x.x.x'
    git push --tags
    ```
* Test installing release candidate from PyPi.
    ```
    mkvirtualenv terrascript-test
    pip install -i https://test.pypi.org/simple/ terrascript==x.x.xrc1
    deactivate
    rmvirtualenv terrascript-test
    ```
* Verify functionality of release candidate.
* Make and commit changes if necessary.
* Tag the release and push the tag to Github.
    ```
    git tag -a x.x.x -m 'Release x.x.x'
    git push --tags
    ```
* Merge the branch ``release/x.x.x`` into ``master`` and push to Github.
    ```
    git checkout master
    git merge release/x.x.x
    git push origin master
    ```
* Delete branch ``release/x.x.x``.
    ```
    git push --delete origin release/x.x.x
    ```
* Merge ``master``` back into ``develop``.
    ```
    git checkout develop
    git merge master
    git push origin develop
    ```
