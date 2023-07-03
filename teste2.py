import rarfile

# Abrir o arquivo .rar
rar = rarfile.RarFile('arquivo.rar')

# Listar o conteúdo dentro do arquivo .rar
conteudo = rar.namelist()

# Exibir o conteúdo
for item in conteudo:
    print(item)

# Extrair todos os arquivos do arquivo .rar
rar.extractall()

# Fechar o arquivo .rar
rar.close()
