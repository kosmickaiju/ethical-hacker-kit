import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Ethical Hacker Training Kit')
    parser.add_argument('--scan_network', action = 'store_true', help = 'Identify active hosts on a network and scan open ports')

    args = parser.parse_args()

    if args.scan_network:
        from scanners import network_scan, port_scan
        target = input('Enter target IP in IPv4: ')
        pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
        if re.fullmatch(pattern, target):
            port_scan.scan_target(target)
            network_scan.scan(target)
        else:
            print(f'Not a valid IPv4 address. Try again!')
        
if __name__ == '__main__':
    main()