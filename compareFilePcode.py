import re


def readHopFile(filename):
    hop_data = {}
    with open(filename, 'r') as file:
        for line in file:
            hop_match = re.search(r'Hop\[(\d+)\]', line)#this line actually looking for regex in line it will return a true or false
            if hop_match:
                key = int(hop_match.group(1))
                freq_match = re.earch(r'Frequency:\s*(\d+)', line)
                if freq_match:
                    hop_data[key] = int(freq_match.group(1))
                if key == 32:
                    break
    return hop_data

def readTuneFreq(filename):
    tune_data = {}
    with open(filename, 'r') as file:
        key = 1
        for line in file:
            tune_match = re.search(r'Tune\s+(\d+)', line)
            if tune_match:
                tune_data[key] = int(tune_match.group(1))
            if key == 32:
                break
    return tune_data

#tx_filename = "txmodem.log"
rx_filename = "rxmodem.log"

#tx_data = read_txmodem(tx_filename)
hop_data = readHopFile(rx_filename)




