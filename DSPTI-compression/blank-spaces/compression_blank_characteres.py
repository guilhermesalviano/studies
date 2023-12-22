# Este é um algoritmo desenvolvido para realizar a compressão de espaços em branco de um texto.
# Exemplo de entrada: Teste:     Olá.
# Exemplo de saída: Teste:{*5}Olá.

# Realizar a compressão
def compressionBlanks(content):
    encodeContent = ""
    i = 0

    # loop que percorre os caracteres da string
    while i < len(content):
        count = 1
        character = content[i]
        nextIndice = i + 1

        # se o caracter atual for um espaço em branco: 
        if character == ' ':
            # realiza a contagem de caracteres em branco
            while nextIndice < len(content) and content[nextIndice] == character:
                count += 1
                nextIndice += 1
            # atribui a quantidade no novo conjunto de string
            encodeContent += '{'+f'*{count}'+'}'
        else:
            encodeContent += character

        i = nextIndice
    return encodeContent

# Realizar a descompressão
def decompressionBlanks(content):
    decodeContent = ''
    i = 0
    while i < len(content):
        character = content[i]
        nextIndice = i + 1

        if character == '{' and nextIndice < len(content) and content[nextIndice] == '*':
            amountBlankSpace = ''
            nextIndice += 1
            while content[nextIndice] != '}':
                amountBlankSpace += content[nextIndice]
                nextIndice += 1
            amountBlankSpace = int(amountBlankSpace)
            count = 0
            while count < amountBlankSpace:
                count += 1
                decodeContent += ' '
            nextIndice += 1
        else:
            decodeContent += character
        i = nextIndice
    return decodeContent
    

print("Olá usuário, este é um código de compressão/descompressão de caracteres em branco")
print("1. Para realizar a compressão de algum arquivo")
print("2. Para realizar a descompressão de algum arquivo")
choice = input("Opção (1/2): ")

if choice == "1":
    try:
        # input_blank_spaces.txt
        file = input("Nome do arquivo: ")
        content = open(file, 'r').read()
        encoded = compressionBlanks(content)
        open('response_blank_spaces.txt', 'w').write(encoded)
        print("Resultado gerado em: response_blank_spaces.txt")
    except Exception as e:
        print("Erro, arquivo inválido.")
    
elif choice == "2":
    try:
        # response_blank_spaces.txt
        file = input("Nome do arquivo: ")
        content = open(file, 'r').read()
        encoded = decompressionBlanks(content)
        open('response_decode_blank_spaces.txt', 'w').write(encoded)
        print("Resultado gerado em: response_decode_blank_spaces.txt")
    except Exception as e:
        print("Erro, arquivo inválido.")
else:
    print("Opção inválida")
