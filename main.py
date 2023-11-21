from programaclinicamedica import *

def main():
    atendimento = Atendimento()

    while True:
        print("Escolha uma opção:")
        print("1. Obter senha de atendimento")
        print("2. Chamar paciente para cadastro")
        print("3. Chamar paciente para o consultório")
        print("4. Consultar a posição atual")
        print("5. Painel de atendimento")
        print("6. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            senha = 0
            medico = input("Digite o nome do médico: ")
            nome = input("Digite o nome do paciente: ")
            senha = atendimento.obter_senha(medico, nome)
            print("Senha emitida:", senha)
            
        elif opcao == "2":
            atendimento.chamar_paciente_para_cadastro()
        elif opcao == "3":
            sala = input("Digite o número da sala: ")
            paciente = input("Digite o CPF do paciente: ")
            atendimento.chamar_paciente_para_o_consultorio(sala, paciente)
        elif opcao == "4":
            paciente = input("Digite o CPF do paciente: ")
            print(atendimento.consultar_posição_atual(paciente))
        elif opcao == "5":
            atendimento.painel_de_atendimento()
        elif opcao == "6":
            break

    print("Obrigado por utilizar nosso sistema!")


if __name__ == "__main__":
    main()
