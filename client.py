import socket

#Input public encryption exponent 'e' and public product of p and q 'n'
#Replace test with your public encryption exponent
e=17512638921991128148673572955423196442398344776117276381655465974556497974683223162719380226002238686944981024291091844333268797240361786630772293063344401280601895251453475347669309425887565536765298266807135940060169242071633221276473849 
#Replace test with your public product
n=239824525928633261759426794394074139593629501230504698260990607122842924837216030539750867462148246560347721497319614560989399214793681607342877447860817318116733589570985049578773638627100349992507284382880359138601392026338560785157530047

def encrypt(p,e,n):
    #Encrypt the plaintext and encode the resulting integer using big endian.
    p_int=int.from_bytes(p.encode(),"big")
    c=pow(p_int,e,n)
    return c

def main():
    #Replace host with ip address of the server, the system receiving the message.
    #Program will not function until valid ip address is used.
    host="server ip address"
    #Port 5555 is used for testing, can be changed to what user wants. Must be same on both client and server.
    port=5555
    s=socket.socket()
    s.connect((host,port))
    while True:
        message=input("->")
        if message=='q':
            break
        ciphertext=encrypt(message,e,n)
        s.send(str(ciphertext).encode())
        #Catch data sent by server to begin new message.
        data=s.recv(1024)
    s.close()

if __name__=='__main__':
    main()

