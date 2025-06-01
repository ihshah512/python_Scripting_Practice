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
    hop_pattern = re.compile(r"Hop\[\d+\]")

    # Filter lines containing the Hop pattern
    matching_lines = [line.strip() for line in trimmed_lines if hop_pattern.search(line)]

    return matching_lines

def main():
    filename = 'your_file.txt'  # Replace with your actual file path
    result = extract_hop_lines(filename)

    print("Lines containing Hop[x]:")
    for line in result:
        print(line)

if __name__ == "__main__":
    main()
