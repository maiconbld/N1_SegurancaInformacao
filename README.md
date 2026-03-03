# 🔐 TCP Client-Server com Diffie-Hellman e Teste de Primalidade

Este projeto implementa uma comunicação **Cliente-Servidor utilizando Sockets TCP em Python**, aplicando:

- 🔐 Troca de chaves com Diffie-Hellman
- 🔑 Criptografia simétrica com Cifra de César
- 🧮 Teste de números primos (Fast e Slow)
- ⏱ Medição de tempo de execução

---

## 📌 Objetivo

Simular uma comunicação segura onde:

1. O número primo `p` é validado antes do uso
2. Cliente e servidor executam Diffie-Hellman
3. Uma chave simétrica é gerada dinamicamente
4. A chave é utilizada para criptografar mensagens
5. O servidor processa a mensagem e envia resposta criptografada

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Biblioteca `socket`
- Biblioteca `time`
- Algoritmo de Diffie-Hellman
- Cifra de César

---

## 🔐 1️⃣ Teste de Primalidade

Antes de executar o Diffie-Hellman, o número `p` é testado utilizando dois algoritmos:

### Primo Fast

Interrompe assim que encontra um divisor.

### Primo Slow

Testa todos os divisores possíveis antes de decidir.

Ambos exibem:

- Se o número é primo ou não
- Tempo de execução

Isso garante que `p` atende ao requisito matemático do Diffie-Hellman.

---

## 🔑 2️⃣ Diffie-Hellman

O algoritmo criado por  
Whitfield Diffie e Martin Hellman  
permite que duas partes gerem uma chave secreta compartilhada sem enviá-la diretamente.

### Etapas:

1. Escolha pública de:
   - `p` (número primo)
   - `g` (base)

2. Cliente escolhe segredo privado `a`
3. Servidor escolhe segredo privado `b`

4. Cliente envia:

A = g^a mod p


5. Servidor envia:

B = g^b mod p


6. Ambos calculam:

Chave = B^a mod p
Chave = A^b mod p


Resultado: mesma chave secreta para ambos.

A chave final é ajustada com:

chave % 26

para ser usada na Cifra de César.

---

## 🔐 3️⃣ Cifra de César

A mensagem é criptografada utilizando deslocamento no alfabeto baseado na chave gerada dinamicamente.

Exemplo:


a → d
b → e
c → f


---

## 🔄 Fluxo Completo da Comunicação

1. Servidor inicia
2. Número primo `p` é testado (Fast e Slow)
3. Cliente conecta
4. Diffie-Hellman gera chave secreta
5. Cliente envia mensagem criptografada
6. Servidor descriptografa
7. Servidor converte para maiúsculo
8. Servidor criptografa novamente
9. Cliente descriptografa e exibe resultado

---

## 📂 Estrutura do Projeto


.
├── Simple_tcpServer.py
├── Simple_tcpClient.py
└── README.md


---

## ▶️ Como Executar

### 1️⃣ Inicie o servidor

