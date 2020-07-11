# NOTE: Make sure to update version number
# pip install twine wheel
rm -rf build/*
rm -rf dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
