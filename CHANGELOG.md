# Version 1.0

- Drop support for Python 2
- New option: --albums: Create album directories and symlink photos there.
  (This feature cannot be used on Windows because it needs symlinks)
- New option: --skip-errors: Don't quit on error, but go to the next download
- Improve guessing of file type when downloading videos

# Version 0.9

- Better error handling of ContentTooShortError
- Small change in output
- Published as a universal wheel

# Version 0.8

- Fix encoding exception thrown in Python 3
- Fix error related to Content-Disposition header (thanks mherdeg)
- Some metadata changes, especially for the new pypi.org website

# Version 0.7

- Support both Python 3 and Python 2
- Be more tolerant of network errors
- Improve documentation

# Version 0.6:

- Download GIF files too, instead of throwing an exception
- Be more tolerant of network errors

# Version 0.5:

- Small aesthetic change in output

# Version 0.4:

- Always download "Original" or "Original Video"
- Don't use characters in filenames that Windows cannot handle
- Fix for bug affecting wrong filename extension
- Automatically retry on "connection reset by peer"
- README.rst now in reStructuredText format

To make sure the bug fixes are applied, redownload your backup from scratch.

# Version 0.3:

- Fix crash when image title contains forward slash
