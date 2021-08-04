#!/usr/bin/python3

import pytest
import syscalls

system_calls = syscalls.syscalls()


def test_x86_64_open():
    assert 2 == system_calls.get("open", "x86_64")


def test_x86_64_openat():
    assert 257 == system_calls.get("openat", "x86_64")


def test_arm64_openat():
    assert 56 == system_calls.get("openat", "arm64")


def test_on_arm64_open_is_not_supported():
    with pytest.raises(syscalls.NotSupportedSystemCall):
        print(system_calls.get("open", "arm64"))


def test_alpha_osf_fuser():
    assert 243 == system_calls.get("osf_fuser", "alpha")


def test_not_existing_system_call():
    with pytest.raises(syscalls.NoSuchSystemCall):
        print(system_calls.get("not-existing-system-call", "arm64"))
