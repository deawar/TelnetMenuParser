import csv
import os

first_char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
path = "d:\gamesrv\menus\\telnet"
def group_and_get_length_by_first_character(filename):
    grouped_data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bbs_name = row['bbsName']
            first_character = bbs_name[0]
            first_character = first_character.upper()
            if first_character in grouped_data:
                grouped_data[first_character].append(row)
            else:
                grouped_data[first_character] = [row]
    
    lengths = {}
    for character, data in grouped_data.items():
        lengths[character] = len(data)
    
    return lengths

def group_by_first_character(filename):
    grouped_data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bbs_name = row['bbsName']
            first_character = bbs_name[0]
            first_character = first_character.upper()
            if first_character in grouped_data:
                grouped_data[first_character].append(row)
            else:
                grouped_data[first_character] = [row]
    return grouped_data

# Example usage:
filename = "bbslist.csv"
grouped_array = group_by_first_character(filename)
for character, data in grouped_array.items():
    print(f"{character} Telnet")
    for row in data:
        print(row)
    print()

grouped_lengths = group_and_get_length_by_first_character(filename)
file_counter = 0
for character, length in grouped_lengths.items():
    num_of_rows = int(length)
    if num_of_rows > 36:
        print("length is: ", length)
        file_name = "{first_char[file_counter]}telnet.ini"
        filepath = os.path.join(path,file_name)
        file_char = str(character)
        os.mkdir(file_char)
        with open(file_name, 'w') as f:
            f.write(f'{file_char}telnet.ini') 
    file_counter += 1         
    print(f"Character '{file_char}': {length} rows")


