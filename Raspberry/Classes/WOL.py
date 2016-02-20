from scapy.all import *

def WOL(mac):
	#thanks to http://www.networknewz.com/2011/08/16/introduction-to-scapy/
	mac = mac.decode("hex")
	eff = '\xff'
	sendp(Ether(dst='ff:ff:ff:ff:ff:ff') / IP(dst='255.255.255.255') /UDP(dport=7) /Raw(eff*6 + mac*16))