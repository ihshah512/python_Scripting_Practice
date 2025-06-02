#!/usr/bin/env python3
import re

def extract_hop_lines(filename):
    """
    Extract lines containing Hop[<number>] from a file,
    ignoring the first 4 and last 5 meaningful (non-empty) lines.
    """
    with open(filename, 'r') as file:
        lines = [line for line in file.readlines() if line.strip()]  # Remove empty/whitespace-only lines
    # Ignore the first 4 and last 5 non-empty lines
    trimmed_lines = lines[4:-5] if len(lines) > 9 else []  # avoid errors for short files
    # Regex to find Hop[number]
    hop_pattern = re.compile(r"Hop\[(\d+)]\s*(\d+)")

    hop_dict={}
    for line in trimmed_lines:
        match = hop_pattern.search(line)
        if match:
            key = int(match.group(1))
            value = int(match.group(2))
            hop_dict[key] = value
    return hop_dict

def extract_tune_info(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.readlines() if line.strip()]
        trimmed_lines = lines[5:-4] if len(lines) > 9 else []
        tune_pattren = re.compile(r"tune\s*(\d+)")
        tune_dict = {}
        key_counter = 1
        for line in trimmed_lines:
            match = tune_pattren.search(line)
            if match:
                value = int(match.group(1))
                tune_dict[key_counter] = value
                key_counter += 1
        return tune_dict

def findDiff(hop_data, tune_data, diff=5000):
        small_diff_found = False
        for key in hop_data:
            if key in tune_data:
                diffVal = abs(hop_data[key] - tune_data[key])
                if(diffVal<= diff):
                    print(f"key '{key}' tuneVal '{tune_data[key]}' hopVal '{hop_data[key]}' diff '{diffVal}'\n")
                    small_diff_found = True
        if not small_diff_found:
                    #print(f"key '{key}' tuneVal '{tune_data[key]}' hopVal '{hop_data[key]}'\n")
                    print("All good")

def main():
    filename = 'your_file.txt'  # Replace with your actual file path
    tune_file = 'tune_fiile.txt'
    hop_data = extract_hop_lines(filename)
    tune_data = extract_tune_info(tune_file)

    print("***Hop Dump***\n")
    for key, value in hop_data.items():
        print(f"'{key} '{value}'")
    print("Tune Dump\n")
    for key, value in tune_data.items():
        print(f"'{key}'  '{value}'")
    findDiff(hop_data, tune_data, 5000)

if __name__ == "__main__":
    main()
