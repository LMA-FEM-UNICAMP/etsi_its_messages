#!/usr/bin/env python3

#########################################################################################################################
# From Cohda Support
# Sending Raw BTP packets from PC to MKx through UDP 
# This is a worked example on MK6C running exampleETSI which receives raw BTP packets through UDP and transmits them.

# On a PC, a python script is created containing the Raw BTP data packet. The BTP packet structure is as follows:

# UDP-BTP DataReq
#     BTPHdrVer: 4
#     BTPHdrId: Data Req (0)
#     BTPHdrLen: 95
#     BTPType: BTP-B (2)
#     PktTransport: SHB (7)
#     TrafficClass: 0x03
#     MaxPktLifetime: 0
#     DstPort: 3000
#     GNCommsProfile: 0x00
#     GNRepeatInterval: 0
#     GNSecurityProfile: NoSecurity (0)
#     GNSecurityITSAID: 0x0000008d
#     GNSecuritySSPLen: 0
#     GNSecuritySSPBits: <MISSING>
#     Length: 17
# Data (17 bytes)
#     Data: 0163000066660007380089119a22ab33b8
#     [Length: 17]
# The data string in the python script will therefore be as follows:

# '0400005f020703000bb8000000000000000000000000000000000000000000000000008d000000000000000
# 000000000000000000000000000000000000000000000000000110163000066660007380089119a22ab33b8' 
#########################################################################################################################


import socket
import time
import codecs

 
# addressing information of target
IPADDR = '143.106.207.85'
#PORTNUM = 9001
PORTNUM = 4403

# enter the data content of the UDP packet as hex

#Raw-BTP (no cert-id)
data = '0400005f020703000bb8000000000000000000000000000000000000000000000000008d000000000000000000000000000000000000000000000000000000000000000000110163000066660007380089119a22ab33b8'


# Below sends every nibble in ascii
#PACKETDATA = data.encode('ascii')

# Below sends hex bytes
#PACKETDATA = bytes.fromhex(data)

# Below also sends hex bytes
PACKETDATA = codecs.decode(data, "hex")


print (PACKETDATA)

try:
    # initialize a socket, think of it as a cable
    # SOCK_DGRAM specifies that this is UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
 
    # connect the socket, think of it as connecting the cable to the address location
    s.connect((IPADDR, PORTNUM))
except:
    print ('Failed to create socket')
    sys.exit()

while(1):
    time.sleep(1.0)
    try:
        # send the command
        s.send(PACKETDATA)
        print("ok")
    except:
	    print ("!!!!")
        #pass
 
# close the socket
s.close()
