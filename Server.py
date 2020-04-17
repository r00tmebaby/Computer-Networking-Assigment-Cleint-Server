##############################################
# UDP Server: Computer Networking Assigment
# Author 	: Zdravko Georgiev
# License   : MIT
# Github 	: https://github.com/r00tmebaby
# Copyright (c) 2019 / 31.03.2019
# Version   : 0.1
###############################################


import socket
import Config

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r = ""
temp_string = ""
counter = 0

try:
    sock.bind((Config.Server_Host, Config.Server_Port))
except socket.error as e:
    print("UDP Server can not bind the socket, please make sure the port in not in use. Error %s" % e)

print("UDP Server is bind to %s:%d and listen for packets" % (Config.Server_Host, Config.Server_Port))

while True:
    print("\nWaiting for packets...")
    data, address = sock.recvfrom(Config.Buffer_Size)
    data_decrypted = Config.decrypt(data.decode(Config.Enc_Type))
    if len(data_decrypted) > 0:
        counter += 1
        print(" -Packet %s from %s has been received" % (data, address))
        # Separate the packets with | to be able to assign them separatelly to s1 and s2 following the requiremets
        temp_string += data_decrypted + "|"		
        s1 = temp_string.split("|")[0]  
        s2 = temp_string.split("|")[1]
        # Proceed with these steps only if two packets are received (as requested in the requiremets)
        if counter == 2:
            print("[*] Server: Desired amount of packets received, cary on the next steps")
            print("   [+] Step 1: Decrypting the packages and assigning "
                  "\n               |S1=%s| and \n               |S2=%s|" % (s1, s2))
            # Check whether the packet timestamps are equal
            if s1.split(Config.Separator)[0] == s2.split(Config.Separator)[0]:
                print("      [++] Step 2: The received |S1=%s| and |S2=%s| timestamps are equal" %
                      (s1.split(Config.Separator)[0], s2.split(Config.Separator)[0]))
                # Swap the packet content positions and concatenate the result to a single packet 
                if s1.split(Config.Separator)[2] > s2.split(Config.Separator)[2]:
                    r = s1.split(Config.Separator)[1] + s2.split(Config.Separator)[1]
                else:
                    r = s2.split(Config.Separator)[1] + s1.split(Config.Separator)[1]
                print("         [+++] Step 3: Distinguish the strings, swap their places and concatenate the result")
                # Encrypt and encode the packet and sending it back to the client
                send = sock.sendto(Config.encrypt(r).encode(Config.Enc_Type), address)
                print("            [++++] Step 4: Encrypting the swapped word to "
                      "\n                           |R=%s| "
                      "\n                           and sending it back to the client" %
                      Config.encrypt(r))
                print("[*] Server: Task successfully completed")
            else:
			    # Send an error message to the client, because the received packets timestamps are different
                send = sock.sendto("Wrong packet received and the server can not return the right word"
                                   .encode(Config.Enc_Type), address)
            # Reset data storage and packets counter
            temp_string = ""
            r = ""
            counter = 0
