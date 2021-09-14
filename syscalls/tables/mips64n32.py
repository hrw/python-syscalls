#!/usr/bin/python3

# Content autogenerated. Do not edit.

syscalls_mips64n32 = {
    "_newselect": 6022,
    "_sysctl": 6152,
    "accept": 6042,
    "accept4": 6297,
    "access": 6020,
    "acct": 6158,
    "add_key": 6243,
    "adjtimex": 6154,
    "alarm": 6037,
    "bind": 6048,
    "bpf": 6319,
    "brk": 6012,
    "cachectl": 6198,
    "cacheflush": 6197,
    "capget": 6123,
    "capset": 6124,
    "chdir": 6078,
    "chmod": 6088,
    "chown": 6090,
    "chroot": 6156,
    "clock_adjtime": 6305,
    "clock_adjtime64": 6405,
    "clock_getres": 6227,
    "clock_getres_time64": 6406,
    "clock_gettime": 6226,
    "clock_gettime64": 6403,
    "clock_nanosleep": 6228,
    "clock_nanosleep_time64": 6407,
    "clock_settime": 6225,
    "clock_settime64": 6404,
    "clone": 6055,
    "clone3": 6435,
    "close": 6003,
    "close_range": 6436,
    "connect": 6041,
    "copy_file_range": 6324,
    "creat": 6083,
    "create_module": 6167,
    "delete_module": 6169,
    "dup": 6031,
    "dup2": 6032,
    "dup3": 6290,
    "epoll_create": 6207,
    "epoll_create1": 6289,
    "epoll_ctl": 6208,
    "epoll_pwait": 6276,
    "epoll_pwait2": 6441,
    "epoll_wait": 6209,
    "eventfd": 6282,
    "eventfd2": 6288,
    "execve": 6057,
    "execveat": 6320,
    "exit": 6058,
    "exit_group": 6205,
    "faccessat": 6263,
    "faccessat2": 6439,
    "fadvise64": 6216,
    "fallocate": 6283,
    "fanotify_init": 6300,
    "fanotify_mark": 6301,
    "fchdir": 6079,
    "fchmod": 6089,
    "fchmodat": 6262,
    "fchown": 6091,
    "fchownat": 6254,
    "fcntl": 6070,
    "fcntl64": 6212,
    "fdatasync": 6073,
    "fgetxattr": 6185,
    "finit_module": 6312,
    "flistxattr": 6188,
    "flock": 6071,
    "fork": 6056,
    "fremovexattr": 6191,
    "fsconfig": 6431,
    "fsetxattr": 6182,
    "fsmount": 6432,
    "fsopen": 6430,
    "fspick": 6433,
    "fstat": 6005,
    "fstatfs": 6135,
    "fstatfs64": 6218,
    "fsync": 6072,
    "ftruncate": 6075,
    "futex": 6194,
    "futex_time64": 6422,
    "futimesat": 6255,
    "get_kernel_syms": 6170,
    "get_mempolicy": 6232,
    "get_robust_list": 6273,
    "getcpu": 6275,
    "getcwd": 6077,
    "getdents": 6076,
    "getdents64": 6299,
    "getegid": 6106,
    "geteuid": 6105,
    "getgid": 6102,
    "getgroups": 6113,
    "getitimer": 6035,
    "getpeername": 6051,
    "getpgid": 6119,
    "getpgrp": 6109,
    "getpid": 6038,
    "getpmsg": 6174,
    "getppid": 6108,
    "getpriority": 6137,
    "getrandom": 6317,
    "getresgid": 6118,
    "getresuid": 6116,
    "getrlimit": 6095,
    "getrusage": 6096,
    "getsid": 6122,
    "getsockname": 6050,
    "getsockopt": 6054,
    "gettid": 6178,
    "gettimeofday": 6094,
    "getuid": 6100,
    "getxattr": 6183,
    "init_module": 6168,
    "inotify_add_watch": 6248,
    "inotify_init": 6247,
    "inotify_init1": 6292,
    "inotify_rm_watch": 6249,
    "io_cancel": 6204,
    "io_destroy": 6201,
    "io_getevents": 6202,
    "io_pgetevents": 6332,
    "io_pgetevents_time64": 6416,
    "io_setup": 6200,
    "io_submit": 6203,
    "io_uring_enter": 6426,
    "io_uring_register": 6427,
    "io_uring_setup": 6425,
    "ioctl": 6015,
    "ioprio_get": 6278,
    "ioprio_set": 6277,
    "kcmp": 6311,
    "kexec_load": 6274,
    "keyctl": 6245,
    "kill": 6060,
    "landlock_add_rule": 6445,
    "landlock_create_ruleset": 6444,
    "landlock_restrict_self": 6446,
    "lchown": 6092,
    "lgetxattr": 6184,
    "link": 6084,
    "linkat": 6259,
    "listen": 6049,
    "listxattr": 6186,
    "llistxattr": 6187,
    "lookup_dcookie": 6206,
    "lremovexattr": 6190,
    "lseek": 6008,
    "lsetxattr": 6181,
    "lstat": 6006,
    "madvise": 6027,
    "mbind": 6231,
    "membarrier": 6322,
    "memfd_create": 6318,
    "migrate_pages": 6250,
    "mincore": 6026,
    "mkdir": 6081,
    "mkdirat": 6252,
    "mknod": 6131,
    "mknodat": 6253,
    "mlock": 6146,
    "mlock2": 6323,
    "mlockall": 6148,
    "mmap": 6009,
    "mount": 6160,
    "mount_setattr": 6442,
    "move_mount": 6429,
    "move_pages": 6271,
    "mprotect": 6010,
    "mq_getsetattr": 6239,
    "mq_notify": 6238,
    "mq_open": 6234,
    "mq_timedreceive": 6237,
    "mq_timedreceive_time64": 6419,
    "mq_timedsend": 6236,
    "mq_timedsend_time64": 6418,
    "mq_unlink": 6235,
    "mremap": 6024,
    "msgctl": 6069,
    "msgget": 6066,
    "msgrcv": 6068,
    "msgsnd": 6067,
    "msync": 6025,
    "munlock": 6147,
    "munlockall": 6149,
    "munmap": 6011,
    "name_to_handle_at": 6303,
    "nanosleep": 6034,
    "newfstatat": 6256,
    "nfsservctl": 6173,
    "open": 6002,
    "open_by_handle_at": 6304,
    "open_tree": 6428,
    "openat": 6251,
    "openat2": 6437,
    "pause": 6033,
    "perf_event_open": 6296,
    "personality": 6132,
    "pidfd_getfd": 6438,
    "pidfd_open": 6434,
    "pidfd_send_signal": 6424,
    "pipe": 6021,
    "pipe2": 6291,
    "pivot_root": 6151,
    "pkey_alloc": 6328,
    "pkey_free": 6329,
    "pkey_mprotect": 6327,
    "poll": 6007,
    "ppoll": 6265,
    "ppoll_time64": 6414,
    "prctl": 6153,
    "pread64": 6016,
    "preadv": 6293,
    "preadv2": 6325,
    "prlimit64": 6302,
    "process_madvise": 6440,
    "process_mrelease": 6448,
    "process_vm_readv": 6309,
    "process_vm_writev": 6310,
    "pselect6": 6264,
    "pselect6_time64": 6413,
    "ptrace": 6099,
    "pwrite64": 6017,
    "pwritev": 6294,
    "pwritev2": 6326,
    "query_module": 6171,
    "quotactl": 6172,
    "quotactl_fd": 6443,
    "read": 6000,
    "readahead": 6179,
    "readlink": 6087,
    "readlinkat": 6261,
    "readv": 6018,
    "reboot": 6164,
    "recvfrom": 6044,
    "recvmmsg": 6298,
    "recvmmsg_time64": 6417,
    "recvmsg": 6046,
    "remap_file_pages": 6210,
    "removexattr": 6189,
    "rename": 6080,
    "renameat": 6258,
    "renameat2": 6315,
    "request_key": 6244,
    "restart_syscall": 6214,
    "rmdir": 6082,
    "rseq": 6331,
    "rt_sigaction": 6013,
    "rt_sigpending": 6125,
    "rt_sigprocmask": 6014,
    "rt_sigqueueinfo": 6127,
    "rt_sigreturn": 6211,
    "rt_sigsuspend": 6128,
    "rt_sigtimedwait": 6126,
    "rt_sigtimedwait_time64": 6421,
    "rt_tgsigqueueinfo": 6295,
    "sched_get_priority_max": 6143,
    "sched_get_priority_min": 6144,
    "sched_getaffinity": 6196,
    "sched_getattr": 6314,
    "sched_getparam": 6140,
    "sched_getscheduler": 6142,
    "sched_rr_get_interval": 6145,
    "sched_rr_get_interval_time64": 6423,
    "sched_setaffinity": 6195,
    "sched_setattr": 6313,
    "sched_setparam": 6139,
    "sched_setscheduler": 6141,
    "sched_yield": 6023,
    "seccomp": 6316,
    "semctl": 6064,
    "semget": 6062,
    "semop": 6063,
    "semtimedop": 6215,
    "semtimedop_time64": 6420,
    "sendfile": 6039,
    "sendfile64": 6219,
    "sendmmsg": 6307,
    "sendmsg": 6045,
    "sendto": 6043,
    "set_mempolicy": 6233,
    "set_robust_list": 6272,
    "set_thread_area": 6246,
    "set_tid_address": 6213,
    "setdomainname": 6166,
    "setfsgid": 6121,
    "setfsuid": 6120,
    "setgid": 6104,
    "setgroups": 6114,
    "sethostname": 6165,
    "setitimer": 6036,
    "setns": 6308,
    "setpgid": 6107,
    "setpriority": 6138,
    "setregid": 6112,
    "setresgid": 6117,
    "setresuid": 6115,
    "setreuid": 6111,
    "setrlimit": 6155,
    "setsid": 6110,
    "setsockopt": 6053,
    "settimeofday": 6159,
    "setuid": 6103,
    "setxattr": 6180,
    "shmat": 6029,
    "shmctl": 6030,
    "shmdt": 6065,
    "shmget": 6028,
    "shutdown": 6047,
    "sigaltstack": 6129,
    "signalfd": 6280,
    "signalfd4": 6287,
    "socket": 6040,
    "socketpair": 6052,
    "splice": 6267,
    "stat": 6004,
    "statfs": 6134,
    "statfs64": 6217,
    "statx": 6330,
    "swapoff": 6163,
    "swapon": 6162,
    "symlink": 6086,
    "symlinkat": 6260,
    "sync": 6157,
    "sync_file_range": 6268,
    "syncfs": 6306,
    "sysfs": 6136,
    "sysinfo": 6097,
    "syslog": 6101,
    "sysmips": 6199,
    "tee": 6269,
    "tgkill": 6229,
    "timer_create": 6220,
    "timer_delete": 6224,
    "timer_getoverrun": 6223,
    "timer_gettime": 6222,
    "timer_gettime64": 6408,
    "timer_settime": 6221,
    "timer_settime64": 6409,
    "timerfd": 6281,
    "timerfd_create": 6284,
    "timerfd_gettime": 6285,
    "timerfd_gettime64": 6410,
    "timerfd_settime": 6286,
    "timerfd_settime64": 6411,
    "times": 6098,
    "tkill": 6192,
    "truncate": 6074,
    "umask": 6093,
    "umount2": 6161,
    "uname": 6061,
    "unlink": 6085,
    "unlinkat": 6257,
    "unshare": 6266,
    "userfaultfd": 6321,
    "ustat": 6133,
    "utime": 6130,
    "utimensat": 6279,
    "utimensat_time64": 6412,
    "utimes": 6230,
    "vhangup": 6150,
    "vmsplice": 6270,
    "wait4": 6059,
    "waitid": 6241,
    "write": 6001,
    "writev": 6019,
}
