# Content autogenerated. Do not edit.

syscalls_sparc64 = {
    "_llseek": 236,
    "_newselect": 230,
    "_sysctl": 251,
    "accept": 99,
    "accept4": 323,
    "access": 33,
    "acct": 51,
    "add_key": 281,
    "adjtimex": 219,
    "alarm": 27,
    "bdflush": 225,
    "bind": 353,
    "bpf": 349,
    "brk": 17,
    "capget": 21,
    "capset": 22,
    "chdir": 12,
    "chmod": 15,
    "chown": 13,
    "chroot": 61,
    "clock_adjtime": 334,
    "clock_getres": 258,
    "clock_gettime": 257,
    "clock_nanosleep": 259,
    "clock_settime": 256,
    "clone": 217,
    "close": 6,
    "close_range": 436,
    "connect": 98,
    "copy_file_range": 357,
    "creat": 8,
    "create_module": 221,
    "delete_module": 222,
    "dup": 41,
    "dup2": 90,
    "dup3": 320,
    "epoll_create": 193,
    "epoll_create1": 319,
    "epoll_ctl": 194,
    "epoll_pwait": 309,
    "epoll_pwait2": 441,
    "epoll_wait": 195,
    "eventfd": 313,
    "eventfd2": 318,
    "execv": 11,
    "execve": 59,
    "execveat": 350,
    "exit": 1,
    "exit_group": 188,
    "faccessat": 296,
    "faccessat2": 439,
    "fadvise64": 209,
    "fadvise64_64": 210,
    "fallocate": 314,
    "fanotify_init": 329,
    "fanotify_mark": 330,
    "fchdir": 176,
    "fchmod": 124,
    "fchmodat": 295,
    "fchown": 123,
    "fchownat": 287,
    "fcntl": 92,
    "fdatasync": 253,
    "fgetxattr": 177,
    "finit_module": 342,
    "flistxattr": 180,
    "flock": 131,
    "fork": 2,
    "fremovexattr": 186,
    "fsconfig": 431,
    "fsetxattr": 171,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat": 62,
    "fstat64": 63,
    "fstatat64": 289,
    "fstatfs": 158,
    "fstatfs64": 235,
    "fsync": 95,
    "ftruncate": 130,
    "futex": 142,
    "futex_waitv": 449,
    "futimesat": 288,
    "get_kernel_syms": 223,
    "get_mempolicy": 304,
    "get_robust_list": 301,
    "getcpu": 308,
    "getcwd": 119,
    "getdents": 174,
    "getdents64": 154,
    "getdomainname": 162,
    "getegid": 50,
    "geteuid": 49,
    "getgid": 47,
    "getgroups": 79,
    "getitimer": 86,
    "getpagesize": 64,
    "getpeername": 141,
    "getpgid": 224,
    "getpgrp": 81,
    "getpid": 20,
    "getppid": 197,
    "getpriority": 100,
    "getrandom": 347,
    "getresgid": 111,
    "getresuid": 109,
    "getrlimit": 144,
    "getrusage": 117,
    "getsid": 252,
    "getsockname": 150,
    "getsockopt": 118,
    "gettid": 143,
    "gettimeofday": 116,
    "getuid": 24,
    "getxattr": 172,
    "init_module": 190,
    "inotify_add_watch": 152,
    "inotify_init": 151,
    "inotify_init1": 322,
    "inotify_rm_watch": 156,
    "io_cancel": 271,
    "io_destroy": 269,
    "io_getevents": 272,
    "io_pgetevents": 361,
    "io_setup": 268,
    "io_submit": 270,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 54,
    "ioprio_get": 218,
    "ioprio_set": 196,
    "ipc": 215,
    "kcmp": 341,
    "kern_features": 340,
    "kexec_load": 306,
    "keyctl": 283,
    "kill": 37,
    "landlock_add_rule": 445,
    "landlock_create_ruleset": 444,
    "landlock_restrict_self": 446,
    "lchown": 16,
    "lgetxattr": 173,
    "link": 9,
    "linkat": 292,
    "listen": 354,
    "listxattr": 178,
    "llistxattr": 179,
    "lookup_dcookie": 208,
    "lremovexattr": 182,
    "lseek": 19,
    "lsetxattr": 170,
    "lstat": 40,
    "lstat64": 132,
    "madvise": 75,
    "mbind": 303,
    "membarrier": 351,
    "memfd_create": 348,
    "memory_ordering": 52,
    "migrate_pages": 302,
    "mincore": 78,
    "mkdir": 136,
    "mkdirat": 285,
    "mknod": 14,
    "mknodat": 286,
    "mlock": 237,
    "mlock2": 356,
    "mlockall": 239,
    "mmap": 71,
    "mount": 167,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 307,
    "mprotect": 74,
    "mq_getsetattr": 278,
    "mq_notify": 277,
    "mq_open": 273,
    "mq_timedreceive": 276,
    "mq_timedsend": 275,
    "mq_unlink": 274,
    "mremap": 250,
    "msgctl": 402,
    "msgget": 399,
    "msgrcv": 401,
    "msgsnd": 400,
    "msync": 65,
    "munlock": 238,
    "munlockall": 240,
    "munmap": 73,
    "name_to_handle_at": 332,
    "nanosleep": 249,
    "nfsservctl": 254,
    "nice": 34,
    "oldlstat": 202,
    "open": 5,
    "open_by_handle_at": 333,
    "open_tree": 428,
    "openat": 284,
    "openat2": 437,
    "pause": 29,
    "pciconfig_read": 148,
    "pciconfig_write": 149,
    "perf_event_open": 327,
    "perfctr": 18,
    "personality": 191,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe": 42,
    "pipe2": 321,
    "pivot_root": 146,
    "pkey_alloc": 363,
    "pkey_free": 364,
    "pkey_mprotect": 362,
    "poll": 153,
    "ppoll": 298,
    "prctl": 147,
    "pread64": 67,
    "preadv": 324,
    "preadv2": 358,
    "prlimit64": 331,
    "process_madvise": 440,
    "process_mrelease": 448,
    "process_vm_readv": 338,
    "process_vm_writev": 339,
    "pselect6": 297,
    "ptrace": 26,
    "pwrite64": 68,
    "pwritev": 325,
    "pwritev2": 359,
    "query_module": 184,
    "quotactl": 165,
    "quotactl_fd": 443,
    "read": 3,
    "readahead": 205,
    "readdir": 204,
    "readlink": 58,
    "readlinkat": 294,
    "readv": 120,
    "reboot": 55,
    "recvfrom": 125,
    "recvmmsg": 328,
    "recvmsg": 113,
    "remap_file_pages": 192,
    "removexattr": 181,
    "rename": 128,
    "renameat": 291,
    "renameat2": 345,
    "request_key": 282,
    "restart_syscall": 0,
    "rmdir": 137,
    "rseq": 365,
    "rt_sigaction": 102,
    "rt_sigpending": 104,
    "rt_sigprocmask": 103,
    "rt_sigqueueinfo": 106,
    "rt_sigreturn": 101,
    "rt_sigsuspend": 107,
    "rt_sigtimedwait": 105,
    "rt_tgsigqueueinfo": 326,
    "sched_get_affinity": 161,
    "sched_get_priority_max": 246,
    "sched_get_priority_min": 247,
    "sched_getaffinity": 260,
    "sched_getattr": 344,
    "sched_getparam": 242,
    "sched_getscheduler": 244,
    "sched_rr_get_interval": 248,
    "sched_set_affinity": 160,
    "sched_setaffinity": 261,
    "sched_setattr": 343,
    "sched_setparam": 241,
    "sched_setscheduler": 243,
    "sched_yield": 245,
    "seccomp": 346,
    "select": 93,
    "semctl": 394,
    "semget": 393,
    "semtimedop": 392,
    "sendfile": 39,
    "sendfile64": 140,
    "sendmmsg": 336,
    "sendmsg": 114,
    "sendto": 133,
    "set_mempolicy": 305,
    "set_robust_list": 300,
    "set_tid_address": 166,
    "setdomainname": 163,
    "setfsgid": 229,
    "setfsuid": 228,
    "setgid": 46,
    "setgroups": 80,
    "sethostname": 88,
    "setitimer": 83,
    "setns": 337,
    "setpgid": 185,
    "setpriority": 96,
    "setregid": 127,
    "setresgid": 110,
    "setresuid": 108,
    "setreuid": 126,
    "setrlimit": 145,
    "setsid": 175,
    "setsockopt": 355,
    "settimeofday": 122,
    "setuid": 23,
    "setxattr": 169,
    "sgetmask": 199,
    "shmat": 397,
    "shmctl": 396,
    "shmdt": 398,
    "shmget": 395,
    "shutdown": 134,
    "sigaction": 198,
    "sigaltstack": 28,
    "signal": 48,
    "signalfd": 311,
    "signalfd4": 317,
    "sigpending": 183,
    "sigprocmask": 220,
    "sigreturn": 216,
    "sigsuspend": 201,
    "socket": 97,
    "socketcall": 206,
    "socketpair": 135,
    "splice": 232,
    "ssetmask": 200,
    "stat": 38,
    "stat64": 139,
    "statfs": 157,
    "statfs64": 234,
    "statx": 360,
    "stime": 233,
    "swapoff": 213,
    "swapon": 85,
    "symlink": 57,
    "symlinkat": 293,
    "sync": 36,
    "sync_file_range": 255,
    "syncfs": 335,
    "sysfs": 226,
    "sysinfo": 214,
    "syslog": 207,
    "tee": 280,
    "tgkill": 211,
    "timer_create": 266,
    "timer_delete": 265,
    "timer_getoverrun": 264,
    "timer_gettime": 263,
    "timer_settime": 262,
    "timerfd_create": 312,
    "timerfd_gettime": 316,
    "timerfd_settime": 315,
    "times": 43,
    "tkill": 187,
    "truncate": 129,
    "umask": 60,
    "umount": 159,
    "umount2": 45,
    "uname": 189,
    "unlink": 10,
    "unlinkat": 290,
    "unshare": 299,
    "uselib": 203,
    "userfaultfd": 352,
    "ustat": 168,
    "utime": 30,
    "utimensat": 310,
    "utimes": 138,
    "utrap_install": 164,
    "vfork": 66,
    "vhangup": 76,
    "vmsplice": 25,
    "wait4": 7,
    "waitid": 279,
    "waitpid": 212,
    "write": 4,
    "writev": 121,
}
