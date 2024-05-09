import socket


def scan(target, prts):
    print('\n' + " Starting scan for " + str(target))
    for port in range(1, prts):
        scan_target(target, port)


def scan_target(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port open " + port + " " + ipaddress)
    except:
        print('')


targets = input("Enter the targets you wish to scan. Separate with comma if you multiple: ")
ports = int(input("Enter the amount of ports you wish to scan: "))

if ',' in targets:
    print("Scanning multiple targets:")
    for ip_add in targets.split(','):
        scan(ip_add.strip(), ports)

else:
    scan(targets, ports)
