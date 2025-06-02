import re


def check_unique_abc_values(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        enabled_found = False
        value_set = set()

    for line in lines:
        if not enabled_found:
            if "ENABLED" in line:
                enabled_found = True
                continue

        if "DecoyHop[" in line:
            try:
                key_part = line.split("DecoyHop[")[1].split("]")[0]
                value_part = line.split(":")[1].strip()
                print(f'{value_part}')
                value_set.add(value_part)
            except IndexError:
                continue  # Skip malformed lines

        if len(value_set) == 30:
            print("All values are unique.")
        else:
            print("Not unique. Only", len(value_set), "unique values found.")

# Example usage:
myFile = 'pn.txt'
check_unique_abc_values(myFile)
