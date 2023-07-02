import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = {'idade': [25, 32, 34, 45, 22, 65],
        'salario': [5000, 6400, 7000, 9800, 4500,15000 ],
        'publico':['M','F','F','M','M','F'],
        'produtos':['ALL','BOLSAS','SAPATOS',' ALL',' ALL','ACESSÓRIOS'],
        'comprou': [0, 1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)
## Tratamento dos dados, para que IA possa utilizá-los

data_2 = data

## Com dois laços for, eu troquei os dados originais do dataframe por valores numéricos correspondentes
counter = 0 
for item in data['publico']:
    if item == 'F':
        data_2['publico'][counter] = 1
    else:
        data_2['publico'][counter] = 0
    counter += 1

counter = 0 
for item in data['produtos']:
    if data_2['produtos'][counter] == 'BOLSAS':
        data_2['produtos'][counter] = 1
    elif data_2['produtos'][counter] == 'SAPATOS':
        data_2['produtos'][counter] = 2
    elif data_2['produtos'][counter] == 'ACESSÓRIOS' or data_2['produtos'][counter] == 'ACESSORIOS':
        data_2['produtos'][counter] = 3
    else:
        data_2['produtos'][counter] = 0
    
    counter += 1 


df_2 = pd.DataFrame(data_2)


def main(): ## Função principal
    alvo = input("Escolha o público desejado: ").strip().upper()[0] #
    
    if alvo == 'F':
        publico = "feminino"
    else: 
        publico = "masculino"

    soma = 0
    divisor = 0

    for i in range(len(df['publico'])): ## Loop para adicionar os salários do público escolhido a uma variável
        if df['publico'][i] == alvo:
            soma += df['salario'][i]
            divisor += 1

    media = soma/divisor ## Cálculo da média salarial do público escolhido

    print(f"Média salarial do público {publico}: R${media:.2f}")
    
    stop_point = input("Deseja calcular outra média? ").strip().lower()[0]
    if stop_point == 's':
        main()
    
    ## Aqui o dataset foi separado em dois, um para treino e outro para teste
    X = df_2.drop(columns = 'comprou')
    Y = df_2['comprou']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

    ## Aqui foi criado o classificador, que foi treinado com os dados de treino, para calcular a probabilidade de, com os dados fonecidos,
    ## o cliente comprar ou não o produto.
    rfc = RandomForestClassifier(max_depth=20, random_state=42)
    rfc = rfc.fit(X_train,Y_train)

    ## Aqui são digitados os dados do cliente, para que a IA possa sugerir se deve, ou não, oferecer o produto
    print("Agora você digitará os dados de um cliente, e a IA irá sugerir se você deve, ou não, oferecer seu produto. ")
    client_data = np.array([int(input("Idade: ")),int(input("Salário: ")), input("Sexo: ").strip().upper()[0], input("Produto: ").upper() ])
    
    ## Tratamento dos dados individuais, para que a IA possa utilizá-los
    if client_data[2] == 'F':
        client_data[2] = 1
    else:
        client_data[2] = 0
    
    if client_data[3] == 'BOLSAS':
        client_data[3] = 1
    elif client_data[3] == 'SAPATOS':
        client_data[3] = 2
    elif client_data[3] == 'ACESSÓRIOS' or client_data[3] == 'ACESSORIOS':
        client_data[3] = 3
    else:
        client_data[3] = 0
    
    client_dataframe = pd.DataFrame([client_data],columns=['idade','salario','publico','produtos'])

    ## Aqui é usada a função predict_proba, que mostra a probabilidade de cada classe ocorrer, com base nos dados apresentados
    probabilities = rfc.predict_proba(client_dataframe)

    ## Por fim, uma mensagem é data ao usuário, para oferecer, ou não, o produto
    if probabilities[0][0] <= 0.5:
        print(f"Ofereça o produto, a chance de um cliente como esse comprá-lo é de {probabilities[0][1]*100:.2f}%!")
    else:
        print(f"Não ofereça o produto, a chance de um cliente como esse não comprá-lo é de {probabilities[0][0]*100:.2f}%!") 
    


    print("""
    Do storytelling de dados:
    No fim, os dados fornecidos foram muito insuficientes, pois o parâmetro que se mostra mais importante para a análise 
    é o sexo, em primeiro momento, sendo assim, após ter sido feita a análise final utilizando-se apenas os outros fatores, 
    percebi uma maior complexidade na análise. entretanto, o contexto também inflencia em como os dados devem ser interpretados, 
    talvez os dados fornecidos sejam de uma loja de roupas femininias, e os homens que entraram e não compraram nada, tenham entrado por engano.
    """)


if __name__ == '__main__': ## Condição para rodar o programa
    main()
