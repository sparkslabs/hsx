
all:
	@echo "Targets"
	@echo
	@echo "bumprev    - Sync all the version strings with VERSION in this directory - prior to release"
	@echo "devinstall - install locally with 'break system packages'"
	@echo "dist       - Build package for PyPI"
	@echo "upload     - upload to pypi"

bumprev:
	./scripts/bump_rev.sh

undevinstall:
	python3 -m pip uninstall hsx  --break-system-package

devinstall:
	python3 -m pip install .  --break-system-package

dist:
	python3 -m build

dist_to_pypi:
	python3 -m twine upload --repository pypi dist/*

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf src/hsx.egg-info/
