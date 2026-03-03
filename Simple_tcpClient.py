from socket import *
import random
import time

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

def primo_fast(N):
    start_time = time.time()
    i = 2
    while i < N:
        if N % i == 0:
            end_time = time.time()
            print(f"{N} não é primo! Tempo: {end_time - start_time:.6f}s")
            return False
        i += 1
    end_time = time.time()
    print(f"{N} é primo! Tempo: {end_time - start_time:.6f}s")
    return True

serverName = "127.0.0.1"
serverPort = 1300

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

p = 23
g = 5

if not primo_fast(p):
    exit()

a = random.randint(1, 10)

A = pow(g, a, p)

clientSocket.send(str(A).encode())

B = int(clientSocket.recv(1024).decode())

chave = pow(B, a, p) % 26

print("Chave secreta gerada:", chave)

sentence = input("Digite a mensagem: ")

mensagem_cripto = cifra_cesar(sentence, chave)

clientSocket.send(mensagem_cripto.encode())

resposta_cripto = clientSocket.recv(65000).decode()

resposta = decifra_cesar(resposta_cripto, chave)

print("Resposta do servidor:", resposta)

clientSocket.close()