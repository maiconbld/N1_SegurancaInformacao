# 🔐 TCP Client-Server com Cifra de César

Este projeto implementa uma comunicação Cliente-Servidor utilizando **Sockets TCP em Python**, aplicando **criptografia com Cifra de César** nas mensagens trocadas.

---

## 📌 Objetivo

Simular uma comunicação segura entre cliente e servidor onde:

1. O cliente criptografa a mensagem
2. O servidor descriptografa
3. O servidor processa a mensagem (converte para maiúsculo)
4. O servidor criptografa novamente
5. O cliente descriptografa ao receber

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Biblioteca `socket`
- Algoritmo de Criptografia: Cifra de César

---

## 🔐 Como Funciona a Cifra de César

A Cifra de César é um método simples de criptografia por substituição, onde cada letra é deslocada um número fixo de posições no alfabeto.

Exemplo com chave = 3:


a → d
b → e
c → f


---

## 📂 Estrutura do Projeto


.
├── Simple_tcpServer.py
├── Simple_tcpClient.py
└── README.md


---

## 🖥️ Servidor (Simple_tcpServer.py)

### Funções principais:

- Recebe mensagem criptografada
- Descriptografa
- Converte para maiúsculo
- Criptografa novamente
- Envia de volta ao cliente

### Porta utilizada:

1300


---

## 💻 Cliente (Simple_tcpClient.py)

### Funções principais:

- Lê entrada do usuário
- Criptografa a mensagem
- Envia ao servidor
- Recebe resposta criptografada
- Descriptografa
- Exibe resultado final

---

## ▶️ Como Executar

### 1️⃣ Inicie o servidor

```bash
python Simple_tcpServer.py

Você verá:

TCP Server
2️⃣ Em outro terminal, execute o cliente
python Simple_tcpClient.py

Digite uma mensagem:

Input lowercase sentence: alou
🔄 Exemplo de Execução
Cliente digita:
alou
Fluxo interno:

Cliente envia: dorx

Servidor descriptografa: alou

Servidor converte: ALOU

Servidor envia criptografado: DORX

Cliente descriptografa: ALOU

Saída final no cliente:
Received: ALOU
📚 Conceitos Aplicados

Programação em Redes

Sockets TCP

Comunicação Cliente-Servidor

Criptografia Simétrica

Manipulação de Strings em Python

⚠️ Observações

A chave de criptografia utilizada é fixa (chave = 3)

O servidor aceita uma conexão por execução

Para múltiplas conexões, é necessário implementar loop ou threads
