#!/usr/bin/python3

import system_calls

system_calls = system_calls.syscalls()

syscalls_count = {}

for syscall_name in system_calls.names():

    syscalls_count[syscall_name] = 0

    for arch in system_calls.archs():
        try:
            system_calls.get(syscall_name, arch)
            syscalls_count[syscall_name] += 1
        except system_calls.NotSupportedSystemCall:
            pass


for syscall_name in syscalls_count:
    print(f"{syscall_name:<32} {syscalls_count[syscall_name]}")
