# backup-all-my-flickr-photos

This scripts simply downloads all your Flickr photos and videos into a directory.

# Installation instructions:

## From Pypi

You can install the latest stable release like this:

    pip install backup_all_my_flickr_photos --user # to install in the user directory ~/.local

If you want to install it globally, use this command:

    sudo pip install backup_all_my_flickr_photos

Many people find it easiest to use [`virtualenv`](https://virtualenv.pypa.io/).

## From source

    git clone https://github.com/Flimm/backup-all-my-flickr-photos.git
    cd backup-all-my-flickr-photos
    virtualenv env
    source env/bin/activate
    python setup.py develop # install dependencies and script
    backup-all-my-flickr-photos --help

# Run

    backup-all-my-flickr-photos [--delete] <destination_directory>

This will download all the photos and videos in your account to the destination directory specified.

If you specified the `--delete` flag, it will also delete files in the destination directory that do not correspond to photos or videos in your Flickr account.

On the the first run, you will be prompted to provide an API key and secret, and to authorise the application.
The script will guide you through this process.
The information will get saved to `~/.local/backup-all-my-flickr-photos/`.
