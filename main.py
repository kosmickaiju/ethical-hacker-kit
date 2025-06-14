import argparse

def main():
    parser = argparse.ArgumentParser(description='Ethical Hacker Training Kit')
    parser.add_argument('--scan_network', action = 'store_true', help = 'Identify active hosts on a network and scan open ports')

    args = parser.parse_args()

    if args.scan_network():
        from scanners import network_scan, port_scan
        port_scan.scan_target()
        network_scan.scan()
