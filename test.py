#!/usr/bin/python3

import os
import syscalls

system_calls = syscalls.syscalls_dict()

for test_call in ['openat', 'osf_uadmin', 'nosuchcall']:
    try:
        print(f"System call '{test_call}' on {os.uname().machine} has number: "
              f"{system_calls[test_call]}")
    except syscalls.NoSuchSystemCall:
        print(f"No such system call '{test_call}' on any architecture")
    except syscalls.NotSupportedSystemCall:
        print(f"System call '{test_call}' is not supported on this "
              "architecture")

print('--')

for test_call in ['openat', 'osf_uadmin', 'nosuchcall']:
    try:
        print(f"System call '{test_call}' on {os.uname().machine} has number: "
              f"{system_calls.get(test_call)}")
    except syscalls.NoSuchSystemCall:
        print(f"No such system call '{test_call}' on any architecture")
    except syscalls.NotSupportedSystemCall:
        print(f"System call '{test_call}' is not supported on this "
              "architecture")

print('--')

for test_call in ['openat', 'osf_uadmin', 'nosuchcall']:
    try:
        print(f"System call '{test_call}' on arm64 has number: "
              f"{system_calls.get(test_call, 'arm64')}")
    except syscalls.NoSuchSystemCall:
        print(f"No such system call '{test_call}' on any architecture")
    except syscalls.NotSupportedSystemCall:
        print(f"System call '{test_call}' is not supported on this "
              "architecture")
