## Creating a new release
Steps for creating a new release of Terrascript (as of November 2020).
### Create release branch
Releases should be done from a branch to prevent blocking development.
* Create a new branch ``release/x.x.x`` from ``develop``.
    ```
    git checkout -b release/x.x.x
    ```
* Review and update if needed:
  - ``setup.py``
  - ``CHANGELOG.md``
  - ``CONTRIBUTORS.md``
  - ``DEVELOPMENT.md``
  - ``.travis.yml``
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

### Create release candidates
For each release, one or more release candidates could be created to verify that the release works as expected.
* Update version to `x.x.xrcN` in ``terrascript/__init__.py`` and ``docs/conf.py`` (replace `N` with candidate).
* Tag and push the tag release candidate to Github.
    ```
    git tag -a x.x.xrcN -m 'Release candidate N for x.x.x'
    git push --tags
    ```
* Test installing release candidate from PyPi.
    ```
    mkvirtualenv terrascript-test
    pip install -i https://test.pypi.org/simple/ terrascript==x.x.xrcN
    deactivate
    rmvirtualenv terrascript-test
    ```
* Verify functionality of release candidate.
* Make and commit changes if necessary.

### Finalizing the release
When the release candidate are stable, finish the release.
* Update version to `x.x.x` in ``terrascript/__init__.py`` and ``docs/conf.py``.
* Tag and push the release tag to Github.
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
