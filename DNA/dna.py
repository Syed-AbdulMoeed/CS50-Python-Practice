import csv
import sys



def check_cli():
    if len(sys.argv) != 3:
        sys.exit("Include database and then DNA sequence to identify")


def read_csv(database):
    rows = []
    with open(database) as file:  # Open csv file with dict reader
        reader = csv.DictReader(file)
        strs = reader.fieldnames
        for row in reader:  # Making a list of dictionaries
            rows.append(row)
        strs.remove('name')  # Remove 'name' to loop easier later
        return rows, strs


def read_txt(text):
    with open(text) as file:
        return file.readline().strip()


def get_matches(dna_seq, strs):
    return {a_str: str(longest_match(dna_seq, a_str)) for a_str in strs}
    


def find_match(database, matches):
    for i in range(len(database)):  # db is list
        name = database[i]['name']  # Storing and then deleting name so both matches and database[i] have
        del database[i]['name']     # Same key value pairs making comparision easy
        if database[i] == matches:
            return name
    return "No match"

def main():

    # Check for command-line usage
    check_cli()
    # Read database file into a variable
    database, strs = read_csv(sys.argv[1])
    # Read DNA sequence file into a variable
    dna_seq = read_txt(sys.argv[2])
    # Find longest match of each STR in DNA sequence
    matches = get_matches(dna_seq, strs)
    # Check database for matching profiles
    return  find_match(database, matches)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


print(main())
