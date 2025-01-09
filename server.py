import socket

#Input private decryption exponent 'd' and public product of p and q 'n'
#replace test with your private decryption exponent
d=205427362442740753587449610502685875612911234704695910823818235952662772995999403523647281048281202619436397191582931986870558796182847146107913588501064879147880671119105880438421144901925170947603791871714749055179896568583298353078739449
#replace test with your public product
n=239824525928633261759426794394074139593629501230504698260990607122842924837216030539750867462148246560347721497319614560989399214793681607342877447860817318116733589570985049578773638627100349992507284382880359138601392026338560785157530047

def decrypt(c,d,n):
    #Decrypt the ciphertext as an integer and decode the integer using big endian.
    c_int=pow(c,d,n)
    p=c_int.to_bytes((c_int.bit_length()+7)//8,"big").decode()
    return p

def main():
    #Replace host with ip address of the server, the system receiving the message.
    #Program will not function until valid ip address is used.
    host='server ip address'
    #Port 5555 is used for testing, can be changed to what user wants. Must be same on both client and server.
    port=5555
    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    print("Listening on port ",port)
    c,addr=s.accept()
    print("Connected")
    while True:
        data=c.recv(1024)
        if not data:
            break
        ciphertext=int(data.decode())
        plaintext=decrypt(ciphertext,d,n)
        print(plaintext)
        #Ciphertext is printed as a demonstration. Can be removed if user
        #only wants the plaintext to be shown and the number hidden.
        print(ciphertext)
        #Needs to send back data so that client receives a new prompt after each message.
        c.send(plaintext.encode())
    c.close()
    print("Disconnected")

if __name__=='__main__':
    main()