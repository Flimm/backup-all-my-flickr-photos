backup-all-my-flickr-photos
===========================

.. image:: https://img.shields.io/pypi/v/backup_all_my_flickr_photos.svg
    :target: https://pypi.python.org/pypi/backup_all_my_flickr_photos
.. image:: https://img.shields.io/pypi/l/backup_all_my_flickr_photos.svg
    :target: https://pypi.python.org/pypi/backup_all_my_flickr_photos
.. image:: https://img.shields.io/pypi/wheel/backup_all_my_flickr_photos.svg
    :target: https://pypi.python.org/pypi/backup_all_my_flickr_photos
.. image:: https://img.shields.io/pypi/pyversions/backup_all_my_flickr_photos.svg
    :target: https://pypi.python.org/pypi/backup_all_my_flickr_photos
    
This scripts simply downloads all your Flickr photos and videos into a
directory.

Installation instructions:
==========================

    pip install backup_all_my_flickr_photos

It is recommended to create a Python 2 environment with `Virtualenv
<https://virtualenv.pypa.io/en/stable/installation/>`_ first.


Run
===

::

    backup-all-my-flickr-photos [--delete] <destination_directory>

This will download all the photos and videos in your account to the
destination directory specified.

If you specified the ``--delete`` flag, it will also delete files in the
destination directory that do not correspond to photos or videos in your
Flickr account.

On the the first run, you will be prompted to provide an API key and
secret, and to authorise the application.
The script will guide you through this process.
The information will get saved to
``~/.config/backup-all-my-flickr-photos/``.
