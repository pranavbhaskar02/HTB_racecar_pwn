#!/bin/python3

from pwn import *
import re

flag = "0x567f51c0 0x170 0x565b4dfa 0x4f 0x5 0x26 0x2 0x1 0x565b596c 0x567f51c0 0x567f5340 0x7b425448 0x5f796877 0x5f643164 0x34735f31 0x745f3376 0x665f3368 0x5f67346c 0x745f6e30 0x355f3368 0x6b633474 0x7d213f 0x8276df00 0xf7f223fc 0x565b7f8c 0xff9cc7d8 0x565b5441 0x1 0xff9cc884 0xff9cc88c"
htbflag = []

for i in flag.split()[1:]:
    htbflag.append(p32(int(i, 16)))

print(b''.join(htbflag))
