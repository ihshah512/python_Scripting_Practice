import re

"""
This program will get required data from two files and compare their ressult
and find the difference. 



def read_txmodem(filename):
    tx_data = {} #Declaration of empty dictionary for key value pairs {}
    key = 1 #counter for assigning the keys to the values
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'tune\s+(\d+)', line)
            if match:
                tx_data[key] = int(match.group(1))
                key += 1
                if key > 32:
                    break
    return tx_data

def read_rxmodem(filename):
    rx_data = {}
    #found_hop_32 = False
    with open(filename, 'r') as file:
        for line in file:
            hop_match = re.search(r'Hop\[(\d+)\]', line)
            if hop_match:
                key = int(hop_match.group(1))
                freq_match = re.search(r'Frequency:\s*(\d+)', line)
                if freq_match:
                    rx_data[key] = int(freq_match.group(1))
                if key == 32:
                    break  # Stop after Hop[32]
    return rx_data

def compare_frequencies(tx_data, rx_data):
    print("Mismatches (difference not > ±1,000,000):")
    for key in range(1, 33):
        tx_val = tx_data.get(key)
        rx_val = rx_data.get(key)

        if tx_val is not None and rx_val is not None:
            diff = tx_val - rx_val
            #print("tx_val {}: key {}: rx_val {} key {}: diff {}: ".format(tx_val, key, rx_val, key, diff))
            if abs(diff) <= 1000000:
                print("Key {}: TX = {}, RX = {}, Diff = {}".format(key, tx_val, rx_val, diff))
    if abs(diff) > 1000000:
        print("Tx and Rx Frqs are more than 1MHZ apart")
# ---- Main Execution ----

tx_filename = "txmodem.log"
rx_filename = "rxmodem.log"

tx_data = read_txmodem(tx_filename)
rx_data = read_rxmodem(rx_filename)

compare_frequencies(tx_data, rx_data)
"""