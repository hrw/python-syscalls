# What is it?

This is very simple code to get system call number/name and availability from
Python level. Reuses data from my [system call
table](https://marcin.juszkiewicz.com.pl/download/tables/syscalls.html) page.

# Usage in Python

Please check "bin/syscall" script and files in "examples/" directory.

# Packages

## Debian (and derived)

I provide source and binary package to install at
https://debian.juszkiewicz.com.pl/python-system-calls/ site.

Tested under:

- Debian 10 'buster'
- Debian 11 'bullseye'
- Debian 'sid'
- Ubuntu 20.04 'focal'

## Fedora

Package for Fedora 35 and rawhide is available in distribution repositories.

## Other distributions

I do not plan to work on packaging for other distributions. Package is available
on Pypi so `pip install system-calls` should work.
