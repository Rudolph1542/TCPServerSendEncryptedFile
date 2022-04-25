from cryptography.fernet import Fernet
import socket


CHUNK_SIZE = 4096
send=1
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('127.0.0.1',65432))
print('Conectado')

f=Fernet(Fernet.generate_key())
print('Enviando archivo encriptado')
with open('tosend.txt','rb') as filee:
    data=filee.read(CHUNK_SIZE)
    encrypted=f.encrypt(data)
    soc.sendall(encrypted)
    print('Se envió archivo encriptado')
    soc.close()