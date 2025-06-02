"""

def extract_frequencies(file_path):
    frequencies = []
    with open(file_path, 'r') as file:
        for line in file:
            if "avoid with" in line:
                parts = line.split("avoid with")
                if len(parts) > 1:
                    number = parts[1].strip().split()[0]
                    if number.isdigit():
                        frequencies.append(number)
    print (frequencies)
    return frequencies


def search_frequencies_in_file(frequencies, search_file_path, output_file_path):
    found_any = False
    with open(search_file_path, 'r') as search_file:
        content = search_file.read()

    with open(output_file_path, 'w') as output_file:
        for freq in frequencies:
            if freq in content:
                output_file.write(f"Found frequency: {freq}\n")
                found_any = True

        if not found_any:
            output_file.write("None of the frequencies were found.\n")


def main():
    # Replace with your actual file paths
    input_file = 'input.txt'         # File with "frequency: ####"
    search_file = 'search_in.txt'    # File to search in
    output_file = 'results.txt'      # Output file for results

    frequencies = extract_frequencies(input_file)
    search_frequencies_in_file(frequencies, search_file, output_file)


if __name__ == "__main__":
    main()
"""