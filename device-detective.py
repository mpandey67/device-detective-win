import scapy.all as scapy
import subprocess
from intro import intr
from get_ip import get_ip_addr
subprocess.call("cls",shell=True)
intr()
lhost=get_ip_addr()
arp_req=scapy.ARP(pdst=lhost)
broadcast_mac=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
arp_req_broadcast_mac= broadcast_mac / arp_req
print("Please wait 20 seconds.")
answered=scapy.srp(arp_req_broadcast_mac,timeout=20,verbose=False)[0]
subprocess.call("cls",shell=True)
intr()
print("\n----------------------------------------------------------")
print("IP ADDRESS \t\t\t ASSOCIATED MAC")
print("----------------------------------------------------------\n")
for elements in answered:
    print(elements[1].psrc + "-------------------->" + elements[1].hwsrc)
print("\n")