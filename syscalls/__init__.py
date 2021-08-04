#!/usr/bin/python3

import os

from syscalls.tables.names import syscalls_names
from syscalls.tables.aarch64 import syscalls_aarch64
from syscalls.tables.alpha import syscalls_alpha
from syscalls.tables.arc import syscalls_arc
from syscalls.tables.arm64 import syscalls_arm64
from syscalls.tables.armoabi import syscalls_armoabi
from syscalls.tables.arm import syscalls_arm
from syscalls.tables.avr32 import syscalls_avr32
from syscalls.tables.blackfin import syscalls_blackfin
from syscalls.tables.c6x import syscalls_c6x
from syscalls.tables.cris import syscalls_cris
from syscalls.tables.csky import syscalls_csky
from syscalls.tables.frv import syscalls_frv
from syscalls.tables.h8300 import syscalls_h8300
from syscalls.tables.hexagon import syscalls_hexagon
from syscalls.tables.i386 import syscalls_i386
from syscalls.tables.ia64 import syscalls_ia64
from syscalls.tables.m32r import syscalls_m32r
from syscalls.tables.m68k import syscalls_m68k
from syscalls.tables.metag import syscalls_metag
from syscalls.tables.microblaze import syscalls_microblaze
from syscalls.tables.mips64n32 import syscalls_mips64n32
from syscalls.tables.mips64 import syscalls_mips64
from syscalls.tables.mipso32 import syscalls_mipso32
from syscalls.tables.mn10300 import syscalls_mn10300
from syscalls.tables.nds32 import syscalls_nds32
from syscalls.tables.nios2 import syscalls_nios2
from syscalls.tables.openrisc import syscalls_openrisc
from syscalls.tables.parisc import syscalls_parisc
from syscalls.tables.powerpc64 import syscalls_powerpc64
from syscalls.tables.powerpc import syscalls_powerpc
from syscalls.tables.riscv32 import syscalls_riscv32
from syscalls.tables.riscv64 import syscalls_riscv64
from syscalls.tables.s390 import syscalls_s390
from syscalls.tables.s390x import syscalls_s390x
from syscalls.tables.score import syscalls_score
from syscalls.tables.sh64 import syscalls_sh64
from syscalls.tables.sh import syscalls_sh
from syscalls.tables.sparc64 import syscalls_sparc64
from syscalls.tables.sparc import syscalls_sparc
from syscalls.tables.tile64 import syscalls_tile64
from syscalls.tables.tile import syscalls_tile
from syscalls.tables.unicore32 import syscalls_unicore32
from syscalls.tables.x32 import syscalls_x32
from syscalls.tables.x86_64 import syscalls_x86_64
from syscalls.tables.xtensa import syscalls_xtensa


class NoSuchSystemCall(Exception):
    pass


class NotSupportedSystemCall(Exception):
    pass


class syscalls(dict):
    def __init__(self):
        self.syscalls = {
            'names': syscalls_names,
            'archs': {
                'aarch64': syscalls_aarch64,
                'alpha': syscalls_alpha,
                'arc': syscalls_arc,
                'arm64': syscalls_arm64,
                'armoabi': syscalls_armoabi,
                'arm': syscalls_arm,
                'avr32': syscalls_avr32,
                'blackfin': syscalls_blackfin,
                'c6x': syscalls_c6x,
                'cris': syscalls_cris,
                'csky': syscalls_csky,
                'frv': syscalls_frv,
                'h8300': syscalls_h8300,
                'hexagon': syscalls_hexagon,
                'i386': syscalls_i386,
                'ia64': syscalls_ia64,
                'm32r': syscalls_m32r,
                'm68k': syscalls_m68k,
                'metag': syscalls_metag,
                'microblaze': syscalls_microblaze,
                'mips64n32': syscalls_mips64n32,
                'mips64': syscalls_mips64,
                'mipso32': syscalls_mipso32,
                'mn10300': syscalls_mn10300,
                'nds32': syscalls_nds32,
                'nios2': syscalls_nios2,
                'openrisc': syscalls_openrisc,
                'parisc': syscalls_parisc,
                'powerpc64': syscalls_powerpc64,
                'powerpc': syscalls_powerpc,
                'riscv32': syscalls_riscv32,
                'riscv64': syscalls_riscv64,
                's390': syscalls_s390,
                's390x': syscalls_s390x,
                'score': syscalls_score,
                'sh64': syscalls_sh64,
                'sh': syscalls_sh,
                'sparc64': syscalls_sparc64,
                'sparc': syscalls_sparc,
                'tile64': syscalls_tile64,
                'tile': syscalls_tile,
                'unicore32': syscalls_unicore32,
                'x32': syscalls_x32,
                'x86_64': syscalls_x86_64,
                'xtensa': syscalls_xtensa,
            },
        }

        self.default_arch = os.uname().machine

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key, arch=''):

        if arch == '':
            arch = self.default_arch

        try:
            return self.syscalls['archs'][arch][key]
        except KeyError:
            if key not in self.syscalls['names']:
                raise NoSuchSystemCall
            else:
                raise NotSupportedSystemCall

    def archs(self):
        return self.syscalls['archs'].keys()

    def names(self):
        return self.syscalls['names']
