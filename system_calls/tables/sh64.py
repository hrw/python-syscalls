# Content autogenerated. Do not edit.

syscalls_sh64 = {
    "_llseek": 140,
    "_newselect": 142,
    "_sysctl": 149,
    "accept": 224,
    "accept4": 366,
    "access": 33,
    "acct": 51,
    "add_key": 313,
    "adjtimex": 124,
    "alarm": 27,
    "bdflush": 134,
    "bind": 221,
    "bpf": 386,
    "brk": 45,
    "cacheflush": 123,
    "capget": 184,
    "capset": 185,
    "chdir": 12,
    "chmod": 15,
    "chown": 182,
    "chown32": 212,
    "chroot": 61,
    "clock_adjtime": 372,
    "clock_getres": 294,
    "clock_gettime": 293,
    "clock_nanosleep": 295,
    "clock_settime": 292,
    "clone": 120,
    "close": 6,
    "connect": 222,
    "copy_file_range": 391,
    "creat": 8,
    "delete_module": 129,
    "dup": 41,
    "dup2": 63,
    "dup3": 358,
    "epoll_create": 282,
    "epoll_create1": 357,
    "epoll_ctl": 283,
    "epoll_pwait": 347,
    "epoll_wait": 284,
    "eventfd": 351,
    "eventfd2": 356,
    "execve": 11,
    "execveat": 387,
    "exit": 1,
    "exit_group": 280,
    "faccessat": 335,
    "fadvise64": 278,
    "fadvise64_64": 300,
    "fallocate": 352,
    "fanotify_init": 367,
    "fanotify_mark": 368,
    "fchdir": 133,
    "fchmod": 94,
    "fchmodat": 334,
    "fchown": 95,
    "fchown32": 207,
    "fchownat": 326,
    "fcntl": 55,
    "fcntl64": 249,
    "fdatasync": 148,
    "fgetxattr": 259,
    "finit_module": 379,
    "flistxattr": 262,
    "flock": 143,
    "fork": 2,
    "fremovexattr": 265,
    "fsetxattr": 256,
    "fstat": 108,
    "fstat64": 197,
    "fstatat64": 328,
    "fstatfs": 100,
    "fstatfs64": 297,
    "fsync": 118,
    "ftruncate": 93,
    "ftruncate64": 194,
    "futex": 268,
    "futimesat": 327,
    "get_robust_list": 340,
    "getcpu": 346,
    "getcwd": 183,
    "getdents": 141,
    "getdents64": 248,
    "getegid": 50,
    "getegid32": 202,
    "geteuid": 49,
    "geteuid32": 201,
    "getgid": 47,
    "getgid32": 200,
    "getgroups": 80,
    "getgroups32": 205,
    "getitimer": 105,
    "getpeername": 226,
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
    "getrlimit": 76,
    "getrusage": 77,
    "getsid": 147,
    "getsockname": 225,
    "getsockopt": 234,
    "gettid": 252,
    "gettimeofday": 78,
    "getuid": 24,
    "getuid32": 199,
    "getxattr": 257,
    "init_module": 128,
    "inotify_add_watch": 319,
    "inotify_init": 318,
    "inotify_init1": 360,
    "inotify_rm_watch": 320,
    "io_cancel": 277,
    "io_destroy": 274,
    "io_getevents": 275,
    "io_setup": 273,
    "io_submit": 276,
    "ioctl": 54,
    "ioprio_get": 317,
    "ioprio_set": 316,
    "ipc": 117,
    "kcmp": 378,
    "keyctl": 315,
    "kill": 37,
    "lchown": 16,
    "lchown32": 198,
    "lgetxattr": 258,
    "link": 9,
    "linkat": 331,
    "listen": 223,
    "listxattr": 260,
    "llistxattr": 261,
    "lookup_dcookie": 281,
    "lremovexattr": 264,
    "lseek": 19,
    "lsetxattr": 255,
    "lstat": 107,
    "lstat64": 196,
    "madvise": 219,
    "membarrier": 389,
    "memfd_create": 385,
    "migrate_pages": 322,
    "mincore": 218,
    "mkdir": 39,
    "mkdirat": 324,
    "mknod": 14,
    "mknodat": 325,
    "mlock": 150,
    "mlock2": 390,
    "mlockall": 152,
    "mmap": 90,
    "mmap2": 192,
    "mount": 21,
    "move_pages": 345,
    "mprotect": 125,
    "mq_getsetattr": 310,
    "mq_notify": 309,
    "mq_open": 305,
    "mq_timedreceive": 308,
    "mq_timedsend": 307,
    "mq_unlink": 306,
    "mremap": 163,
    "msgctl": 243,
    "msgget": 242,
    "msgrcv": 241,
    "msgsnd": 240,
    "msync": 144,
    "munlock": 151,
    "munlockall": 153,
    "munmap": 91,
    "name_to_handle_at": 370,
    "nanosleep": 162,
    "nfsservctl": 169,
    "nice": 34,
    "oldfstat": 28,
    "oldlstat": 84,
    "oldstat": 18,
    "olduname": 109,
    "open": 5,
    "open_by_handle_at": 371,
    "openat": 323,
    "pause": 29,
    "perf_event_open": 364,
    "personality": 136,
    "pipe": 42,
    "pipe2": 359,
    "pivot_root": 217,
    "poll": 168,
    "ppoll": 337,
    "prctl": 172,
    "pread64": 180,
    "preadv": 361,
    "preadv2": 392,
    "prlimit64": 369,
    "process_vm_readv": 376,
    "process_vm_writev": 377,
    "pselect6": 336,
    "ptrace": 26,
    "pwrite64": 181,
    "pwritev": 362,
    "pwritev2": 393,
    "quotactl": 131,
    "read": 3,
    "readahead": 253,
    "readdir": 89,
    "readlink": 85,
    "readlinkat": 333,
    "readv": 145,
    "reboot": 88,
    "recv": 230,
    "recvfrom": 231,
    "recvmmsg": 365,
    "recvmsg": 236,
    "remap_file_pages": 285,
    "removexattr": 263,
    "rename": 38,
    "renameat": 330,
    "renameat2": 382,
    "request_key": 314,
    "restart_syscall": 0,
    "rmdir": 40,
    "rt_sigaction": 174,
    "rt_sigpending": 176,
    "rt_sigprocmask": 175,
    "rt_sigqueueinfo": 178,
    "rt_sigreturn": 173,
    "rt_sigsuspend": 179,
    "rt_sigtimedwait": 177,
    "rt_tgsigqueueinfo": 363,
    "sched_get_priority_max": 159,
    "sched_get_priority_min": 160,
    "sched_getaffinity": 270,
    "sched_getattr": 380,
    "sched_getparam": 155,
    "sched_getscheduler": 157,
    "sched_rr_get_interval": 161,
    "sched_setaffinity": 269,
    "sched_setattr": 381,
    "sched_setparam": 154,
    "sched_setscheduler": 156,
    "sched_yield": 158,
    "seccomp": 383,
    "semctl": 239,
    "semget": 238,
    "semop": 237,
    "send": 228,
    "sendfile": 187,
    "sendfile64": 267,
    "sendmmsg": 374,
    "sendmsg": 235,
    "sendto": 229,
    "set_robust_list": 339,
    "set_tid_address": 286,
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
    "setsockopt": 233,
    "settimeofday": 79,
    "setuid": 23,
    "setuid32": 213,
    "setxattr": 254,
    "sgetmask": 68,
    "shmat": 244,
    "shmctl": 247,
    "shmdt": 245,
    "shmget": 246,
    "shutdown": 232,
    "sigaction": 67,
    "sigaltstack": 186,
    "signal": 48,
    "signalfd": 349,
    "signalfd4": 355,
    "sigpending": 73,
    "sigprocmask": 126,
    "sigreturn": 119,
    "sigsuspend": 72,
    "socket": 220,
    "socketcall": 102,
    "socketpair": 227,
    "splice": 341,
    "ssetmask": 69,
    "stat": 106,
    "stat64": 195,
    "statfs": 99,
    "statfs64": 296,
    "stime": 25,
    "swapoff": 115,
    "swapon": 87,
    "symlink": 83,
    "symlinkat": 332,
    "sync": 36,
    "sync_file_range": 342,
    "syncfs": 373,
    "sysfs": 135,
    "sysinfo": 116,
    "syslog": 103,
    "tee": 343,
    "tgkill": 298,
    "time": 13,
    "timer_create": 287,
    "timer_delete": 291,
    "timer_getoverrun": 290,
    "timer_gettime": 289,
    "timer_settime": 288,
    "timerfd_create": 350,
    "timerfd_gettime": 354,
    "timerfd_settime": 353,
    "times": 43,
    "tkill": 266,
    "truncate": 92,
    "truncate64": 193,
    "ugetrlimit": 191,
    "umask": 60,
    "umount": 22,
    "umount2": 52,
    "uname": 122,
    "unlink": 10,
    "unlinkat": 329,
    "unshare": 338,
    "uselib": 86,
    "userfaultfd": 388,
    "ustat": 62,
    "utime": 30,
    "utimensat": 348,
    "utimes": 299,
    "vfork": 190,
    "vhangup": 111,
    "vmsplice": 344,
    "wait4": 114,
    "waitid": 312,
    "waitpid": 7,
    "write": 4,
    "writev": 146,
}
