# Este é um algoritmo desenvolvido para realizar a compressão de caracteres repetidos em um texto.
# Exemplo de entrada: OláAAAAAJJJJJJJJJUUUUUUU
# Exemplo de saída: Olá{5A}{9J}{7U}

def compressionRepeated(content):
    encodeContent = ""
    i = 0
    # loop que percorre os caracteres da string
    while i < len(content):
        count = 1
        character = content[i]
        nextIndice = i + 1

        # se o caracter atual for igual ao próximo:
        if nextIndice < len(content) and content[nextIndice] == character:
            # realiza a contagem de caracteres iguais
            while nextIndice < len(content) and content[nextIndice] == character:
                count += 1
                nextIndice += 1
            # atribui a quantidade no novo conjunto de string
            encodeContent += '{' + f'{count}' + f'{character}' + '}'
        else:
            encodeContent += character

        i = nextIndice
    return encodeContent

def decompressionRepeated(content):
    decodeContent = ""
    i = 0
    # 
    while i < len(content):
        count = 1
        character = content[i]
        nextIndice = i + 1 
        if character == '{' and nextIndice < len(content):
            amountRepeated = ''
            try:
                while int(content[nextIndice]) or int(content[nextIndice]) == 0:
                    amountRepeated += content[nextIndice]
                    nextIndice += 1
            except Exception as e:
                noTry = True
            count = 0
            repeatedCharacter = content[nextIndice]
            amountRepeated = int(amountRepeated)
            while count < amountRepeated:
                count += 1
                decodeContent += repeatedCharacter
            nextIndice += 2
        else:
            decodeContent += character
        i = nextIndice
    return decodeContent

print("Olá usuário, este é um código de compressão/descompressão de caracteres repetidos")
print("1. Para realizar a compressão de algum arquivo")
print("2. Para realizar a descompressão de algum arquivo")
choice = input("Opção (1/2): ")

if choice == "1":
    try:
        # input_repeat_characteres.txt
        file = input("Nome do arquivo: ")
        content = open(file, 'r').read()
        encoded = compressionRepeated(content)
        open('response_repeat_characteres.txt', 'w').write(encoded)
        print("Resultado gerado em: response_repeat_characteres.txt")
    except Exception as e:
        print("Erro, arquivo inválido.")
    
elif choice == "2":
    try:
        # response_repeat_characteres.txt
        file = input("Nome do arquivo: ")
        content = open(file, 'r').read()
        encoded = decompressionRepeated(content)
        open('response_decode_repeat_characteres.txt', 'w').write(encoded)
        print("Resultado gerado em: response_decode_repeat_characteres.txt")
    except Exception as e:
        print("Erro, arquivo inválido.")
else:
    print("Opção inválida")
