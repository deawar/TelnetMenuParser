#import module
import pprint
import sys
import math
import os
import lxml
from bs4 import BeautifulSoup as bs
from soup2dict import convert
content = []

first_char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
path = r'\gamesrv\menus\telnet'
print("******path = ",path,"******")

# Read the XML file
with open(sys.argv[1], "r", encoding='utf-8') as f:
#with open("minitest.xml", "r", encoding='utf-8') as f: # Short xml file for testing
#with open("dialdirectory.xml", "r", encoding='utf-8') as f:    # Full xml file intended for processing
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

# if 'X' in BBSList:
#     BBSInfo = BBSList['X'][0]
#     BBSName = BBSList['X'][0]['@name']
#     BBSLen = len(BBSList['X'])
#     print(BBSLen, "is the number of BBS's in this group")
#     print(BBSInfo)
#     print(BBSName)
# else:
#     print('Key not found')

def print_listing(BBSList):
    first_character = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    for x in BBSList:  
        print("Current Index:", [x])  
        BBSLen = len(BBSList[x])
        print(BBSLen, "is the number of BBS's in this group")
        if BBSLen == 1:
            name = BBSList[x][0]['@name']
            protocol = BBSList[x][0]['@protocol']
            ip = BBSList[x][0]['@ip']
            dirname = BBSList[x][0]
            print('\n')
            
            print(r"[" + x[0] + "]")
            print(r"Name=" + name)
            print(r"Action="+ protocol)
            print(r"Parameter="+ ip)
            print("RequiredAccess=10")
            print('\n')
        else:
            if BBSLen > 36:
                file_count = 0
                menu_counter = 0
                file_count = math.ceil(BBSLen/36)
                x_path = r" {path} + '\\' + {x}"
                print('New dir:',x_path)
                os.mkdir(x_path)
                while menu_counter < 37:
                    
                    for i in range(BBSLen):
                        name = BBSList[x][i]['@name']
                        protocol = BBSList[x][i]['@protocol']
                        ip = BBSList[x][i]['@ip']
                        #dirname = str(first_character[i])
                        dirname = first_character[i]
                        print(r"[" + dirname + "]")
                        print(r"Name=" + name)
                        print(r"Action="+ protocol)
                        print(r"Parameter="+ ip)
                        print("RequiredAccess=10")
                        print('\n')
                    menu_counter += 1            
                
def group_by_1st_char(BBSList):
    grouped_data = {}
    first_character = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
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
        file_name = '{first_character}, "  telnet.ini"'
        print("!!!!!!!!file_name=",file_name)
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
        
group_by_1st_char(BBSList) # Test print to display grouped data by 1st character
#print_listing(BBSList) # Test print to display what the contents of each <first_character> telnet.ini file should contain
print_listing(group_by_1st_char(BBSList)) # Test print to display the output from grouped_data dict