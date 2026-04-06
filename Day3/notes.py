#When dealing with files there are diffrernt types of actions you can do: you can read and write and append these are the main three actions and there are others as wel.
# the diffrernce between the write and append is that the right mode read then remove everything in the file and then write while the append is only adding to the end of the file.
# When we use with we dont need to use close()

#example:
with open("testing.txt",'w') as f:
    f.write("tesssst\n")
    f.write("nn")

with open("testing.txt",'r')as f:
    c =f.read()
    print(c)


import csv
#what is csv, csv is a comma saprated files 
csv_data = """hostname,ip_address,location
router1,192.168.1.1,New York
"""
with open('devices.csv', 'w') as f:
    f.write(csv_data)
with open('devices.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(f"Device: {row[0]}, IP: {row[1]}, Location: {row[2]}")