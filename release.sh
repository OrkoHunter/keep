# NOTE: Make sure to update version number
# pip install twine wheel
rm -rf build/*
rm -rf dist/*
python -m build
twine upload dist/*
