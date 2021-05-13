# What is it?

This is very simple code to get system call numbers from Python level.

# Usage

Quite simple:

```python
#!/usr/bin/python3

import syscalls

system_calls = syscalls.syscalls_dict()

for test_call in ['openat', 'osf_uadmin', 'nosuchcall']:
    try:
        print(system_calls[test_call])
    except syscalls.NoSuchSystemCall:
        print(f"No such system call '{test_call}' on any architecture")
    except syscalls.NotSupportedSystemCall:
        print(f"System call '{test_call}' is not supported on this "
              "architecture")
```

# Plans

- add all files required to create wheel
- add to Pypi
