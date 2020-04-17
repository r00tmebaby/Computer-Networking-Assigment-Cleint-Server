##############################################
# UDP Client: Computer Networking Assigment
# Author 	: Zdravko Georgiev
# License   : MIT
# Github 	: https://github.com/r00tmebaby
# Copyright (c) 2019 / 31.03.2019
# Version   : 0.1
###############################################

import socket
import time
import Config

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    string = input("\n[*] Client: Please type a word: ")
    n = len(string)

    if n % 2 == 0:
        s1 = "%.f%s%s%s%d" % (time.time(), Config.Separator, string[0:n // 2], Config.Separator, 1)
        s2 = "%.f%s%s%s%d" % (time.time(), Config.Separator, string[n // 2:n], Config.Separator, 2)
    else:
        s1 = "%.f%s%s%s%d" % (time.time(), Config.Separator, string[0:n // 2 + 1], Config.Separator, 1)
        s2 = "%.f%s%s%s%d" % (time.time(), Config.Separator, string[len(string[0:n // 2 + 1]):n], Config.Separator, 2)

    print(" [+] Step 1: Separating the given word to two packages S1 = %s and S2 = %s " % (s1, s2))

    try:
        sock.sendto(Config.encrypt(s1).encode(Config.Enc_Type),
                    (Config.Server_Host, Config.Server_Port))
        sock.sendto(Config.encrypt(s2).encode(Config.Enc_Type),
                    (Config.Server_Host, Config.Server_Port))
        print("  [++] Step 2: Encrypting and sending the two packages to the server "
              "\n               |S1=%s|  \n               |S2=%s| " %
              (Config.encrypt(s1), Config.encrypt(s2)))

    finally:
        r, addr = sock.recvfrom(Config.Buffer_Size)
        swapped_string = s2.split(Config.Separator)[1] + s1.split(Config.Separator)[1]
        returned_string = Config.decrypt(r.decode(Config.Enc_Type))
        print("[**] Server replies with encrypted r=%s" % r)
        print("[***] Decrypted result r=%s" % returned_string)
        if swapped_string == returned_string:
            print("[****] Final Result: The Server replied with %s that is concatenation of S2 (%s) + S1 (%s) "
                  "which is the expected result" % (
                      returned_string,
                      s2.split(Config.Separator)[1],
                      s1.split(Config.Separator)[1],))
        else:
            print("[!] Server Replayed with %s S2 (%s) + S1 (%s) and %s is an incorrect reply" % (
                      returned_string,
                      s2.split(Config.Separator)[1],
                      s1.split(Config.Separator)[1],
                      swapped_string))
