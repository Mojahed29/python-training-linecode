#Steps
# 1- I will make a funcyion that takes to parameters Enter an IP address and CIDR
# 2- For cheaking that the Ip is vaild i will use the function that been created in the first day but i will add another paremeter to cheack the cidr
# 3- Third point that i will create a function that takes the ip address and chnage it to 0s and 1
# 4- I will do another function that will takes cdir and make the sub mask
# 5- finally i will do a function that  network address, broadcast address, and the number of usable hosts for the given subnet.


def ipv4_cheacker(ip_input,cidr_input):
    octets = ip_input.split('.')
    try:
        cdir =int(cidr_input)
    except ValueError:
        print("it must be int")
        return False
    
    if len(octets) != 4:
        print("Error: There are not 4 octets.")
        return False 
    if cdir <0 or cdir >32:
        return False
    for val in octets:
        if not val.isdigit(): 
            print(f"Error: '{val}' is not a valid digit.")
            return False 
            
        number = int(val)

        if number > 255 or number < 0:
            print(f"Error: {number} is out of range (0-255).")
            return False

    print("Valid IPv4 address! and CIDR")


def ip_to_binary(ip_input):
    octs= ip_input.split('.')
    oct_zero = int(octs[0])
    oct_one = int(octs[1])
    oct_two = int(octs[2])
    oct_three = int(octs[3])

    ip_int = (oct_zero * 256**3) + (oct_one * 256**2) + (oct_two * 256**1) + (oct_three  * 256**0)
    return ip_int & 0xFFFFFFFF

def subnet_mask(cidr_in):
    cidr_digit = int(cidr_in)
    host_bits = 32 - cidr_digit
    
    mask_int = (0xFFFFFFFF << host_bits) & 0xFFFFFFFF
    
    return mask_int    

def network_address(ip_input, mask_int):
    return ip_input & mask_int

def broadcast_address(network_int, mask_int): 
    inverted_mask = ~mask_int & 0xFFFFFFFF
    
    broadcast = network_int | inverted_mask
    
    return broadcast
def usable_hosts(cidr_in):

    cidr = int(cidr_in)
    
    host_bits = 32 - cidr
    total_addresses = 2 ** host_bits
    
    if total_addresses < 2:
        return 0
        
    return total_addresses - 2

def int_to_ip(ip_int):

    o0 = (ip_int >> 24) & 255
    o1 = (ip_int >> 16) & 255
    o2 = (ip_int >> 8) & 255
    o3 = ip_int & 255
    return f"{o0}.{o1}.{o2}.{o3}"



user_ip = input("Enter an IP address : ")
user_cidr = input("Enter CIDR prefix : ")

if ipv4_cheacker(user_ip, user_cidr) != False:
    ip_num = ip_to_binary(user_ip)

    mask_num = subnet_mask(user_cidr)

    net_num = network_address(ip_num, mask_num)
    
    brd_num = broadcast_address(net_num, mask_num)
    
    print("\n---\nSubnet Calculator\n---")
    print(f"Network Address: {int_to_ip(net_num)}")
    print(f"Broadcast Address: {int_to_ip(brd_num)}")
    print(f"Number of Usable Hosts: {usable_hosts(user_cidr)}")
    print("-------------------------")