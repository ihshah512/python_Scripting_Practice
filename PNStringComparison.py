import sys
import re

def check_unique_abc_values(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    enabled_found = False
    value_set = set()# choose set becauese we want unique keys
    #skip all lines untill you see ENABLED string
    for line_number, line in enumerate(lines, start=1):
        if not enabled_found:
            if "ENABLED" in line:
                enabled_found = True
            continue  # Skip all lines before ENABLED

        if "DecoyHop[" in line:
            try:
                # Use regex to extract DecoyHop number and value
                match = re.search(r'DecoyHop\[(\d+)\]:\s*(.*)', line)
                if match:
                    hop_number = match.group(1)
                    value_part = match.group(2).strip()

                    if value_part in value_set:
                        sys.stderr.write(
                            f"Error: Duplicate value found on line {line_number} "
                            f"at DecoyHop[{hop_number}]: {value_part}\n"
                        )
                        sys.exit(1)

                    value_set.add(value_part)

            except IndexError:
                continue  # Skip malformed lines

    # If all values are unique
    print("All values are unique. List of unique values:")
    key = 2
    for value in value_set:
        print(f"DecoyHop {key} : {value}")
        key +=1




# Example usage:
myFile = 'pn.txt'
check_unique_abc_values(myFile)
