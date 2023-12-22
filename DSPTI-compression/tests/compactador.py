content = ''

content = open('arquivo_a_ser_compactado.txt', 'r').read()

# AAAABBDDDDEEE  Teste
# {4A}{2B}{4D}{3E}{*2}Teste

print(f"Antes: {len(content)}")


def encodeBlankSpaces(content):
    encoded_message = ""
    i = 0
    while i < len(content):
        count = 1
        ch = content[i]
        j = i + 1
        if ch == ' ':
            while j < len(content) and content[j] == ch:
                count += 1
                j += 1
            encoded_message += f'*{count}'
        else:
            encoded_message += ch
        i = j
    return encoded_message

def encodeRepeatedWords(content):
    encoded_message = ""
    counting = 0
    while counting < len(content):
        counting = 1;
        while (s[n] == s[n + 1]):
            counting++, n++

        encoding += to_string(counting) + s[n]
    return encoding

encoded = encodeBlankSpaces(content)

print(f"Depois: {len(encoded)}")

open('arquivo_compactado.txt', 'w').write(encoded)