# Content autogenerated. Do not edit.

syscalls_parisc = {
    "_llseek": 140,
    "_newselect": 142,
    "_sysctl": 149,
    "accept": 35,
    "accept4": 320,
    "access": 33,
    "acct": 51,
    "add_key": 264,
    "adjtimex": 124,
    "alarm": 27,
    "bdflush": 134,
    "bind": 22,
    "bpf": 341,
    "brk": 45,
    "capget": 106,
    "capset": 107,
    "chdir": 12,
    "chmod": 15,
    "chown": 180,
    "chroot": 61,
    "clock_adjtime": 324,
    "clock_adjtime64": 405,
    "clock_getres": 257,
    "clock_getres_time64": 406,
    "clock_gettime": 256,
    "clock_gettime64": 403,
    "clock_nanosleep": 258,
    "clock_nanosleep_time64": 407,
    "clock_settime": 255,
    "clock_settime64": 404,
    "clone": 120,
    "clone3": 435,
    "close": 6,
    "close_range": 436,
    "connect": 31,
    "copy_file_range": 346,
    "creat": 8,
    "delete_module": 129,
    "dup": 41,
    "dup2": 63,
    "dup3": 312,
    "epoll_create": 224,
    "epoll_create1": 311,
    "epoll_ctl": 225,
    "epoll_pwait": 297,
    "epoll_pwait2": 441,
    "epoll_wait": 226,
    "eventfd": 304,
    "eventfd2": 310,
    "execve": 11,
    "execveat": 342,
    "exit": 1,
    "exit_group": 222,
    "faccessat": 287,
    "faccessat2": 439,
    "fadvise64_64": 236,
    "fallocate": 305,
    "fanotify_init": 322,
    "fanotify_mark": 323,
    "fchdir": 133,
    "fchmod": 94,
    "fchmodat": 286,
    "fchown": 95,
    "fchownat": 278,
    "fcntl": 55,
    "fcntl64": 202,
    "fdatasync": 148,
    "fgetxattr": 243,
    "finit_module": 333,
    "flistxattr": 246,
    "flock": 143,
    "fork": 2,
    "fremovexattr": 249,
    "fsconfig": 431,
    "fsetxattr": 240,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat": 28,
    "fstat64": 112,
    "fstatat64": 280,
    "fstatfs": 100,
    "fstatfs64": 299,
    "fsync": 118,
    "ftruncate": 93,
    "ftruncate64": 200,
    "futex": 210,
    "futex_time64": 422,
    "futex_waitv": 449,
    "futimesat": 279,
    "get_mempolicy": 261,
    "get_robust_list": 290,
    "getcpu": 296,
    "getcwd": 110,
    "getdents": 141,
    "getdents64": 201,
    "getegid": 50,
    "geteuid": 49,
    "getgid": 47,
    "getgroups": 80,
    "getitimer": 105,
    "getpeername": 53,
    "getpgid": 132,
    "getpgrp": 65,
    "getpid": 20,
    "getppid": 64,
    "getpriority": 96,
    "getrandom": 339,
    "getresgid": 171,
    "getresuid": 165,
    "getrlimit": 76,
    "getrusage": 77,
    "getsid": 147,
    "getsockname": 44,
    "getsockopt": 182,
    "gettid": 206,
    "gettimeofday": 78,
    "getuid": 24,
    "getxattr": 241,
    "init_module": 128,
    "inotify_add_watch": 270,
    "inotify_init": 269,
    "inotify_init1": 314,
    "inotify_rm_watch": 271,
    "io_cancel": 219,
    "io_destroy": 216,
    "io_getevents": 217,
    "io_pgetevents": 350,
    "io_pgetevents_time64": 416,
    "io_setup": 215,
    "io_submit": 218,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 54,
    "ioprio_get": 268,
    "ioprio_set": 267,
    "kcmp": 332,
    "kexec_file_load": 355,
    "kexec_load": 300,
    "keyctl": 266,
    "kill": 37,
    "landlock_add_rule": 445,
    "landlock_create_ruleset": 444,
    "landlock_restrict_self": 446,
    "lchown": 16,
    "lgetxattr": 242,
    "link": 9,
    "linkat": 283,
    "listen": 32,
    "listxattr": 244,
    "llistxattr": 245,
    "lookup_dcookie": 223,
    "lremovexattr": 248,
    "lseek": 19,
    "lsetxattr": 239,
    "lstat": 84,
    "lstat64": 198,
    "madvise": 119,
    "mbind": 260,
    "membarrier": 343,
    "memfd_create": 340,
    "migrate_pages": 272,
    "mincore": 72,
    "mkdir": 39,
    "mkdirat": 276,
    "mknod": 14,
    "mknodat": 277,
    "mlock": 150,
    "mlock2": 345,
    "mlockall": 152,
    "mmap": 90,
    "mmap2": 89,
    "mount": 21,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 295,
    "mprotect": 125,
    "mq_getsetattr": 234,
    "mq_notify": 233,
    "mq_open": 229,
    "mq_timedreceive": 232,
    "mq_timedreceive_time64": 419,
    "mq_timedsend": 231,
    "mq_timedsend_time64": 418,
    "mq_unlink": 230,
    "mremap": 163,
    "msgctl": 191,
    "msgget": 190,
    "msgrcv": 189,
    "msgsnd": 188,
    "msync": 144,
    "munlock": 151,
    "munlockall": 153,
    "munmap": 91,
    "name_to_handle_at": 325,
    "nanosleep": 162,
    "nice": 34,
    "open": 5,
    "open_by_handle_at": 326,
    "open_tree": 428,
    "openat": 275,
    "openat2": 437,
    "pause": 29,
    "perf_event_open": 318,
    "personality": 136,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe": 42,
    "pipe2": 313,
    "pivot_root": 67,
    "pkey_alloc": 352,
    "pkey_free": 353,
    "pkey_mprotect": 351,
    "poll": 168,
    "ppoll": 274,
    "ppoll_time64": 414,
    "prctl": 172,
    "pread64": 108,
    "preadv": 315,
    "preadv2": 347,
    "prlimit64": 321,
    "process_madvise": 440,
    "process_mrelease": 448,
    "process_vm_readv": 330,
    "process_vm_writev": 331,
    "pselect6": 273,
    "pselect6_time64": 413,
    "ptrace": 26,
    "pwrite64": 109,
    "pwritev": 316,
    "pwritev2": 348,
    "quotactl": 131,
    "quotactl_fd": 443,
    "read": 3,
    "readahead": 207,
    "readlink": 85,
    "readlinkat": 285,
    "readv": 145,
    "reboot": 88,
    "recv": 98,
    "recvfrom": 123,
    "recvmmsg": 319,
    "recvmmsg_time64": 417,
    "recvmsg": 184,
    "remap_file_pages": 227,
    "removexattr": 247,
    "rename": 38,
    "renameat": 282,
    "renameat2": 337,
    "request_key": 265,
    "restart_syscall": 0,
    "rmdir": 40,
    "rseq": 354,
    "rt_sigaction": 174,
    "rt_sigpending": 176,
    "rt_sigprocmask": 175,
    "rt_sigqueueinfo": 178,
    "rt_sigreturn": 173,
    "rt_sigsuspend": 179,
    "rt_sigtimedwait": 177,
    "rt_sigtimedwait_time64": 421,
    "rt_tgsigqueueinfo": 317,
    "sched_get_priority_max": 159,
    "sched_get_priority_min": 160,
    "sched_getaffinity": 212,
    "sched_getattr": 335,
    "sched_getparam": 155,
    "sched_getscheduler": 157,
    "sched_rr_get_interval": 161,
    "sched_rr_get_interval_time64": 423,
    "sched_setaffinity": 211,
    "sched_setattr": 334,
    "sched_setparam": 154,
    "sched_setscheduler": 156,
    "sched_yield": 158,
    "seccomp": 338,
    "semctl": 187,
    "semget": 186,
    "semop": 185,
    "semtimedop": 228,
    "semtimedop_time64": 420,
    "send": 58,
    "sendfile": 122,
    "sendfile64": 209,
    "sendmmsg": 329,
    "sendmsg": 183,
    "sendto": 82,
    "set_mempolicy": 262,
    "set_robust_list": 289,
    "set_tid_address": 237,
    "setdomainname": 121,
    "setfsgid": 139,
    "setfsuid": 138,
    "setgid": 46,
    "setgroups": 81,
    "sethostname": 74,
    "setitimer": 104,
    "setns": 328,
    "setpgid": 57,
    "setpriority": 97,
    "setregid": 71,
    "setresgid": 170,
    "setresuid": 164,
    "setreuid": 70,
    "setrlimit": 75,
    "setsid": 66,
    "setsockopt": 181,
    "settimeofday": 79,
    "setuid": 23,
    "setxattr": 238,
    "sgetmask": 68,
    "shmat": 192,
    "shmctl": 195,
    "shmdt": 193,
    "shmget": 194,
    "shutdown": 117,
    "sigaltstack": 166,
    "signal": 48,
    "signalfd": 302,
    "signalfd4": 309,
    "sigpending": 73,
    "sigprocmask": 126,
    "socket": 17,
    "socketpair": 56,
    "splice": 291,
    "ssetmask": 69,
    "stat": 18,
    "stat64": 101,
    "statfs": 99,
    "statfs64": 298,
    "statx": 349,
    "stime": 25,
    "swapoff": 115,
    "swapon": 87,
    "symlink": 83,
    "symlinkat": 284,
    "sync": 36,
    "sync_file_range": 292,
    "syncfs": 327,
    "sysfs": 135,
    "sysinfo": 116,
    "syslog": 103,
    "tee": 293,
    "tgkill": 259,
    "time": 13,
    "timer_create": 250,
    "timer_delete": 254,
    "timer_getoverrun": 253,
    "timer_gettime": 252,
    "timer_gettime64": 408,
    "timer_settime": 251,
    "timer_settime64": 409,
    "timerfd_create": 306,
    "timerfd_gettime": 308,
    "timerfd_gettime64": 410,
    "timerfd_settime": 307,
    "timerfd_settime64": 411,
    "times": 43,
    "tkill": 208,
    "truncate": 92,
    "truncate64": 199,
    "umask": 60,
    "umount2": 52,
    "uname": 59,
    "unlink": 10,
    "unlinkat": 281,
    "unshare": 288,
    "uselib": 86,
    "userfaultfd": 344,
    "ustat": 62,
    "utime": 30,
    "utimensat": 301,
    "utimensat_time64": 412,
    "utimes": 336,
    "vfork": 113,
    "vhangup": 111,
    "vmsplice": 294,
    "wait4": 114,
    "waitid": 235,
    "waitpid": 7,
    "write": 4,
    "writev": 146,
}
