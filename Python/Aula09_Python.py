#arquivo = open('teste.txt', 'w') # o W serve para escrever algo dentro do arquivo, porem toda vez que vocÊ escrever algo novo ele substituirá o antigo pelo novo (seria um update)

# arquivo = open('teste.txt', 'a') # o a serve para escrever novas coisas no arquivo, porem sem substituiro o que ja tinha dentro
# arquivo.write('\nMinha segunda escrita')

# arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
    
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()
    
def ler_arquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        texto = arquivo.read()
        print(texto)



if __name__ == '__main__':
    #escrever_arquivo('Primeira linha \n')
    aluno = input('Digite as 4 notas, uma do lado da outra separadas por virgula: \n')
    atualizar_arquivo('notas.txt', aluno )
    #ler_arquivo('teste.txt')