def main():
    vel = (1570+1450)/2 ## Aqui eu defini uma variável com o valor da velocidade média do som na água
    print("Vamos calcular a distância de você até o objeto! ")
    time = float(input("Entre com o tempo registrado, em segundos: "))
    print(f"Distância calculada: {time*vel/2}m") ##Calculo do resultado dentro de uma f-string
    
    stop_point = input("Deseja calcular outra? ").strip().lower()[0] ## Condição para parar o programa
    if stop_point == 's':
        main()


if __name__ == '__main__': ## Condição para rodar o programa
    main()
