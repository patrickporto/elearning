# Contributing

## Submitting patches (bugfix, features, ...)

### Work flow

If you want to contribute some code:

1. Create a branch with an explicit name (like `my-new-feature` or `issue-XX`).
2. Commit your changes.
3. Merge the `master` in your branch.
4. Add you change to the changelog.
5. Submit your pull-request.

### Definition of Done

There are some rules to follow:

* Your contribution should be documented (if needed).
* Your contribution should be tested and the test suite should pass successfully.
* Your code should be mostly project's code style compatible.

## Development setup

You need to install some dependencies to develop:

```shell
pip install pipenv
```

Install the project dependencies through [Pipenv](https://github.com/pypa/pipenv).

```shell
export PIPENV_VENV_IN_PROJECT=true
pipenv --three install --dev
```
