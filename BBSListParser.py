#import module
# from bs4 import BeautifulSoup as bs
# content = []
import xmltodict

# Read the XML file
# with open("dialdirectory.xml", "r") as file:
#     # Read each line in the file, readlines() returns a list of lines
#     content = file.readlines()
# # Combine the lines in the list into a string
# content = "".join(content)
# bs_content = bs(content, "lxml")

# xml_file=open("minitest.xml","r")
xml_file=open("dialdirectory.xml","r")
xml_string = xml_file.read()
def xml_to_dict(xml_string):
    root = xmltodict.parse(xml_string)
    result = {}
    for child in root:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = root(child)
    return result
print("The XML string is:")
print(xml_string)
# try:
python_dict = xmltodict.parse(xml_string)
BBSNum = len(python_dict['EtherTerm']['Phonebook']['BBS'])
print("The python dictionary Length is:", BBSNum)
BBSList = python_dict['EtherTerm']['Phonebook']['BBS']
print("The python dictionary is:")
# print(python_dict)
for x in BBSList:    
# for x,y in (python_dict['EtherTerm']['Phonebook']['BBS']).items():
    # BBS1 = dict(python_dict['EtherTerm']['Phonebook']['BBS'][BBSNum])
    print( )
    print("Name:",x['@name'])
    print("IP:",x['@ip'],":",x['@port'])
    print("Protocol:",x['@protocol'])
# except xmltodict.expat.ExpatError:
#     print ("That's Not Right...",xmltodict.expat.ExpatError)
