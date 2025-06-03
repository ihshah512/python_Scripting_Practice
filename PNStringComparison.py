import re
import sys

def check_decoyhop_duplicates(filename):
    value_set = set()
    start_collecting = False

    # Updated regex: DecoyHop[NUMBER]: VALUE
    pattern = re.compile(r'DecoyHop\[\d+\]:\s*(\S+)')

    try:
        with open(filename, 'r') as file:
            counter = 0
            for line_num, line in enumerate(file, 1):
                match = pattern.search(line)
                if match:
                    counter += 1
                    value_part = match.group(1)
                    #print(f"{value_part}")
                    if not start_collecting:
                        start_collecting = True
                    if value_part in value_set:
                        print(f"Error: Duplicate value_part '{value_part}' found at line {line_num}")
                        return False
                    value_set.add(value_part)

        print(f"Script finished successfully. No duplicates found. All {counter} decoys accounted for")
        return True

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False


# Example usage:
myFile = 'pn.txt'
check_decoyhop_duplicates(myFile)
