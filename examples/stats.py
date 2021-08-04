#!/usr/bin/python3

import syscalls

popular_syscalls = {}

system_calls = syscalls.syscalls()

for syscall_name in system_calls.names():
    counter = 0

    for arch in system_calls.archs():
        try:
            system_calls.get(syscall_name, arch)
            counter += 1
        except syscalls.NotSupportedSystemCall:
            pass

    try:
        popular_syscalls[counter].append(syscall_name)
    except KeyError:
        popular_syscalls[counter] = []
        popular_syscalls[counter].append(syscall_name)

amount_of_archs = len(system_calls.archs())

for amount in range(1, amount_of_archs + 1):
    try:
        tmp = popular_syscalls[amount]
        print(f"System calls supported on {amount} of {amount_of_archs} "
              "architectures:")
        for syscall in popular_syscalls[amount]:
            print(f"\t{syscall}")
        print("\n")
    except KeyError:
        pass
