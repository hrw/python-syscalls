#!/usr/bin/python3

import syscalls

system_calls = syscalls.syscalls_dict()

for test_call in ['openat', 'osf_uadmin', 'nosuchcall']:
    try:
        print(f"System call '{test_call}' has number: {system_calls[test_call]}")
    except syscalls.NoSuchSystemCall:
        print(f"No such system call '{test_call}' on any architecture")
    except syscalls.NotSupportedSystemCall:
        print(f"System call '{test_call}' is not supported on this "
              "architecture")
