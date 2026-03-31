#How to get input form user in python:
user_name= input("Can I get your name: ")
print(user_name)

#Slicing
user_name= input("give me an IP address: ")
first_octet = user_name[0:3] 
print(first_octet)

#Lists
ip_list = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

ip_list.append("10.0.0.4")
ip_list.remove("10.0.0.2")

#dictionary
device = {
"hostname": "core-switch-1",
"ports": 48
}
print(device["hostname"]) 
print(device["ports"]) 