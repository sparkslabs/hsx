Random basic dev notes

python -m venv dev-hsx
cd dev-hsx/
source bin/activate
rsync -avz ../hsx/ hsx/
cd hsx
make devinstall
make undevinstall
# pip3 install .
# pip3 uninstall hsx
