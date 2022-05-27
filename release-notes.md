# Releasing

    vim CHANGELOG.md setup.py .travis.yml README.md
    python3 setup.py bdist_wheel
    git commit -m "Release 1.X"
    git tag v1.X
    git push --tags
    twine upload dist/backup_all_my_flickr_photos-1.X-py3-none-any.whl
