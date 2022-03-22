produtos = ['iphone 7', 'iphone 8','iphone x','iphone 11','iphone 12','iphone 13','macbook', 'airpods','apple watch']


for comando in produtos:
    item = input('Você deseja excluir, adicionar ou substituir o produto? ')
    item.split()
    item.casefold()
    if item == 'excluir':
        produto = input('Qual produto você deseja excluir? ')
        produto.split()
        produto.casefold()
        if produto in produtos:
            produtos.remove(produto)
            print(f'{produto} foi removido com sucesso!')
            print(produtos)
            continue
        else:
            print('Esse produto não existe na lista!')
            continue

    elif item == 'adicionar':
        novo_produto = input('Qual produto você deseja adicionar? ')
        produtos.append(novo_produto)
        print(f'{novo_produto} adicionado com sucesso!')
        print(produtos)
        continue

    elif item == 'substituir':
        produto = input('Qual produto você deseja substituir? ')
        produto.split()
        produto.casefold()

        if  produto in produtos:
            novo_produto = input('Qual produto você deseja adicionar? ')
            novo_produto.split()
            novo_produto.casefold()
            i = produtos.index(produto)
            produto_removido = produtos.pop(i)
            produtos[i] = novo_produto
            print(f'{novo_produto} foi adicionado com sucesso!')
            print(produtos)
            continue

        else:
            print('Esse produto não existe na lista!')
            continue
    else:
        print('Digite apenas "excluir" ou "substituir"')
        continue
