# NOTE: Make sure to update version number in pyproject.toml

# Install reps needed
# pip install twine wheel build
rm -rf build/*
rm -rf dist/*
python -m build
twine upload dist/*
