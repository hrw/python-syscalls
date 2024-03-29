# Content autogenerated. Do not edit.

syscalls_ia64 = {
    "_sysctl": 1150,
    "accept": 1194,
    "accept4": 1334,
    "access": 1049,
    "acct": 1064,
    "add_key": 1271,
    "adjtimex": 1131,
    "bdflush": 1138,
    "bind": 1191,
    "bpf": 1341,
    "brk": 1060,
    "cachestat": 1475,
    "capget": 1185,
    "capset": 1186,
    "chdir": 1034,
    "chmod": 1038,
    "chown": 1039,
    "chroot": 1068,
    "clock_adjtime": 1328,
    "clock_getres": 1255,
    "clock_gettime": 1254,
    "clock_nanosleep": 1256,
    "clock_settime": 1253,
    "clone": 1128,
    "clone2": 1213,
    "close": 1029,
    "close_range": 1460,
    "connect": 1192,
    "copy_file_range": 1347,
    "creat": 1030,
    "delete_module": 1134,
    "dup": 1057,
    "dup2": 1070,
    "dup3": 1316,
    "epoll_create": 1243,
    "epoll_create1": 1315,
    "epoll_ctl": 1244,
    "epoll_pwait": 1305,
    "epoll_pwait2": 1465,
    "epoll_wait": 1245,
    "eventfd": 1309,
    "eventfd2": 1314,
    "execve": 1033,
    "execveat": 1342,
    "exit": 1025,
    "exit_group": 1236,
    "faccessat": 1293,
    "faccessat2": 1463,
    "fadvise64": 1234,
    "fallocate": 1303,
    "fanotify_init": 1323,
    "fanotify_mark": 1324,
    "fchdir": 1035,
    "fchmod": 1099,
    "fchmodat": 1292,
    "fchmodat2": 1476,
    "fchown": 1100,
    "fchownat": 1284,
    "fcntl": 1066,
    "fdatasync": 1052,
    "fgetxattr": 1222,
    "finit_module": 1335,
    "flistxattr": 1225,
    "flock": 1145,
    "fremovexattr": 1228,
    "fsconfig": 1455,
    "fsetxattr": 1219,
    "fsmount": 1456,
    "fsopen": 1454,
    "fspick": 1457,
    "fstat": 1212,
    "fstatfs": 1104,
    "fstatfs64": 1257,
    "fsync": 1051,
    "ftruncate": 1098,
    "futex": 1230,
    "futex_waitv": 1473,
    "futimesat": 1285,
    "get_mempolicy": 1260,
    "get_robust_list": 1299,
    "getcpu": 1304,
    "getcwd": 1184,
    "getdents": 1144,
    "getdents64": 1214,
    "getegid": 1063,
    "geteuid": 1047,
    "getgid": 1062,
    "getgroups": 1077,
    "getitimer": 1119,
    "getpeername": 1196,
    "getpgid": 1079,
    "getpid": 1041,
    "getpmsg": 1188,
    "getppid": 1042,
    "getpriority": 1101,
    "getrandom": 1339,
    "getresgid": 1075,
    "getresuid": 1073,
    "getrlimit": 1085,
    "getrusage": 1086,
    "getsid": 1082,
    "getsockname": 1195,
    "getsockopt": 1204,
    "gettid": 1105,
    "gettimeofday": 1087,
    "getuid": 1046,
    "getunwind": 1215,
    "getxattr": 1220,
    "init_module": 1133,
    "inotify_add_watch": 1278,
    "inotify_init": 1277,
    "inotify_init1": 1318,
    "inotify_rm_watch": 1279,
    "io_cancel": 1242,
    "io_destroy": 1239,
    "io_getevents": 1240,
    "io_pgetevents": 1351,
    "io_setup": 1238,
    "io_submit": 1241,
    "io_uring_enter": 1450,
    "io_uring_register": 1451,
    "io_uring_setup": 1449,
    "ioctl": 1065,
    "ioprio_get": 1275,
    "ioprio_set": 1274,
    "kcmp": 1345,
    "kexec_load": 1268,
    "keyctl": 1273,
    "kill": 1053,
    "landlock_add_rule": 1469,
    "landlock_create_ruleset": 1468,
    "landlock_restrict_self": 1470,
    "lchown": 1124,
    "lgetxattr": 1221,
    "link": 1031,
    "linkat": 1289,
    "listen": 1193,
    "listxattr": 1223,
    "llistxattr": 1224,
    "lookup_dcookie": 1237,
    "lremovexattr": 1227,
    "lseek": 1040,
    "lsetxattr": 1218,
    "lstat": 1211,
    "madvise": 1209,
    "mbind": 1259,
    "membarrier": 1344,
    "memfd_create": 1340,
    "migrate_pages": 1280,
    "mincore": 1208,
    "mkdir": 1055,
    "mkdirat": 1282,
    "mknod": 1037,
    "mknodat": 1283,
    "mlock": 1153,
    "mlock2": 1346,
    "mlockall": 1154,
    "mmap": 1151,
    "mmap2": 1172,
    "mount": 1043,
    "mount_setattr": 1466,
    "move_mount": 1453,
    "move_pages": 1276,
    "mprotect": 1155,
    "mq_getsetattr": 1267,
    "mq_notify": 1266,
    "mq_open": 1262,
    "mq_timedreceive": 1265,
    "mq_timedsend": 1264,
    "mq_unlink": 1263,
    "mremap": 1156,
    "msgctl": 1112,
    "msgget": 1109,
    "msgrcv": 1111,
    "msgsnd": 1110,
    "msync": 1157,
    "munlock": 1158,
    "munlockall": 1159,
    "munmap": 1152,
    "name_to_handle_at": 1326,
    "nanosleep": 1168,
    "newfstatat": 1286,
    "nfsservctl": 1169,
    "old_getpagesize": 1171,
    "open": 1028,
    "open_by_handle_at": 1327,
    "open_tree": 1452,
    "openat": 1281,
    "openat2": 1461,
    "pciconfig_read": 1173,
    "pciconfig_write": 1174,
    "perf_event_open": 1352,
    "personality": 1140,
    "pidfd_getfd": 1462,
    "pidfd_open": 1458,
    "pidfd_send_signal": 1448,
    "pipe": 1058,
    "pipe2": 1317,
    "pivot_root": 1207,
    "pkey_alloc": 1355,
    "pkey_free": 1356,
    "pkey_mprotect": 1354,
    "poll": 1090,
    "ppoll": 1295,
    "prctl": 1170,
    "pread64": 1148,
    "preadv": 1319,
    "preadv2": 1348,
    "prlimit64": 1325,
    "process_madvise": 1464,
    "process_mrelease": 1472,
    "process_vm_readv": 1332,
    "process_vm_writev": 1333,
    "pselect6": 1294,
    "ptrace": 1048,
    "pwrite64": 1149,
    "pwritev": 1320,
    "pwritev2": 1349,
    "quotactl": 1137,
    "quotactl_fd": 1467,
    "read": 1026,
    "readahead": 1216,
    "readlink": 1092,
    "readlinkat": 1291,
    "readv": 1146,
    "reboot": 1096,
    "recv": 1200,
    "recvfrom": 1201,
    "recvmmsg": 1322,
    "recvmsg": 1206,
    "remap_file_pages": 1125,
    "removexattr": 1226,
    "rename": 1054,
    "renameat": 1288,
    "renameat2": 1338,
    "request_key": 1272,
    "restart_syscall": 1246,
    "rmdir": 1056,
    "rseq": 1357,
    "rt_sigaction": 1177,
    "rt_sigpending": 1178,
    "rt_sigprocmask": 1179,
    "rt_sigqueueinfo": 1180,
    "rt_sigreturn": 1181,
    "rt_sigsuspend": 1182,
    "rt_sigtimedwait": 1183,
    "rt_tgsigqueueinfo": 1321,
    "sched_get_priority_max": 1165,
    "sched_get_priority_min": 1166,
    "sched_getaffinity": 1232,
    "sched_getattr": 1337,
    "sched_getparam": 1160,
    "sched_getscheduler": 1162,
    "sched_rr_get_interval": 1167,
    "sched_setaffinity": 1231,
    "sched_setattr": 1336,
    "sched_setparam": 1161,
    "sched_setscheduler": 1163,
    "sched_yield": 1164,
    "seccomp": 1353,
    "select": 1089,
    "semctl": 1108,
    "semget": 1106,
    "semop": 1107,
    "semtimedop": 1247,
    "send": 1198,
    "sendfile": 1187,
    "sendmmsg": 1331,
    "sendmsg": 1205,
    "sendto": 1199,
    "set_mempolicy": 1261,
    "set_mempolicy_home_node": 1474,
    "set_robust_list": 1298,
    "set_tid_address": 1233,
    "setdomainname": 1129,
    "setfsgid": 1143,
    "setfsuid": 1142,
    "setgid": 1061,
    "setgroups": 1078,
    "sethostname": 1083,
    "setitimer": 1118,
    "setns": 1330,
    "setpgid": 1080,
    "setpriority": 1102,
    "setregid": 1072,
    "setresgid": 1076,
    "setresuid": 1074,
    "setreuid": 1071,
    "setrlimit": 1084,
    "setsid": 1081,
    "setsockopt": 1203,
    "settimeofday": 1088,
    "setuid": 1045,
    "setxattr": 1217,
    "shmat": 1114,
    "shmctl": 1116,
    "shmdt": 1115,
    "shmget": 1113,
    "shutdown": 1202,
    "sigaltstack": 1176,
    "signalfd": 1307,
    "signalfd4": 1313,
    "socket": 1190,
    "socketpair": 1197,
    "splice": 1297,
    "stat": 1210,
    "statfs": 1103,
    "statfs64": 1258,
    "statx": 1350,
    "swapoff": 1095,
    "swapon": 1094,
    "symlink": 1091,
    "symlinkat": 1290,
    "sync": 1050,
    "sync_file_range": 1300,
    "syncfs": 1329,
    "sysfs": 1139,
    "sysinfo": 1127,
    "syslog": 1117,
    "tee": 1301,
    "tgkill": 1235,
    "timer_create": 1248,
    "timer_delete": 1252,
    "timer_getoverrun": 1251,
    "timer_gettime": 1250,
    "timer_settime": 1249,
    "timerfd": 1308,
    "timerfd_create": 1310,
    "timerfd_gettime": 1312,
    "timerfd_settime": 1311,
    "times": 1059,
    "tkill": 1229,
    "truncate": 1097,
    "umask": 1067,
    "umount": 1044,
    "umount2": 1044,
    "uname": 1130,
    "unlink": 1032,
    "unlinkat": 1287,
    "unshare": 1296,
    "uselib": 1093,
    "userfaultfd": 1343,
    "ustat": 1069,
    "utimensat": 1306,
    "utimes": 1036,
    "vhangup": 1123,
    "vmsplice": 1302,
    "wait4": 1126,
    "waitid": 1270,
    "write": 1027,
    "writev": 1147,
}
