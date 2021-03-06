#!/usr/bin/env python

# Wed, 18 Jan 2017 (NZDT)
# test-IPflow.py:  Demonstrate IPflow objects
# Copyright (C) 2017, Nevil Brownlee, U Auckland | WAND

import plt
import natkit
from plt_testing import *

def test_uri(uri, tag=''):
    t = plt.trace(uri)
    t.start()

    nip = n = 0
    for pkt in t:
        n += 1
        test_println("n = %d" % n, tag+get_tag("n:"+str(n)))
        ipf = natkit.IPflow(pkt)
        if not ipf:
            test_println(" ", tag+get_tag())
            continue
        nip += 1

        test_println("%5d: %d %3d  %5d %5d  %s  %s" % (n,  # v6
           ipf.version, ipf.proto, ipf.src_port, ipf.dst_port,
           ipf.src_prefix, ipf.dst_prefix), tag+get_tag("n:"+str(n)))

        fwd = ipf.fwd_key
        test_print("fwd =",  tag+get_tag("n:"+str(n)))
        for b in fwd:
            test_print(" %02x" % b)

        rev = ipf.rev_key
        test_println('')
        test_print("rev =",tag+get_tag("n:"+str(n)))
        for b in rev:
            test_print(" %02x" % b)
        test_println('')

        if nip == 4:
            break

    t.close()

test_uri("pcapfile:anon-v4.pcap", get_tag())
test_uri("pcapfile:anon-v6.pcap", get_tag())
