def cifra_cesar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            deslocado = (ord(char) - base + chave) % 26
            resultado += chr(base + deslocado)
        else:
            resultado += char
    return resultado


def decifra_cesar(texto, chave):
    return cifra_cesar(texto, -chave)


from socket import *

serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5)

print ("TCP Server\n")

connectionSocket, addr = serverSocket.accept()

sentence = connectionSocket.recv(65000)
received = str(sentence,"utf-8")

print ("Received From Client:", received)

chave = 3

mensagem_original = decifra_cesar(received, chave)
print("Descriptografado:", mensagem_original)

mensagem_resposta = cifra_cesar(mensagem_original.upper(), chave)

connectionSocket.send(bytes(mensagem_resposta,"utf-8"))

print("Sent back to Client:", mensagem_resposta)

connectionSocket.close()