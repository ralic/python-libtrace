#!/usr/bin/env python

# Thu, 13 Mar 14 (PDT)
# ip6.py:  Demonstrate IPv6 objects
# Copyright (C) 2017, Nevil Brownlee, U Auckland | WAND

from plt_testing import *

t = get_example_trace('anon-v6.pcap')

n = 0
for pkt in t:
    ip6 = pkt.ip6
    if not ip6:
        continue
    n += 1  # Wireshark uses 1-org packet numbers

    print("%5d: " % (n), end=' ')
    print_ip6(ip6, 12)
    print()
    if n == 20:
        break

t.close()  # Don't do this inside the loop!

