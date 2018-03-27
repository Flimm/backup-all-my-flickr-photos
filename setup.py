#!/usr/bin/env python
from setuptools import setup
import os

version='0.7'


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "rb") as f:
    long_description = f.read().decode("UTF-8")

setup(
    name='backup_all_my_flickr_photos',
    version=version,
    description="A script to download all photos and videos in your Flickr account",
    long_description=long_description,
    author="David D Lowe",
    author_email="daviddlowe.flimm@gmail.com",
    url="https://github.com/Flimm/backup-all-my-flickr-photos",
    download_url="https://github.com/Flimm/backup-all-my-flickr-photos/tarball/v%s" % (version,),
    scripts=['bin/backup-all-my-flickr-photos'],
    install_requires=[
        'flickr_api',
        'future',
        'humanfriendly',
    ],
    license='bsd',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
    ],
)