```bash
python Simple_tcpServer.py
2️⃣ Em outro terminal, execute o cliente
python Simple_tcpClient.py
🧪 Exemplo de Execução

Cliente digita:

alou

Fluxo interno:

Chave secreta gerada via Diffie-Hellman

Cliente envia mensagem criptografada

Servidor descriptografa

Servidor envia resposta criptografada

Cliente exibe:

Resposta do servidor: ALOU
📚 Conceitos Aplicados

Programação em Redes

Sockets TCP

Criptografia Assimétrica

Criptografia Simétrica

Aritmética Modular

Teste de Primalidade

Medição de desempenho

⚠️ Observações

O número primo utilizado atualmente é pequeno (23) para fins acadêmicos.

Em aplicações reais, números primos possuem centenas ou milhares de bits.

A Cifra de César é usada apenas para fins didáticos.

Em sistemas reais, utiliza-se AES ou outros algoritmos seguros.

🎓 Aplicação Acadêmica

Projeto desenvolvido para estudo de:

Redes de Computadores

Segurança da Informação

Criptografia

Protocolos de troca de chave


---

Se você quiser, posso agora:

- 🔥 Deixar o README em nível mais técnico (com complexidade O(n))
- 📊 Adicionar comparação de desempenho Fast vs Slow
- 📄 Adaptar para entregar como relatório formal
- 🎤 Preparar um roteiro de apresentação para você explicar em sala

Qual próximo passo?
deixe o texto de uma forma que eu precise copiar apenas uma vez no readme do git

Perfeito 👌
Aqui está o README pronto para copiar e colar uma única vez no GitHub, já formatado corretamente em Markdown e sem blocos quebrados.

🔐 TCP Client-Server com Diffie-Hellman e Teste de Primalidade

Este projeto implementa uma comunicação Cliente-Servidor utilizando Sockets TCP em Python, aplicando:

🔐 Troca de chaves com Diffie-Hellman

🔑 Criptografia simétrica com Cifra de César

🧮 Teste de números primos (Fast e Slow)

⏱ Medição de tempo de execução

📌 Objetivo

Simular uma comunicação segura onde:

O número primo p é validado antes do uso

Cliente e servidor executam o algoritmo de Diffie-Hellman

Uma chave simétrica é gerada dinamicamente

A chave é utilizada para criptografar mensagens

O servidor processa a mensagem e envia resposta criptografada

🛠 Tecnologias Utilizadas

Python 3

Biblioteca socket

Biblioteca time

Algoritmo de Diffie-Hellman

Cifra de César

🔐 1️⃣ Teste de Primalidade

Antes de executar o Diffie-Hellman, o número p é testado utilizando dois algoritmos:

Primo Fast

Interrompe a execução assim que encontra um divisor.

Primo Slow

Testa todos os divisores possíveis antes de decidir.

Ambos exibem:

Se o número é primo ou não

Tempo de execução

Isso garante que p atende ao requisito matemático do Diffie-Hellman.

🔑 2️⃣ Diffie-Hellman

O algoritmo permite que duas partes gerem uma chave secreta compartilhada sem enviá-la diretamente pela rede.

Etapas:

Escolha pública de:

p (número primo)

g (base)

Cliente escolhe segredo privado a

Servidor escolhe segredo privado b

Cliente envia:

A = g^a mod p

Servidor envia:

B = g^b mod p

Ambos calculam:

Chave = B^a mod p
Chave = A^b mod p

Resultado: ambos obtêm a mesma chave secreta.

A chave final é ajustada com:

chave % 26

para ser utilizada na Cifra de César.

🔐 3️⃣ Cifra de César

A mensagem é criptografada utilizando deslocamento no alfabeto baseado na chave gerada dinamicamente.

Exemplo com chave = 3:

a → d
b → e
c → f
🔄 Fluxo Completo da Comunicação

Servidor inicia

Número primo p é testado (Fast e Slow)

Cliente conecta

Diffie-Hellman gera chave secreta

Cliente envia mensagem criptografada

Servidor descriptografa

Servidor converte para maiúsculo

Servidor criptografa novamente

Cliente descriptografa e exibe resultado

📂 Estrutura do Projeto
.
├── Simple_tcpServer.py
├── Simple_tcpClient.py
└── README.md
▶️ Como Executar
1️⃣ Inicie o servidor
python Simple_tcpServer.py
2️⃣ Em outro terminal, execute o cliente
python Simple_tcpClient.py
🧪 Exemplo de Execução

Cliente digita:

alou

Fluxo interno:

Chave secreta gerada via Diffie-Hellman

Cliente envia mensagem criptografada

Servidor descriptografa

Servidor envia resposta criptografada

Cliente exibe:

Resposta do servidor: ALOU
📚 Conceitos Aplicados

Programação em Redes

Sockets TCP

Criptografia Assimétrica

Criptografia Simétrica

Aritmética Modular

Teste de Primalidade

Medição de desempenho

⚠️ Observações

O número primo utilizado atualmente é pequeno (23) para fins acadêmicos.

Em aplicações reais, números primos possuem centenas ou milhares de bits.

A Cifra de César é usada apenas para fins didáticos.

Em sistemas reais, utiliza-se AES ou outros algoritmos criptográficos seguros.
