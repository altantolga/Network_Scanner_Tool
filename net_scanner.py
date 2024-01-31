import scapy.all as scapy
import optparse

def get_user_input():
    parse_obj=optparse.OptionParser()
    parse_obj.add_option("-i","--ipaddress",dest="ip_address",help="Enter IP Address")

    (user_input,arguments)=parse_obj.parse_args()
    if not user_input.ip_address:
        print("Enter IP Address")
    return user_input


def scan_network(ip):
    arp_request_packet=scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet=scapy.Ether("ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet=broadcast_packet/arp_request_packet
    (answered,unanswered)=scapy.srp(combined_packet,timeout=1)
    answered.summary()

user_ip_address=get_user_input()
scan_network(user_ip_address.ip_address)

