# Content autogenerated. Do not edit.

syscalls_m68k = {
    "_llseek": 140,
    "_newselect": 142,
    "_sysctl": 149,
    "accept4": 361,
    "access": 33,
    "acct": 51,
    "add_key": 279,
    "adjtimex": 124,
    "alarm": 27,
    "atomic_barrier": 336,
    "atomic_cmpxchg_32": 335,
    "bdflush": 134,
    "bind": 358,
    "bpf": 354,
    "brk": 45,
    "cacheflush": 123,
    "capget": 184,
    "capset": 185,
    "chdir": 12,
    "chmod": 15,
    "chown": 16,
    "chown32": 198,
    "chroot": 61,
    "clock_adjtime": 342,
    "clock_adjtime64": 405,
    "clock_getres": 261,
    "clock_getres_time64": 406,
    "clock_gettime": 260,
    "clock_gettime64": 403,
    "clock_nanosleep": 262,
    "clock_nanosleep_time64": 407,
    "clock_settime": 259,
    "clock_settime64": 404,
    "clone": 120,
    "clone3": 435,
    "close": 6,
    "close_range": 436,
    "connect": 359,
    "copy_file_range": 376,
    "creat": 8,
    "create_module": 127,
    "delete_module": 129,
    "dup": 41,
    "dup2": 63,
    "dup3": 326,
    "epoll_create": 249,
    "epoll_create1": 325,
    "epoll_ctl": 250,
    "epoll_pwait": 315,
    "epoll_pwait2": 441,
    "epoll_wait": 251,
    "eventfd": 319,
    "eventfd2": 324,
    "execve": 11,
    "execveat": 355,
    "exit": 1,
    "exit_group": 247,
    "faccessat": 300,
    "faccessat2": 439,
    "fadvise64": 246,
    "fadvise64_64": 267,
    "fallocate": 320,
    "fanotify_init": 337,
    "fanotify_mark": 338,
    "fchdir": 133,
    "fchmod": 94,
    "fchmodat": 299,
    "fchown": 95,
    "fchown32": 207,
    "fchownat": 291,
    "fcntl": 55,
    "fcntl64": 239,
    "fdatasync": 148,
    "fgetxattr": 228,
    "finit_module": 348,
    "flistxattr": 231,
    "flock": 143,
    "fork": 2,
    "fremovexattr": 234,
    "fsconfig": 431,
    "fsetxattr": 225,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat": 108,
    "fstat64": 197,
    "fstatat64": 293,
    "fstatfs": 100,
    "fstatfs64": 264,
    "fsync": 118,
    "ftruncate": 93,
    "ftruncate64": 194,
    "futex": 235,
    "futex_time64": 422,
    "futex_waitv": 449,
    "futimesat": 292,
    "get_kernel_syms": 130,
    "get_mempolicy": 269,
    "get_robust_list": 305,
    "get_thread_area": 333,
    "getcpu": 314,
    "getcwd": 183,
    "getdents": 141,
    "getdents64": 220,
    "getegid": 50,
    "getegid32": 202,
    "geteuid": 49,
    "geteuid32": 201,
    "getgid": 47,
    "getgid32": 200,
    "getgroups": 80,
    "getgroups32": 205,
    "getitimer": 105,
    "getpagesize": 166,
    "getpeername": 365,
    "getpgid": 132,
    "getpgrp": 65,
    "getpid": 20,
    "getpmsg": 188,
    "getppid": 64,
    "getpriority": 96,
    "getrandom": 352,
    "getresgid": 171,
    "getresgid32": 211,
    "getresuid": 165,
    "getresuid32": 209,
    "getrlimit": 76,
    "getrusage": 77,
    "getsid": 147,
    "getsockname": 364,
    "getsockopt": 362,
    "gettid": 221,
    "gettimeofday": 78,
    "getuid": 24,
    "getuid32": 199,
    "getxattr": 226,
    "init_module": 128,
    "inotify_add_watch": 285,
    "inotify_init": 284,
    "inotify_init1": 328,
    "inotify_rm_watch": 286,
    "io_cancel": 245,
    "io_destroy": 242,
    "io_getevents": 243,
    "io_pgetevents_time64": 416,
    "io_setup": 241,
    "io_submit": 244,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 54,
    "ioprio_get": 283,
    "ioprio_set": 282,
    "ipc": 117,
    "kcmp": 347,
    "kexec_load": 313,
    "keyctl": 281,
    "kill": 37,
    "landlock_add_rule": 445,
    "landlock_create_ruleset": 444,
    "landlock_restrict_self": 446,
    "lchown": 182,
    "lchown32": 212,
    "lgetxattr": 227,
    "link": 9,
    "linkat": 296,
    "listen": 360,
    "listxattr": 229,
    "llistxattr": 230,
    "lookup_dcookie": 248,
    "lremovexattr": 233,
    "lseek": 19,
    "lsetxattr": 224,
    "lstat": 107,
    "lstat64": 196,
    "madvise": 238,
    "mbind": 268,
    "membarrier": 374,
    "memfd_create": 353,
    "migrate_pages": 287,
    "mincore": 237,
    "mkdir": 39,
    "mkdirat": 289,
    "mknod": 14,
    "mknodat": 290,
    "mlock": 150,
    "mlock2": 375,
    "mlockall": 152,
    "mmap": 90,
    "mmap2": 192,
    "mount": 21,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 310,
    "mprotect": 125,
    "mq_getsetattr": 276,
    "mq_notify": 275,
    "mq_open": 271,
    "mq_timedreceive": 274,
    "mq_timedreceive_time64": 419,
    "mq_timedsend": 273,
    "mq_timedsend_time64": 418,
    "mq_unlink": 272,
    "mremap": 163,
    "msgctl": 402,
    "msgget": 399,
    "msgrcv": 401,
    "msgsnd": 400,
    "msync": 144,
    "munlock": 151,
    "munlockall": 153,
    "munmap": 91,
    "name_to_handle_at": 340,
    "nanosleep": 162,
    "nfsservctl": 169,
    "nice": 34,
    "oldfstat": 28,
    "oldlstat": 84,
    "oldstat": 18,
    "open": 5,
    "open_by_handle_at": 341,
    "open_tree": 428,
    "openat": 288,
    "openat2": 437,
    "pause": 29,
    "perf_event_open": 332,
    "personality": 136,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe": 42,
    "pipe2": 327,
    "pivot_root": 217,
    "pkey_alloc": 382,
    "pkey_free": 383,
    "pkey_mprotect": 381,
    "poll": 168,
    "ppoll": 302,
    "ppoll_time64": 414,
    "prctl": 172,
    "pread64": 180,
    "preadv": 329,
    "preadv2": 377,
    "prlimit64": 339,
    "process_madvise": 440,
    "process_mrelease": 448,
    "process_vm_readv": 345,
    "process_vm_writev": 346,
    "pselect6": 301,
    "pselect6_time64": 413,
    "ptrace": 26,
    "pwrite64": 181,
    "pwritev": 330,
    "pwritev2": 378,
    "query_module": 167,
    "quotactl": 131,
    "quotactl_fd": 443,
    "read": 3,
    "readahead": 240,
    "readdir": 89,
    "readlink": 85,
    "readlinkat": 298,
    "readv": 145,
    "reboot": 88,
    "recvfrom": 368,
    "recvmmsg": 371,
    "recvmmsg_time64": 417,
    "recvmsg": 369,
    "remap_file_pages": 252,
    "removexattr": 232,
    "rename": 38,
    "renameat": 295,
    "renameat2": 351,
    "request_key": 280,
    "restart_syscall": 0,
    "rmdir": 40,
    "rseq": 384,
    "rt_sigaction": 174,
    "rt_sigpending": 176,
    "rt_sigprocmask": 175,
    "rt_sigqueueinfo": 178,
    "rt_sigreturn": 173,
    "rt_sigsuspend": 179,
    "rt_sigtimedwait": 177,
    "rt_sigtimedwait_time64": 421,
    "rt_tgsigqueueinfo": 331,
    "sched_get_priority_max": 159,
    "sched_get_priority_min": 160,
    "sched_getaffinity": 312,
    "sched_getattr": 350,
    "sched_getparam": 155,
    "sched_getscheduler": 157,
    "sched_rr_get_interval": 161,
    "sched_rr_get_interval_time64": 423,
    "sched_setaffinity": 311,
    "sched_setattr": 349,
    "sched_setparam": 154,
    "sched_setscheduler": 156,
    "sched_yield": 158,
    "seccomp": 380,
    "select": 82,
    "semctl": 394,
    "semget": 393,
    "semtimedop_time64": 420,
    "sendfile": 187,
    "sendfile64": 236,
    "sendmmsg": 372,
    "sendmsg": 367,
    "sendto": 366,
    "set_mempolicy": 270,
    "set_robust_list": 304,
    "set_thread_area": 334,
    "set_tid_address": 253,
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
    "setns": 344,
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
    "setsockopt": 363,
    "settimeofday": 79,
    "setuid": 23,
    "setuid32": 213,
    "setxattr": 223,
    "sgetmask": 68,
    "shmat": 397,
    "shmctl": 396,
    "shmdt": 398,
    "shmget": 395,
    "shutdown": 370,
    "sigaction": 67,
    "sigaltstack": 186,
    "signal": 48,
    "signalfd": 317,
    "signalfd4": 323,
    "sigpending": 73,
    "sigprocmask": 126,
    "sigreturn": 119,
    "sigsuspend": 72,
    "socket": 356,
    "socketcall": 102,
    "socketpair": 357,
    "splice": 306,
    "ssetmask": 69,
    "stat": 106,
    "stat64": 195,
    "statfs": 99,
    "statfs64": 263,
    "statx": 379,
    "stime": 25,
    "swapoff": 115,
    "swapon": 87,
    "symlink": 83,
    "symlinkat": 297,
    "sync": 36,
    "sync_file_range": 307,
    "syncfs": 343,
    "sysfs": 135,
    "sysinfo": 116,
    "syslog": 103,
    "tee": 308,
    "tgkill": 265,
    "time": 13,
    "timer_create": 254,
    "timer_delete": 258,
    "timer_getoverrun": 257,
    "timer_gettime": 256,
    "timer_gettime64": 408,
    "timer_settime": 255,
    "timer_settime64": 409,
    "timerfd_create": 318,
    "timerfd_gettime": 322,
    "timerfd_gettime64": 410,
    "timerfd_settime": 321,
    "timerfd_settime64": 411,
    "times": 43,
    "tkill": 222,
    "truncate": 92,
    "truncate64": 193,
    "ugetrlimit": 191,
    "umask": 60,
    "umount": 22,
    "umount2": 52,
    "uname": 122,
    "unlink": 10,
    "unlinkat": 294,
    "unshare": 303,
    "uselib": 86,
    "userfaultfd": 373,
    "ustat": 62,
    "utime": 30,
    "utimensat": 316,
    "utimensat_time64": 412,
    "utimes": 266,
    "vfork": 190,
    "vhangup": 111,
    "vmsplice": 309,
    "wait4": 114,
    "waitid": 277,
    "waitpid": 7,
    "write": 4,
    "writev": 146,
}
