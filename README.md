# 🔁 Conversor Binário-Decimal em Python

Este projeto é uma **atividade prática da disciplina de Princípios de Programação**, cujo objetivo é exercitar a lógica de programação com Python, desenvolver habilidades com manipulação numérica e praticar a criação de interfaces gráficas com a biblioteca **Tkinter**, porém dei preferência por utilizar a **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)**, que é derivada do Tkinter, pelo fato de proporcionar mais opções de customização de elementos e da interface.

---

## 🧠 Objetivos

- Praticar a conversão entre os sistemas **binário e decimal** (com suporte a parte fracionária).
- Aplicar conceitos como:
  - Funções
  - Condicionais
  - Manipulação de strings e números
  - Controle de exceções
- Desenvolver uma **interface gráfica interativa** com Python.

---

## 🖼️ Interface

A aplicação tem uma interface simples, intuitiva e funcional construída com CustomTkinter, com suporte a:

- Entrada de dados binários e decimais
- Conversão de números com **parte inteira e parte fracionária (decimal)**
- Tratamento de erros e mensagens de validação
- Troca de modo de conversão com apenas um clique

<br>

![preview da interface](https://github.com/user-attachments/assets/4dea3839-0d0b-41cc-afcb-af39c46e6f36)


---

## 🚀 Tecnologias utilizadas

- **Python 3.10+**
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** — para interface gráfica moderna

---

## ⚙️ Como executar

1. Clone o repositório:

```bash
   git clone https://github.com/BruCamps/Conversor-Binario-Decimal.git
```
2. Instale as dependências:

```bash
  pip install customtkinter
```

3. Execute o programa:

```bash
  python conversor.py
```

## 🧪 Exemplos de uso

### Binário para decimal:

```python
  # Entrada: 101,11 -> A vírgula é convertida em ponto para as conversões
  # Saída: 5.75
```

### Decimal para binário:

```python
  # Entrada: 12.625
  # Saída: 1100.101
```


## ⚠️ Regras de validação
- Somente um único separador decimal (. ou ,) é aceito.
- Números binários devem conter apenas 0, 1, e opcionalmente ..
- Números decimais podem conter qualquer dígito.

## 📌 Observações
- Este projeto foi desenvolvido exclusivamente para fins acadêmicos e de aprendizado.
- Ele não tem como foco precisão científica para grandes casas decimais ou suporte a notação científica.
- O conversor fracionário é limitado a 10 dígitos binários na parte decimal para evitar loops infinitos.

---

Feito com 💜 por Bru

