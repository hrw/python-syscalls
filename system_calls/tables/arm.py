# Content autogenerated. Do not edit.

syscalls_arm = {
    "_llseek": 140,
    "_newselect": 142,
    "_sysctl": 149,
    "accept": 285,
    "accept4": 366,
    "access": 33,
    "acct": 51,
    "add_key": 309,
    "adjtimex": 124,
    "arm_fadvise64_64": 270,
    "bdflush": 134,
    "bind": 282,
    "bpf": 386,
    "brk": 45,
    "capget": 184,
    "capset": 185,
    "chdir": 12,
    "chmod": 15,
    "chown": 182,
    "chown32": 212,
    "chroot": 61,
    "clock_adjtime": 372,
    "clock_adjtime64": 405,
    "clock_getres": 264,
    "clock_getres_time64": 406,
    "clock_gettime": 263,
    "clock_gettime64": 403,
    "clock_nanosleep": 265,
    "clock_nanosleep_time64": 407,
    "clock_settime": 262,
    "clock_settime64": 404,
    "clone": 120,
    "clone3": 435,
    "close": 6,
    "close_range": 436,
    "connect": 283,
    "copy_file_range": 391,
    "creat": 8,
    "delete_module": 129,
    "dup": 41,
    "dup2": 63,
    "dup3": 358,
    "epoll_create": 250,
    "epoll_create1": 357,
    "epoll_ctl": 251,
    "epoll_pwait": 346,
    "epoll_pwait2": 441,
    "epoll_wait": 252,
    "eventfd": 351,
    "eventfd2": 356,
    "execve": 11,
    "execveat": 387,
    "exit": 1,
    "exit_group": 248,
    "faccessat": 334,
    "faccessat2": 439,
    "fallocate": 352,
    "fanotify_init": 367,
    "fanotify_mark": 368,
    "fchdir": 133,
    "fchmod": 94,
    "fchmodat": 333,
    "fchown": 95,
    "fchown32": 207,
    "fchownat": 325,
    "fcntl": 55,
    "fcntl64": 221,
    "fdatasync": 148,
    "fgetxattr": 231,
    "finit_module": 379,
    "flistxattr": 234,
    "flock": 143,
    "fork": 2,
    "fremovexattr": 237,
    "fsconfig": 431,
    "fsetxattr": 228,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat": 108,
    "fstat64": 197,
    "fstatat64": 327,
    "fstatfs": 100,
    "fstatfs64": 267,
    "fsync": 118,
    "ftruncate": 93,
    "ftruncate64": 194,
    "futex": 240,
    "futex_time64": 422,
    "futimesat": 326,
    "get_mempolicy": 320,
    "get_robust_list": 339,
    "getcpu": 345,
    "getcwd": 183,
    "getdents": 141,
    "getdents64": 217,
    "getegid": 50,
    "getegid32": 202,
    "geteuid": 49,
    "geteuid32": 201,
    "getgid": 47,
    "getgid32": 200,
    "getgroups": 80,
    "getgroups32": 205,
    "getitimer": 105,
    "getpeername": 287,
    "getpgid": 132,
    "getpgrp": 65,
    "getpid": 20,
    "getppid": 64,
    "getpriority": 96,
    "getrandom": 384,
    "getresgid": 171,
    "getresgid32": 211,
    "getresuid": 165,
    "getresuid32": 209,
    "getrusage": 77,
    "getsid": 147,
    "getsockname": 286,
    "getsockopt": 295,
    "gettid": 224,
    "gettimeofday": 78,
    "getuid": 24,
    "getuid32": 199,
    "getxattr": 229,
    "init_module": 128,
    "inotify_add_watch": 317,
    "inotify_init": 316,
    "inotify_init1": 360,
    "inotify_rm_watch": 318,
    "io_cancel": 247,
    "io_destroy": 244,
    "io_getevents": 245,
    "io_pgetevents": 399,
    "io_pgetevents_time64": 416,
    "io_setup": 243,
    "io_submit": 246,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 54,
    "ioprio_get": 315,
    "ioprio_set": 314,
    "kcmp": 378,
    "kexec_file_load": 401,
    "kexec_load": 347,
    "keyctl": 311,
    "kill": 37,
    "landlock_add_rule": 445,
    "landlock_create_ruleset": 444,
    "landlock_restrict_self": 446,
    "lchown": 16,
    "lchown32": 198,
    "lgetxattr": 230,
    "link": 9,
    "linkat": 330,
    "listen": 284,
    "listxattr": 232,
    "llistxattr": 233,
    "lookup_dcookie": 249,
    "lremovexattr": 236,
    "lseek": 19,
    "lsetxattr": 227,
    "lstat": 107,
    "lstat64": 196,
    "madvise": 220,
    "mbind": 319,
    "membarrier": 389,
    "memfd_create": 385,
    "migrate_pages": 400,
    "mincore": 219,
    "mkdir": 39,
    "mkdirat": 323,
    "mknod": 14,
    "mknodat": 324,
    "mlock": 150,
    "mlock2": 390,
    "mlockall": 152,
    "mmap2": 192,
    "mount": 21,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 344,
    "mprotect": 125,
    "mq_getsetattr": 279,
    "mq_notify": 278,
    "mq_open": 274,
    "mq_timedreceive": 277,
    "mq_timedreceive_time64": 419,
    "mq_timedsend": 276,
    "mq_timedsend_time64": 418,
    "mq_unlink": 275,
    "mremap": 163,
    "msgctl": 304,
    "msgget": 303,
    "msgrcv": 302,
    "msgsnd": 301,
    "msync": 144,
    "munlock": 151,
    "munlockall": 153,
    "munmap": 91,
    "name_to_handle_at": 370,
    "nanosleep": 162,
    "nfsservctl": 169,
    "nice": 34,
    "open": 5,
    "open_by_handle_at": 371,
    "open_tree": 428,
    "openat": 322,
    "openat2": 437,
    "pause": 29,
    "pciconfig_iobase": 271,
    "pciconfig_read": 272,
    "pciconfig_write": 273,
    "perf_event_open": 364,
    "personality": 136,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe": 42,
    "pipe2": 359,
    "pivot_root": 218,
    "pkey_alloc": 395,
    "pkey_free": 396,
    "pkey_mprotect": 394,
    "poll": 168,
    "ppoll": 336,
    "ppoll_time64": 414,
    "prctl": 172,
    "pread64": 180,
    "preadv": 361,
    "preadv2": 392,
    "prlimit64": 369,
    "process_madvise": 440,
    "process_mrelease": 448,
    "process_vm_readv": 376,
    "process_vm_writev": 377,
    "pselect6": 335,
    "pselect6_time64": 413,
    "ptrace": 26,
    "pwrite64": 181,
    "pwritev": 362,
    "pwritev2": 393,
    "quotactl": 131,
    "quotactl_fd": 443,
    "read": 3,
    "readahead": 225,
    "readlink": 85,
    "readlinkat": 332,
    "readv": 145,
    "reboot": 88,
    "recv": 291,
    "recvfrom": 292,
    "recvmmsg": 365,
    "recvmmsg_time64": 417,
    "recvmsg": 297,
    "remap_file_pages": 253,
    "removexattr": 235,
    "rename": 38,
    "renameat": 329,
    "renameat2": 382,
    "request_key": 310,
    "restart_syscall": 0,
    "rmdir": 40,
    "rseq": 398,
    "rt_sigaction": 174,
    "rt_sigpending": 176,
    "rt_sigprocmask": 175,
    "rt_sigqueueinfo": 178,
    "rt_sigreturn": 173,
    "rt_sigsuspend": 179,
    "rt_sigtimedwait": 177,
    "rt_sigtimedwait_time64": 421,
    "rt_tgsigqueueinfo": 363,
    "sched_get_priority_max": 159,
    "sched_get_priority_min": 160,
    "sched_getaffinity": 242,
    "sched_getattr": 381,
    "sched_getparam": 155,
    "sched_getscheduler": 157,
    "sched_rr_get_interval": 161,
    "sched_rr_get_interval_time64": 423,
    "sched_setaffinity": 241,
    "sched_setattr": 380,
    "sched_setparam": 154,
    "sched_setscheduler": 156,
    "sched_yield": 158,
    "seccomp": 383,
    "semctl": 300,
    "semget": 299,
    "semop": 298,
    "semtimedop": 312,
    "semtimedop_time64": 420,
    "send": 289,
    "sendfile": 187,
    "sendfile64": 239,
    "sendmmsg": 374,
    "sendmsg": 296,
    "sendto": 290,
    "set_mempolicy": 321,
    "set_robust_list": 338,
    "set_tid_address": 256,
    "setdomainname": 121,
    "setfsgid": 139,
    "setfsgid32": 216,
    "setfsuid": 138,
    "setfsuid32": 215,
    "setgid": 46,
    "setgid32": 214,
    "setgroups": 81,
    "setgroups32": 206,
    "sethostname": 74,
    "setitimer": 104,
    "setns": 375,
    "setpgid": 57,
    "setpriority": 97,
    "setregid": 71,
    "setregid32": 204,
    "setresgid": 170,
    "setresgid32": 210,
    "setresuid": 164,
    "setresuid32": 208,
    "setreuid": 70,
    "setreuid32": 203,
    "setrlimit": 75,
    "setsid": 66,
    "setsockopt": 294,
    "settimeofday": 79,
    "setuid": 23,
    "setuid32": 213,
    "setxattr": 226,
    "shmat": 305,
    "shmctl": 308,
    "shmdt": 306,
    "shmget": 307,
    "shutdown": 293,
    "sigaction": 67,
    "sigaltstack": 186,
    "signalfd": 349,
    "signalfd4": 355,
    "sigpending": 73,
    "sigprocmask": 126,
    "sigreturn": 119,
    "sigsuspend": 72,
    "socket": 281,
    "socketpair": 288,
    "splice": 340,
    "stat": 106,
    "stat64": 195,
    "statfs": 99,
    "statfs64": 266,
    "statx": 397,
    "swapoff": 115,
    "swapon": 87,
    "symlink": 83,
    "symlinkat": 331,
    "sync": 36,
    "sync_file_range2": 341,
    "syncfs": 373,
    "sysfs": 135,
    "sysinfo": 116,
    "syslog": 103,
    "tee": 342,
    "tgkill": 268,
    "timer_create": 257,
    "timer_delete": 261,
    "timer_getoverrun": 260,
    "timer_gettime": 259,
    "timer_gettime64": 408,
    "timer_settime": 258,
    "timer_settime64": 409,
    "timerfd_create": 350,
    "timerfd_gettime": 354,
    "timerfd_gettime64": 410,
    "timerfd_settime": 353,
    "timerfd_settime64": 411,
    "times": 43,
    "tkill": 238,
    "truncate": 92,
    "truncate64": 193,
    "ugetrlimit": 191,
    "umask": 60,
    "umount2": 52,
    "uname": 122,
    "unlink": 10,
    "unlinkat": 328,
    "unshare": 337,
    "uselib": 86,
    "userfaultfd": 388,
    "ustat": 62,
    "utimensat": 348,
    "utimensat_time64": 412,
    "utimes": 269,
    "vfork": 190,
    "vhangup": 111,
    "vmsplice": 343,
    "wait4": 114,
    "waitid": 280,
    "write": 4,
    "writev": 146,
}
