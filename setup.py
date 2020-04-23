#!/usr/bin/env python
from setuptools import setup
import os

version='1.0'


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), "rb") as f:
    long_description = f.read().decode("UTF-8")

setup(
    name='backup_all_my_flickr_photos',
    version=version,
    description="A script to download all photos and videos in your Flickr account",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="David D Lowe",
    author_email="daviddlowe.flimm@gmail.com",
    url="https://github.com/Flimm/backup-all-my-flickr-photos",
    scripts=['bin/backup-all-my-flickr-photos'],
    install_requires=[
        'flickr_api',
        'humanfriendly',
    ],
    license='bsd',
    project_urls={
        'GitHub': 'https://github.com/Flimm/backup-all-my-flickr-photos',
        'Change log': 'https://github.com/Flimm/backup-all-my-flickr-photos/blob/master/CHANGELOG.md',
    },
    python_requires='>=3.3, <4',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
    ],
)
