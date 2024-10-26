def bionic_reading(text):
    words = text.split()
    bionic_words = []

    for word in words:
        length = len(word)

        if length <= 3:  # Palavras curtas
            bionic_words.append(word)
        elif 4 <= length <= 6:  # Palavras médias
            bionic_word = f"**{word[:2]}**{word[2:]}"
            bionic_words.append(bionic_word)
        elif 7 <= length <= 12:  # Palavras longas
            bionic_word = f"**{word[:3]}**{word[3:]}"
            bionic_words.append(bionic_word)
        else:  # Palavras muito longas
            bionic_word = f"**{word[:5]}**{word[5:]}"
            bionic_words.append(bionic_word)

    bionic_text = ' '.join(bionic_words)
    return bionic_text

def save_to_markdown(text, filename='output.md'):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def read_from_file(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        return file.read()

# Exemplo de uso
input_filename = 'input.txt'  # Nome do arquivo de entrada
input_text = read_from_file(input_filename)  # Lê o texto do arquivo
bionic_text = bionic_reading(input_text)  # Aplica a formatação

output_filename = 'output.md'  # Nome do arquivo de saída
# Adicionando a marcação de título e a indicação de IA
markdown_output = f"# Bionic Reading\n\n{bionic_text}\n\n*Texto formatado por inteligência artificial sob as instruções de Ezequias Rocha.*"

# Salvando o conteúdo em markdown
save_to_markdown(markdown_output, output_filename)

print(f"O texto formatado em Bionic Reading foi salvo em {output_filename}.")
