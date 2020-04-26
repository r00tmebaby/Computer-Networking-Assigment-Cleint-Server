# Computer-Networking-Assigment
 Simple networking game with server and client side that I created for Computer networking module.
 
 It was marked 100% so I think that it maybe helpfull to other students too. 



<b>UDP Client and Server Documentation</b>

<b>Client</b>
<img src='https://i.gyazo.com/a1241be37d7ee467fe3becdf9699394d.png'>

1. UDP client request a word to be typed by the user without any specific length or characters encoding requirements 
2. The client separates the word into two strings depending on the word length as described in the specifications. If the word length is an odd number, it will divide it in half + 1 letter and if the length is even number will separate it in half.
3. Then the client will add additional information to each of the produced strings because UDP protocol does not give a guarantee that the packages will be delivered or if they are delivered will remain in the same order. UDP by design is quick protocol but does not give any guarantees as TCP. So, I have decided to make sure that the dedicated packets contain information for their original order and the time when they have been sent and assigned. So we are adding additional information to each produced string (s1 and s2) in such a manner: time-separator-string-separator-position 
4. Then the client encrypts each of the produced strings, convert them to a binary string and send each one separately to the server as distinguish packet. 
5. The client waits for the server reply
6. When the answer from the server is received it the client decodes the received binary string and decrypts the contained data 
7. It compares the received string from the server whether it is a concatenation of s2+s1 and returns a message
8. Wait for the next word input

 
<b>Server</b>
<img src='https://i.gyazo.com/d7a1da5b0544add94595be232d53deca.png'>

1. The server binds to UDP socket if the port is free and wait for packets 
2. If a packet is received the server creates a temporary variable which is storing each one of them separated with a specific separator in such manner: packet1+separator+packet2+separator+packet3 etc
3. As requested in the requirements, we wait for only two packets to proceed with the next steps, which are: 
         3.1 Step 1 The server split both received packets and compare the times that they hold. In case that sending times are equal, that means those packets have been generated at the same time and belong to the requested word sent by the client. If the times are a different one of the packets is lost or different than the original, and the word cannot be retrieved. The server sends a notification message to the client. 
        3.2 Ste 2 The server compares by lexicographic order the enumeration that each packet hold and swap their places. It will place the more significant received number at the front and generate a new string. 
4. The server encrypts the produced string, convert it to a binary string and sends it back to the client
5. The server print a message that the task is completed and remain in waiting condition to receive new packets 
