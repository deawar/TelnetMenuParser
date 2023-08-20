import csv
import os.path

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
bbs_id = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
line_count = 0
grouped_lengths = group_and_get_length_by_first_character(filename)
for character, length in grouped_lengths.items():
    new_file_name = str(character) + ' telnet.ini'
    print('New file name:', new_file_name)
    print('test string:', length)
    if length < 36 and os.path.isfile(new_file_name):
            with open(new_file_name, 'a') as f:
                bbs_char = str(bbs_id[line_count])
                print('bbs_char string: ',bbs_char)
                print('length value:', grouped_lengths[character])
                print(f'Action=Telnet\nParameters={grouped_lengths[character]["TelnetAddress"]}\nPort={grouped_lengths[character]["bbsPort"]}\nRequiredAccess=10\n')
                print(f'Name={grouped_lengths[character]["bbsName"]}\n')
                print(f'Name={grouped_lengths[character]["bbsName"]}\nAction=Telnet\nParameters={grouped_lengths[character]["TelnetAddress"]}\nPort={grouped_lengths[character]["bbsPort"]}\nRequiredAccess=10\n')
                
                f.write(f'\n [{bbs_char}]\n')
                f.write(f'Name={grouped_lengths[character]["bbsName"]}\nAction=Telnet\nParameters={grouped_lengths[character]["TelnetAddress"]}\nPort={grouped_lengths[character]["bbsPort"]}\nRequiredAccess=10\n')
                line_count += 1
                if line_count > 36:
                    f.write('\n[*]\nName=Quit to Level Above\nAction=ChangeMenu\nParameters=TelnetDoor\nRequiredAccess=0\n')
    else:
            with open(new_file_name, 'w') as f:
                bbs_char = bbs_id[line_count]
                f.write(f'\n [{bbs_char}]\n')
                f.write(f'Name={grouped_lengths[character]["bbsName"]}\nAction=Telnet\nParameters={grouped_lengths[character]["TelnetAddress"]}\nPort={grouped_lengths[character]["bbsPort"]}\nRequiredAccess=10\n')
                line_count += 1
                #f.write('\n[*]\nName=Quit to Level Above\nAction=ChangeMenu\nParameters=TelnetDoor\nRequiredAccess=0\n')

    print(f"Character '{character}': {length} rows")

grouped_array = group_by_first_character(filename)
for character, data in grouped_array.items():
    print(f"{character} Telnet")
    for row in data:
        print(row)
    print()

# with open('bbslist.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     menu_letter = ""
#     menu_count = 0
#     x = 0
#     bbs_id = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             bbs_name = row[0]
#             id_only = bbs_name[0]
#             menu_id = ('[' + bbs_name[0] + ']')
#             file_name = str(f'{id_only} telnet.ini')
#             print('Testing the file_name Variable ', x)
#             if os.path.isfile(file_name):
#                  with open(file_name, 'a') as f:
#                     if x == 36:
#                         x = 0
#                     f.write('\n')
#                     f.write(f'[{bbs_id[x]}]\n')
#                     f.write(f'Name={row[0]}\nAction=Telnet\nParameters={row[3]}\nPort={row[4]}\nRequiredAccess=10\n')
#                     # f.write('\n[*]\nName=Quit to Level Above\nAction=ChangeMenu\nParameters=TelnetDoor\nRequiredAccess=0\n')
#                     print(f'[{bbs_id[x]}]') 
#                     print(f'Name={row[0]}\nAction=Telnet\nParameters={row[3]}\nPort={row[4]}\nRequiredAccess=10\n')
#                     x += 1
#             else:
#                 with open(file_name, 'w') as f:
#                     if x == 36:
#                         x = 0
#                     x += 1
#                     f.write('\n')
#                     f.write(f'[{bbs_id[x]}]\n')
#                     f.write(f'Name={row[0]}\nAction=Telnet\nParameters={row[3]}\nPort={row[4]}\nRequiredAccess=10\n')
#                     f.write('\n[*]\nName=Quit to Level Above\nAction=ChangeMenu\nParameters=TelnetDoor\nRequiredAccess=0\n')
#                     print(f'[{bbs_id[x]}]')
#                     print(f'Name={row[0]}\nAction=Telnet\nParameters={row[3]}\nPort={row[4]}\nRequiredAccess=10\n')
#             line_count += 1
#     print(f'Processed {line_count} lines.')
    