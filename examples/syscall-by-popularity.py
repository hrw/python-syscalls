#!/usr/bin/python3

"""
Print syscalls in 'popularity' order.

From entries supported on one architecture to supported on every one.
"""

import syscalls

system_calls = syscalls.syscalls()

syscalls_count = {}

for syscall_name in system_calls.names():

    syscalls_count[syscall_name] = {"amount": 0, "archs": []}

    for arch in system_calls.archs():
        try:
            system_calls.get(syscall_name, arch)
            syscalls_count[syscall_name]["amount"] += 1
            syscalls_count[syscall_name]["archs"].append(arch)
        except syscalls.NotSupportedSystemCall:
            pass

for amount in range(1, len(system_calls.archs()) + 1):
    for syscall_name in syscalls_count:
        if amount == syscalls_count[syscall_name]["amount"]:
            print(f"{syscall_name:<32}"
                  f"{syscalls_count[syscall_name]['archs']}")
