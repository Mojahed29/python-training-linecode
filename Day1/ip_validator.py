
# #Steps

# 1- first we will create function that takes the IPV4
# 2- The function will split the input and will cheack if it is 4 octs.
# 3- then it will cheack if all the octs are ints
# 4- Then will cheack if the ints are less 255
# 5- finally it will returen if it true or not 

def ipv4_cheacker(ip_input):
    octets = ip_input.split('.')

    if len(octets) != 4:
        print("Error: There are not 4 octets.")
        return 

    for val in octets:
        if not val.isdigit(): 
            print(f"Error: '{val}' is not a valid digit.")
            return
            
        number = int(val)

        if number > 255 or number < 0:
            print(f"Error: {number} is out of range (0-255).")
            return
    
    print("Valid IPv4 address!")

ip_address = input("Enter the IPv4 address: ")

ipv4_cheacker(ip_address)