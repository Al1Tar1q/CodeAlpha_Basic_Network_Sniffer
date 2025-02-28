#!/usr/bin/env python3

from scapy.all import sniff

def packet_callback(packet):
   if packet.haslayer('TCP'):
        print(packet.summary())  # Print packet detailss

# Sniff packets on the default interface
sniff(filter='tcp', prn=packet_callback, store=False)
