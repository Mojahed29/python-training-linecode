#Steps
# 1- I will make a funcyion that takes to parameters Enter an IP address and CIDR
# 2- For cheaking that the Ip is vaild i will use the function that been created in the first day but i will add another paremeter to cheack the cidr
# 3-


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

user_ip= input("give me the IP")
user_cidr= input("give me the Cidr")
ipv4_cheacker(user_ip,user_cidr)