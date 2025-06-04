# ------------------ Seção de Importações ------------------
import customtkinter as ctk
import os

# ------------------ Seção de Configuração do Tema ------------------
ctk.set_appearance_mode("light")

# ------------------ Seção de Configuração da Janela ------------------
app = ctk.CTk()
app.title("Conversor Binário-Decimal")
app.geometry("600x600")
app.configure(bg="#037bfc")
app.resizable(False, False)
app.grid_columnconfigure(0, weight=1)

# ------------------ Seção de Configuração da Fonte ------------------
font_style = ctk.CTkFont( 
    family="Arial",
    weight="normal",
    underline=0
)

# ------------------ Seção de Configuração do Icone da Janela ------------------
caminho_imagem = os.path.join(os.path.dirname(__file__), "logo.ico")
app.iconbitmap(caminho_imagem)

# Definição da variável de escolha (bin_to_dec ou dec_to_bin)
escolha = ctk.StringVar(value="bin_to_dec")

# ------------------ Seção de Funções ------------------


# ------------------ Função de Limpeza da Entrada e do Resultado ------------------
# Limpa a entrada e o resultado e muda a instrução de acordo com a opção escolhida
def limpar_entrada():
    if escolha.get() == 'bin_to_dec':
        instrucao.configure(text="Digite um número binário")
    else:
        instrucao.configure(text="Digite um número decimal")

    if (entrada.get() == "" and resultado.cget("text") == ""):
        return
    entrada.delete(0, ctk.END)
    resultado.configure(text="")
    # Muda o foco para o container geral para aparecer o placeholder da entrada
    app.focus_set()

# ------------------ Função de Verificação de Opção e Formatação dos Botões ------------------
# Verifica qual opção de escolha está selecionada e a formatação dos botões
def trocar_opcao():
    if escolha.get() == 'bin_to_dec':
        btn_opcao_1.configure(
            fg_color="#b562d1", text_color="white", border_color="#801aa3", 
            border_width=2.5, hover_color="#ca72e8"
        )
        btn_opcao_2.configure(
            fg_color="#3b8ed0", text_color="white", border_width=0, 
            hover_color="#439de6"
        )
    else:
        btn_opcao_1.configure(
            fg_color="#3b8ed0", text_color="white", border_width=0, 
            hover_color="#439de6"
        )
        btn_opcao_2.configure(
            fg_color="#b562d1", text_color="white", border_color="#801aa3",
            border_width=2.5, hover_color="#ca72e8"
        )

# ------------------ Função de Alteração de Opção ------------------
# Altera a opção de escolha, limpa os dados e muda a instrução
def set_opcao1():
    escolha.set('bin_to_dec')
    trocar_opcao()
    limpar_entrada()
    instrucao.configure(text="Digite um número binário")

# ------------------ Função de Alteração de Opção ------------------
# Altera a opção de escolha, limpa os dados e muda a instrução
def set_opcao2():
    escolha.set('dec_to_bin')
    trocar_opcao()
    limpar_entrada()
    instrucao.configure(text="Digite um número decimal")

# ------------------ Função de Verificação e Conversão de Binário para Decimal ------------------
# Converte um número binário para decimal fazendo as devidas verificações
def binario_para_decimal(bin_str):

    # Variável de controle para sinal de negativo
    negativo = False
    # Mensagem de erro
    msgError = "Entrada inválida para binário. Use apenas números inteiros e decimais que contenham 0 ou 1."

    # Verifica se a string bin_str contém um sinal de negativo
    if bin_str.startswith("-"):
        negativo = True
        bin_str = bin_str[1:]

    # Laço de repetição que percorre cada caractere (char) da string bin_str
    for char in bin_str:
        # Verifica se o caractere atual é diferente de 0, 1 ou ponto e retorna uma mensagem de erro
        if char != "0" and char != "1" and char != ".":
            return msgError
    
    # Verifica se a string bin_str não contém um ponto
    if "." not in bin_str:
        valor = int(bin_str, 2)
        return str(-valor if negativo else valor)

    # Parte a string bin_str em duas partes separadas pelo ponto
    parte_inteira, parte_decimal = bin_str.split(".")

    # Converte a parte inteira para um valor decimal
    valor_inteiro = int(parte_inteira, 2)
    # Transforma cada dígito/bit da parte fracionária em um valor decimal e soma-os
    valor_fracionado = sum(
        int(bit) / (2 ** i) for i, bit in enumerate(parte_decimal, start=1)
    )

    # Soma o valor inteiro com o valor fracionado para obter o resultado final
    valor = valor_inteiro + valor_fracionado

    # Retorna o valor convertido para string com o sinal de negativo se necessário
    return str(-valor if negativo else valor)

# ------------------ Função de Verificação e Conversão de Decimal para Binário ------------------
# Converte um número decimal para binário fazendo as devidas verificações
def decimal_para_binario(num_str):
    # Verifica se a string num_str não contém um ponto
    if "." not in num_str:
        # Converte o valor decimal para binário e retira o prefixo "0b"
        return str(bin(int(num_str)).replace("0b", ""))

    # Parte a string num_str em duas partes separadas pelo ponto
    parte_inteira, parte_decimal = num_str.split(".")
    # Converte a parte inteira para binário e retira o prefixo "0b"
    valor_inteiro = bin(int(parte_inteira)).replace("0b", "")

    # Converte a parte fracionária para float
    parte_fracionada = float("0." + parte_decimal)
    # String que armazenará o valor binário final
    valor_fracionario = ""

    # Laço de repetição converte até 10 dígitos/bits
    for i in range(10):
        # Multiplica o valor fracionário por 2
        parte_fracionada *= 2
        # A parte inteira do resultado da multiplicação é guardado como bit
        bit = int(parte_fracionada)
        # Adiciona o valor do bit ao valor fracionário
        valor_fracionario += str(bit)
        # Subtrai o valor do bit do valor fracionário
        parte_fracionada -= bit

        # Verifica se a parte fracionária chegou a zero e para
        if parte_fracionada == 0:
            break

    # Retorna a parte inteira e a parte fracionada convertidas para binário
    return f"{valor_inteiro}.{valor_fracionario}"

