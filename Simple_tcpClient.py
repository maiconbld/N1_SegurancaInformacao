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
serverName = "127.0.0.1"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Input lowercase sentence: ")
chave = 3  # temporário
mensagem_cripto = cifra_cesar(sentence, chave)
clientSocket.send(bytes(mensagem_cripto, "utf-8"))
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence,"utf-8")
mensagem_original = decifra_cesar(text, chave)
print("Received:", mensagem_original)