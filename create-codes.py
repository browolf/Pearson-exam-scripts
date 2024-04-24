import os
import random
import sys
import csv

server_path=r"\\dfs\pupilareas\assessment\\"
list_of_accounts = []
unique_prefixes=[]

def createcode():
    charlist ="abcdefghijkmnprstuvwxyz23456789"
    code = ""
    while len(code) < 10:
        code = code + charlist[random.randint(0,len(charlist)-1)]
    return code

number_of_accounts = int(input("How many accounts? "))

#LIST THE PREFIXES THAT ALREADY EXIST
subfolders = [ f.name for f in os.scandir(server_path) if f.is_dir() and "-" in f.name ]
for folder in subfolders:
    prefix = folder.split("-")[0].upper()
    if prefix not in unique_prefixes:
        unique_prefixes.append(prefix)

print(f"Current prefixes are: {', '.join(unique_prefixes)}")
prefix = input("Enter unique prefix: ").upper()

for x in range(number_of_accounts):
    foldername = prefix + "-" + createcode()
    try:
        os.mkdir(server_path + foldername)
    except Exception as e:
        print(f"Error creating {server_path + foldername} Exiting script")
        sys.exit()
    else:
        list_of_accounts.append(foldername)

print(list_of_accounts)
try:
    with open(server_path + f"Codes-{prefix}-{number_of_accounts}.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Code"])
        for account in list_of_accounts:
            writer.writerow([account])
except Exception as e:
    print("Error writing csv file")
    sys.exit()
else:
    print(f"Codes written to {server_path[:-1]}Codes-{prefix}-{number_of_accounts}.csv")
