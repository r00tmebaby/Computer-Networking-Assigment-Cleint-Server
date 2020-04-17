##############################################
# Config File : Computer Networking Assigment
# Author 	  : Zdravko Georgiev
# License     : MIT
# Github 	  : https://github.com/r00tmebaby
# Copyright (c) 2019 / 31.03.2019
# Version     : 0.1
###############################################

import base64

Cipher_Key  = "BirkBeck!Computing!2019" # An Unique key that is used for the packet encryption
Enc_Type    = "utf-8"                   # Encoding standart, can be ascii etc. depending on the requirements
Separator   = "[*&]D#]"                 # Used to distinguish the start and the end of each packet data
Server_Host = "127.0.0.1"               # Server IP address, can be hostname as well
Server_Port = 8080                      # Port number used by the server. Make sure that it is not in use.
Buffer_Size = 1024                      # Receiver and sender socket buffer size. A large socket receiver buffer is essential to support high throughput.


def encrypt(clear):
    enc = []
    for i in range(len(clear)):
        key_c = Cipher_Key[i % len(Cipher_Key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decrypt(enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = Cipher_Key[i % len(Cipher_Key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

