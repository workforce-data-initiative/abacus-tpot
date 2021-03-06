# abacus-tpot
Analysis Library

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3](https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/python-3-shield.svg)](https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/)
[![Updates](https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/shield.svg)](https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/)
[![CircleCI](https://circleci.com/gh/workforce-data-initiative/tpot-abacus.svg?style=svg)](https://circleci.com/gh/workforce-data-initiative/tpot-abacus)
[![Coverage Status](https://coveralls.io/repos/github/workforce-data-initiative/tpot-abacus/badge.svg?branch=develop)](https://coveralls.io/github/workforce-data-initiative/tpot-abacus?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/c5a146f4dd1f46bf2eaa/maintainability)](https://codeclimate.com/github/workforce-data-initiative/abacus-tpot/maintainability)

### Installation

Create a Python virtual environment then run:

```bash
pip install abacus-tpot
```

### Development

This project has a `.editorconfig` file to help contributors define and maintain consistent coding styles between different editors and IDEs.

We are using CircleCI for continuous integration.

Found a bug or want to propose something to the team? Create a new issue if it is not listed [here](https://github.com/workforce-data-initiative/tpot-abacus/issues). Even better, feel free to fork this repo, make the changes and raise a PR. We'll be more than happy to review it.

### Testing

Run:
```bash
python setup.py test
```

### Deployment

Automatic Uploading to `testpypi` and `pypi` has been set in the CI and only develop and master branches are deployed to the package repositories respectively.

Ready to deploy? Update the version in `setup.py` and create a new git tag with `git tag $VERSION`. Push the tag to GitHub with `git push --tags`, a new CircleCI build is triggered and will only confirm that the package is ready for uploading. The upload will only happen when `master` or `develop` are pushed and successfully build.

### Docs

Going through [this jupyter notebook](https://github.com/workforce-data-initiative/tpot-abacus/blob/develop/abacus.ipynb) will give you a sense of what the abacus packs in.
