#!/usr/bin/env python
from setuptools import setup

setup(
    name='backup_all_my_flickr_photos',
    version='0.1',
    description="A script to download all photos and videos in your Flickr account",
    author="David D Lowe",
    author_email="daviddlowe.flimm@gmail.com",
    url="https://github.com/Flimm/backup-all-my-flickr-photos",
    download_url="https://github.com/Flimm/backup-all-my-flickr-photos/tarball/0.01",
    scripts=['bin/backup-all-my-flickr-photos'],
    install_requires=[
        'flickr_api',
        'humanfriendly',
    ],
    license='bsd',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Environment :: Console',
    ],
)
