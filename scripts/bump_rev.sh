#!/bin/bash -x

export VERSION=`cat VERSION`

sed -e "s/^version.*/version = \"$VERSION\"/g" pyproject.toml > pyproject.toml-
mv pyproject.toml-  pyproject.toml

sed -e "s/^__version__.*/__version__ = \"$VERSION\"/g" src/hsx/__init__.py > src/hsx/__init__.py-
mv src/hsx/__init__.py-  src/hsx/__init__.py


sed -e "s/^\*\*Version:\*\*.*/**Version:** $VERSION/g" README.md >README.md-
mv README.md- README.md 
