#!/usr/bin/python3


import argparse
import string

"""
Address conversion
Create pattern max 6760
Offset calculation
Fix address filling and reversing

"""

pattern = ""
correct_pattern = ""
fix_potlas = "0"
def main():

    print("\n")
    print("Pizs\\x69 Buffer Overflow Tool")
    print("\n")

    parser = argparse.ArgumentParser()
    parser.add_argument("-a64","--address64",help="Adjon megy egy 64-bites címet",type=str)
    parser.add_argument("-a32","--address32",help="Adjon megy egy 32-bites címet",type=str)
    parser.add_argument("-32f","--address32f",help="Adjon megy egy 32-bites fix címet",type=str)
    parser.add_argument("-64f","--address64f",help="Adjon megy egy 64-bites fix címet",type=str)
    parser.add_argument("-p","--pattern",help="Adja meg a pattern méretét default azthiszem valami 6760 > 26*26*10",type=int)
    parser.add_argument("-o","--offset",help="Adja meg az offset hex értékét",type=str)
    parser.add_argument("-fp","--fixpotlas",help="Adja meg a cím feltöltési értékét(default \'0\')",type=str)

    parser.add_argument("-s","--skeleton",help="Ipv4 reverse shell script skeleton.(reverse_script.py)",action='store_true')

    args = parser.parse_args()

    global correct_pattern
    global fix_potlas


    if(args.skeleton):
        Skeleton_script()



    if(args.fixpotlas):
        fix_potlas = args.fixpotlas[0]

    if(args.address32f):
        address32f_temp=args.address32f
        correct_address32f = ""
        if(address32f_temp[0]=="0" and address32f_temp[1]=="x"):
            address32f_temp = address32f_temp[2:]

        if(len(address32f_temp)==8):
            for s in reversed(range(len(address32f_temp))):
                #if(s!=1):
                if(s%2==1):
                    print("\\x"+address32f_temp[s-1]+address32f_temp[s],end='',flush=True)
 
        if(len(address32f_temp)<8):
            potlas_count = 8-len(address32f_temp)
            correct_address32f = str(fix_potlas)*potlas_count+address32f_temp
            if(len(correct_address32f)==8):
                for s in reversed(range(len(correct_address32f))):
                    if(s%2==1):
                        print("\\x"+correct_address32f[s-1]+correct_address32f[s],end='',flush=True)


    if(args.address64f):
        address64f_temp=args.address64f
        correct_address64f = ""
        if(address64f_temp[0]=="0" and address64f_temp[1]=="x"):
            address64f_temp = address64f_temp[2:]

        if(len(address64f_temp)==12):
            for s in reversed(range(len(address64f_temp))):
                if(s%2==1):
                    print("\\x"+address64f_temp[s-1]+address64f_temp[s],end='',flush=True)

        if(len(address64f_temp)<12):
            potlas_count = 12-len(address64f_temp)
            correct_address64f = str(fix_potlas)*potlas_count+address64f_temp
            if(len(correct_address64f)==12):
                for s in reversed(range(len(correct_address64f))):
                    if(s%2==1):
                        print("\\x"+correct_address64f[s-1]+correct_address64f[s],end='',flush=True)





    if(args.address32):
        address_temp=args.address32

        if(address_temp[0]=="0" and address_temp[1]=="x"):
            address_temp = address_temp[2:]

        if(len(address_temp)==8):
            for s in reversed(range(len(address_temp))):
                #if(s!=1):
                if(s%2==1):
                    print("\\x"+address_temp[s-1]+address_temp[s],end='',flush=True)
        else:
            print("Nem jó a 32 bites cím.")
        
    if(args.address64):
        address_temp=args.address64
    
        if(address_temp[0]=="0" and address_temp[1]=="x"):
            address_temp = address_temp[2:]

        if(len(address_temp)==12):
            for s in reversed(range(len(address_temp))):
                #if(s!=1):
                if(s%2==1):
                    print("\\x"+address_temp[s-1]+address_temp[s],end='',flush=True)
        else:
            print("Nem jó a 64 bites cím.")


    if(args.pattern and args.offset==None):
        pattern_temp = args.pattern
        if(pattern_temp<=6760 and pattern_temp!=0):
            Pattern_gen(pattern_temp)
            print(correct_pattern)
            
    if(args.offset):
        if(args.pattern==None):
            print("Szükséges az előző pattern méret")
        else:
            pattern_temp = args.pattern
            Pattern_gen(pattern_temp)
            
            offset=args.offset
            if(offset[0]=="0" and offset[1]=="x"):
                offset = offset[2:]
                
            correct_offset=bytes.fromhex(offset).decode('utf-8')
            Offset(correct_offset)

    print("\n\n")
    

def Pattern_gen(size):
    global pattern
    global correct_pattern
    count = 0

    for s0 in string.ascii_uppercase:
            #count+=1
            for s1 in string.ascii_lowercase:
                #count+=1
                for s2 in range(10):

                    count +=3
                    pattern+=s0+s1+str(s2)
                    if(count>=size):
                        break
                if(count>=size):
                        break
            if(count>=size):
                        break
    
    correct_pattern = pattern[:size]

def bad_chars_just_note():
    badchars = (
    b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
    b"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
    b"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
    b"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
    b"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
    b"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
    b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
    b"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
    b"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
    b"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
    b"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
    b"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
    b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
    b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
    b"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
    b"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
def Skeleton_script():
    file = open("reverse_script.py","w+")

    file.write("import socket\n")
    file.write("import sys\n")
    file.write("import os\n")
    file.write("\n")
    file.write("host = \"127.0.0.1\"\n")
    file.write("port=12345\n")
    file.write("\n")
    file.write("client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n")
    file.write("client.connect((host,port))\n")
    file.write("#client.recv(512)\n")
    file.write("A=\'\\x90\'#*A méret\n")
    file.write("\n")
    file.write("#B=\"\"")
    file.write("\n")
    file.write("buf=\"\"\n")
    file.write("\n")
    file.write("#V=\'\\x90\'#Végén eltolás ha szükséges")
    file.write("\n")
    file.write("cim=\"\"\n")
    file.write("\n")
    file.write("payload=\"\"\n")
    file.write("#client.send(payload.encode(\'latin-1\'))  #encode ha kell\n")
    file.write("client.send(payload)\n")
    file.write("#client.recv(512)\n")
    file.write("client.close()\n")
    file.close()

    print("Elkészült a reverse_script.py fájl.")



def Offset(offset):
    reverse_offset = ""
    for r in reversed(offset):
        reverse_offset+=r
        
    result = correct_pattern.find(reverse_offset)+len(reverse_offset)

    print("Offset: ",result)

if __name__ == "__main__":
    main()
