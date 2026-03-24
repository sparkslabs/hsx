
all:
	@echo "Targets"
	@echo "devinstall - install locally with 'break system packages'"
	@echo "dist   - Build package for PyPI"
	@echo "upload - upload to pypi"


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
