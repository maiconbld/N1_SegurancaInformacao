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

def primo_slow(N):
    start_time = time.time()
    cont = 0
    i = 2
    while i < N:
        if N % i == 0:
            cont += 1
        i += 1
    end_time = time.time()
    if cont == 0:
        print(f"{N} é primo! Tempo: {end_time - start_time:.6f}s")
        return True
    else:
        print(f"{N} não é primo! Tempo: {end_time - start_time:.6f}s")
        return False

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("TCP Server\n")

connectionSocket, addr = serverSocket.accept()

p = 23
g = 5

print("Teste Primo Fast:")
if not primo_fast(p):
    exit()

print("Teste Primo Slow:")
if not primo_slow(p):
    exit()

b = random.randint(1, 10)

A = int(connectionSocket.recv(1024).decode())

B = pow(g, b, p)

connectionSocket.send(str(B).encode())

chave = pow(A, b, p) % 26

print("Chave secreta gerada:", chave)

mensagem_cripto = connectionSocket.recv(65000).decode()
print("Recebido criptografado:", mensagem_cripto)

mensagem_original = decifra_cesar(mensagem_cripto, chave)
print("Descriptografado:", mensagem_original)

resposta = mensagem_original.upper()
resposta_cripto = cifra_cesar(resposta, chave)

connectionSocket.send(resposta_cripto.encode())

print("Resposta enviada:", resposta_cripto)

connectionSocket.close()