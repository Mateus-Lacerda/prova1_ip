import pandas as pd ## Importando a biblioteca pandas, para trabalhar com dataframes
## Comente sobre o código, explicando-o


def main(): ## Função principal
    
    
    def stock(): ## Função para criar o estoque
        print("Você agora digitará os dados de algumas vendas, para ser feita a criação do arquivo com os dados do seu estoque: ")

        items_matrix = []

        while True: ## Loop para adicionar os dados dos produtos
            product_name, quantity, unit_price = input("Nome do produto: "), int(input("Quantidade em estoque: ")), float(input("Preço unitário: "))
            product_data = [product_name, quantity, unit_price]
            items_matrix.append(product_data)
            stop_point = input("Deseja parar? ").lower().strip()[0]
            if stop_point == 's':
                break
        
        product_dataframe = pd.DataFrame(items_matrix, columns=['Produto', 'Quantidade', 'Preço'])
        product_dataframe.to_csv(r'/home/mateus/Desktop/Estudo/VSCode Projects/Prova1IP/vendas.csv', index=False)
        stock_dataframe = pd.DataFrame([[0,0] for i in range(len(product_dataframe['Produto']))],columns = ['Media','Lucro'])
        stock_dataframe.to_csv(r'/home/mateus/Desktop/Estudo/VSCode Projects/Prova1IP/media_vendas.csv', index=False)

    option = input("Deseja refazer o estoque do zero? ").lower().strip()[0]

    if option == 's': ## Condição para refazer o estoque
        stock()
    

    ## Essa função irá atualizar o estoque com base nas vendas, além de calcular a média diária de vendas e lucro, por produto
    def update_stock():
        product_dataframe = pd.read_csv(r'/home/mateus/Desktop/Estudo/VSCode Projects/Prova1IP/vendas.csv')
        print(f"Estoque atual:\n{product_dataframe}")
        print("Agora, você digitará os dados das vendas de hoje, para a atualização dos dados do estoque: ")
       
        sales_control = pd.DataFrame(pd.read_csv(r'/home/mateus/Desktop/Estudo/VSCode Projects/Prova1IP/media_vendas.csv'),columns=['Media','Lucro'])
        print(sales_control)

        len_new = len(product_dataframe['Produto'])
        len_old = len(sales_control['Media'])

        ## Condicional para aumentar o tamanho do dataframe sales_control, caso sejam adicionados produtos ao arquivo csv media_vendas externamente
        if len_new != len_old:
            new_lines = pd.DataFrame([[0,0] for i in range(len(len_new - len_old))],columns = ['Media','Lucro'])
            pd.concat([sales_control,new_lines])
        
        ## Laço for para atualizar item a item os dados de controle de vendas e lucro
        counter = 0
        for product in product_dataframe['Produto']:
            dayly_sales = int(input(f"Vendas de {product}: "))
            if sales_control['Media'][counter] != 0:
                product_dataframe['Quantidade'][counter] -= dayly_sales
                sales_control['Media'][counter] = (sales_control['Media'][counter] + dayly_sales)/2
                sales_control['Lucro'][counter] = (sales_control['Media'][counter]*product_dataframe['Preço'][counter])
                counter += 1
            else:
                product_dataframe['Quantidade'][counter] -= dayly_sales
                sales_control['Media'][counter] = (sales_control['Media'][counter] + dayly_sales)
                sales_control['Lucro'][counter] = (sales_control['Media'][counter]*product_dataframe['Preço'][counter])
                counter += 1

        sales_control.to_csv(r'/home/mateus/Desktop/Estudo/VSCode Projects/Prova1IP/media_vendas.csv', index=False)

        ## Laço for para mostrar item a item os dados de vendas
        counter = 0
        for product in product_dataframe['Produto']:
            print(f"Produto :{product}\nMédia de vendas: {sales_control['Media'][counter]}\nLucro médio: {sales_control['Lucro'][counter]}")
            counter += 1
        
        
        print(f"Estoque atualizado:\n{product_dataframe}")

        product_dataframe.to_csv(r'/home/mateus/Desktop/Estudo/VSCode Projects/Prova1IP/vendas.csv', index=False)



    option = input("Deseja atualizar o estoque? ").lower().strip()[0]

    if option == 's': ## Condição para atualizar o estoque
        update_stock()


if __name__ == '__main__': ## Condição para rodar o programa
    main()
