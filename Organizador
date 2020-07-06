def organizar(diretorio):

    A = []  # Linhas do documento, cada uma vira um elemento de "A".
    B = []  # Base de dados limpa ('@' + user + !).
    C = []  # Posições esperadas para "Foto de ..." (index).

    with open(diretorio, 'r') as f:

        for line in f:
            A.append(line)

        for g in range(0, len(A)*3, 3):
            C.append(g)

        for w in range(0, len(A)):
            aval = A[w]
            if "Foto" in aval:
                if w in C:
                    pass
                else:
                    A.insert(w, "asd")

        for i in range(1, len(A), 3):
            B.append("@" + A[i])

        print(len(B))
    
    with open(diretorio, 'w') as arquivo:
        usuarios = ""
        for usuario in B:
            usuario = usuario[:-1] + "!"
            usuarios += usuario 
        arquivo.write(usuarios[:-1])
    
'''insira em "organizar" o caminho do .txt com os usuarios a organizar'''
organizar("Insira_Aqui")
