
# #Steps

# 1- first we will create function that takes the IPV4
# 2- The function will split the input and will cheack if it is 4 octs.
# 3- then it will cheack if all the octs are ints
# 4- Then will cheack if the ints are less 255
# 5- finally it will returen if it true or not 

def ipv4_cheacker(ip_input):
    octets = ip_input.split('.')

    if len(octets) != 4:
        return False

    for val in octets:
        if not val.isdigit(): 
            return False
            
        number = int(val)

        if number > 255 or number < 0:
            return False
    
    return True

ip_address = input("Enter the IPv4 address: ")

if ipv4_cheacker(ip_address):
    print("Valid IPv4 address")
else:
    print("Invalid IPv4 address")