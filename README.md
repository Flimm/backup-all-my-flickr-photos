backup-all-my-flickr-photos
===========================

[![PyPI](https://img.shields.io/pypi/v/backup_all_my_flickr_photos.svg)](https://pypi.org/project/backup_all_my_flickr_photos/) 
[![PyPI](https://img.shields.io/pypi/l/backup_all_my_flickr_photos.svg)](https://pypi.org/project/backup_all_my_flickr_photos/)
[![PyPI](https://img.shields.io/pypi/wheel/backup_all_my_flickr_photos.svg)](https://pypi.org/project/backup_all_my_flickr_photos/)
[![PyPI](https://img.shields.io/pypi/pyversions/backup_all_my_flickr_photos.svg)](https://pypi.org/project/backup_all_my_flickr_photos/)

This scripts simply downloads all your Flickr photos and videos into a
directory.

Installation instructions:
==========================

    pip3 install backup_all_my_flickr_photos

It is recommended to create a Python 3 environment with
[Virtualenv](https://virtualenv.pypa.io/en/stable/installation/) first.

Run:
====

    backup-all-my-flickr-photos [--delete] <destination_directory>

This will download all the photos and videos in your account to the
destination directory specified.

On the the first run, you will be prompted to provide an API key and
secret, and to authorise the application. The script will guide you
through this process. The information will get saved to
`~/.config/backup-all-my-flickr-photos/`.

The files in the destination folder will be given an appropriate file
extension and will be named with the name of the photo/movie (if it has
a name), followed by an ID number. No other metadata is saved.

Options:
--------

`--delete`:

If you specified the `--delete` flag, it will also delete files in the
destination directory that do not correspond to photos or videos in your
Flickr account.

`--albums`:

In addition to downloading all the photos and videos, this will create a
directory for each album in the destination directory. Each directory will
contain symlinks to the photos and videos that that album contains. This option
cannot be used on Windows, because Windows does not support symlinks.

`--skip-errors` or `-s`:

If an error occurs during the download of a photo or video, usually the script
automatically retries the download a few times. If it still fails, then an
error is printed and the script quits. Use this option if you want it to skip
to the next photo or video.