# ------------------ Função de Exibição de Resultado ------------------
# Exibe o resultado da conversão de acordo com a opção escolhida
def converter():
    entrada_texto = entrada.get().replace(",", ".").strip()
    tipo = escolha.get()
    cor = "#3b8ed0"

    try:
        # Verifica se a entrada contém mais de um ponto
        if entrada_texto.count(".") > 1:
            resultado_texto = "Entrada inválida. Utilize apenas um ponto ou vírgula para a parte fracionária."
            cor = "#d03b3b"
        # Verifica o tipo de conversão e executa a função correspondente
        elif tipo == 'bin_to_dec':
            # Executa a conversão de binário para decimal
            resultado_texto = binario_para_decimal(entrada_texto)
            # Verifica se o resultado da conversão é uma mensagem de erro
            if resultado_texto == "Entrada inválida para binário. Use apenas números inteiros e decimais que contenham 0 ou 1.":
                cor = "#d03b3b"
        else:
            # Executa a conversão de decimal para binário 
            resultado_texto = decimal_para_binario(entrada_texto)

        # Altera o valor do Label de resultado de acordo com o resultado da conversão
        resultado_label.configure(text=str(resultado_texto), text_color=cor)

    # Captura qualquer exceção e exibe uma mensagem de erro no Label
    except:
        # Define a mensagem de erro de acordo com o tipo de conversão
        mensagem_erro = "Binário inválido" if tipo == 'bin_to_dec' else "Decimal inválido"
        # Altera o valor do Label de resultado de acordo com a mensagem de erro
        resultado_label.configure(text=mensagem_erro, text_color="#d03b3b")

# ------------------ Seção de Criação de Widgets ------------------

frame_botoes = ctk.CTkFrame(app, width=400, height=400, corner_radius=20)

btn_opcao_1 = ctk.CTkButton(
    frame_botoes, text="Binário para Decimal", command=set_opcao1,
    width=200, height=40, corner_radius=20, fg_color="#b562d1", 
    hover_color="#ca72e8", text_color="white", border_color="#801aa3", 
    border_width=2.5, font=(font_style, 18.4)
)

btn_opcao_2 = ctk.CTkButton(
    frame_botoes, text="Decimal para Binário", command=set_opcao2, 
    width=200, height=40, corner_radius=20, text_color="white", 
    fg_color="#3b8ed0", hover_color="#439de6", font=(font_style, 18.4)
)

instrucao = ctk.CTkLabel(
    app, text="Digite um número binário", text_color="black", 
    font=(font_style, 20, "bold")
)

frame_entrada = ctk.CTkFrame(
    app, width=400, height=400, corner_radius=20, 
    fg_color="transparent"
)

entrada = ctk.CTkEntry(
    frame_entrada, width=300, height=40, corner_radius=10,
    font=(font_style, 18), placeholder_text="Ex.: 10101",
)

btn_limpar = ctk.CTkButton(
    frame_entrada, text="❌", command=limpar_entrada,
    width=24, height=32, corner_radius=8, fg_color="#d03b3b", 
    hover_color="#f05151", text_color="white"
)

btn_converter = ctk.CTkButton(
    app, text="Converter", command=converter,
    width=200, height=40, corner_radius=20, fg_color="#3b8ed0", 
    hover_color="#439de6", text_color="white", 
    font=(font_style, 18)
)

frame_resultado = ctk.CTkScrollableFrame(
    app, width=500, height=10, corner_radius=20, fg_color="white",
    scrollbar_button_color="#beb4c2", label_anchor="center",
    scrollbar_button_hover_color="#a95ac4"
)

resultado = ctk.CTkLabel(
    frame_resultado, text="", text_color="#3b8ed0",
    font=(font_style, 24, "bold"), anchor="center", width=500, 
    height=50, wraplength=450
)

titulo_resultado = ctk.CTkLabel(
    app, text="Resultado", text_color="black", 
    font=(font_style, 18, "bold"), anchor="center",
    fg_color="white", width=250, corner_radius = 10
)

# ------------------ Seção de Organização de Widgets ------------------

# Adiciona o frame dos botões na tela
frame_botoes.grid(column=0, row=0, pady=20)

# Adiciona o primeiro botão de escolha na tela
btn_opcao_1.grid(row=0, column=0, pady=10, padx=10)

# Adiciona o segundo botão de escolha na tela
btn_opcao_2.grid(row=0, column=1, pady=10, padx=10)

# Adiciona a Label de instrução na tela
instrucao.grid(pady=10)

# Adiciona o frame de entrada na tela
frame_entrada.grid()

# Adiciona a entrada na tela
entrada.grid(pady=5, column=0, row=1)

# Aciona a função converter ao pressionar enter
entrada.bind("<Return>", lambda event: converter())

# Adiciona o botão de limpar na tela
btn_limpar.grid(pady=5, padx=10, column=1, row=1)

# Adiciona o botão de converter na tela
btn_converter.grid(pady=24)

# Adiciona a Label de Título do frame de Resultado na tela
titulo_resultado.grid(ipady=5, ipadx=10)

# Adiciona o frame de Resultado na tela
frame_resultado.grid(ipadx=5)

# Adiciona o Label do Resultado na tela
resultado.grid(ipady=10)

# Executa a janela/aplicação
app.mainloop()