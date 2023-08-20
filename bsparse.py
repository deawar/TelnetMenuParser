#import module
import pprint
import os
import lxml
from bs4 import BeautifulSoup as bs
from soup2dict import convert
content = []

first_char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
path = r'\gamesrv\menus\telnet'

# Read the XML file
with open("minitest.xml", "r", encoding='utf-8') as f:
    # Read each line in the file, readlines() returns a list of lines
    file = f.read()
    xml_string = bs(file, 'xml')

# Test print of XML file to be removed later
    print("The XML string is:")
    print(xml_string)

python_dict = convert(xml_string)
# BBSNum = len(python_dict['EtherTerm']['Phonebook']['BBS'])
# print("The python dictionary Length is:", BBSNum)
# BBSList = python_dict['EtherTerm']['Phonebook']['BBS']
BBSList = python_dict['EtherTerm'][0]['Phonebook'][0]['BBS']

print("The python dictionary is:")
# print(BBSList)

# Structure of the Telnet Menu ini file:
# [C]
# Name=The Shadowlands BBS 
# Action=Telnet
# Parameters=theshadowlandsbbs.ddns.net:2300
# RequiredAccess=10

def print_listing(BBSList):
    for x in BBSList:    
    # # for x,y in (python_dict['EtherTerm']['Phonebook']['BBS']).items():
        # BBS1 = dict(python_dict['EtherTerm']['Phonebook']['BBS'][BBSNum])
        print('\n')
        print(r"["+x['@name'][0]+"]")
        print(r"Name="+x['@name'])
        print(r"Action="+x['@protocol'])
        print(r"Parameter="+x['@ip']+":"+x['@port'])
        print("RequiredAccess=10")
        
def group_by_1st_char(BBSList):
    grouped_data = {}
    first_character = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    menu_counter = 0
    line_count = 0
    for x in BBSList:
        bbs_name = x['@name']
        first_character = bbs_name[0]
        first_character = first_character.upper()
        if first_character in grouped_data:
            grouped_data[first_character].append(x)
        else:
            grouped_data[first_character] = [x]
    length = len(grouped_data[first_character])
    print(grouped_data[first_character],"'s length is:", length)
    if length > 36:
        file_name = r'{first_character}, "  telnet.ini"'
        print("file_name=",file_name)
       # Check to see if file exists alread and if so append to it
        if os.path.isfile(file_name):
            with open(file_name, 'a') as f:
                if menu_counter == 36:
                    menu_counter = 0
                    f.write('\n')
                    f.write(f'[{[menu_counter]}]\n')
                    f.write(f'Name={grouped_data[0]}\nAction=Telnet\nParameters={grouped_data[3]}\nPort={grouped_data[4]}\nRequiredAccess=10\n')
                    # f.write('\n[*]\nName=Quit to Level Above\nAction=ChangeMenu\nParameters=TelnetDoor\nRequiredAccess=0\n')
                    print(f'[{first_character[menu_counter]}]') 
                    print(f'Name={grouped_data[0]}\nAction=Telnet\nParameters={grouped_data[3]}\nPort={grouped_data[4]}\nRequiredAccess=10\n')
                    x += 1
        else:
            with open(file_name, 'w') as f:
                if menu_counter == 36:
                    menu_counter = 0
                    menu_counter += 1
                    f.write('\n')
                    f.write(f'[{first_character[menu_counter]}]\n')
                    f.write(f'Name={grouped_data[0]}\nAction=Telnet\nParameters={grouped_data[3]}\nPort={grouped_data[4]}\nRequiredAccess=10\n')
                    f.write('\n[*]\nName=Quit to Level Above\nAction=ChangeMenu\nParameters=TelnetDoor\nRequiredAccess=0\n')
                    print(f'[{first_character[menu_counter]}]')
                    print(f'Name={grouped_data[0]}\nAction=Telnet\nParameters={grouped_data[3]}\nPort={grouped_data[4]}\nRequiredAccess=10\n')
            line_count += 1
    print(f'Processed {line_count} lines.')
        
        
    pprint.pprint(grouped_data)
    return grouped_data               
        
group_by_1st_char(BBSList)
#print_listing(BBSList)
#print_listing(group_by_1st_char(BBSList))