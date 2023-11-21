class Paciente:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class No:
    def __init__(self, paciente, proximo=None):
        self.paciente = paciente
        self.proximo = proximo

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, paciente):
        novo_no = No(paciente)

        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def remover(self):
        if self.inicio is None:
            return None

        paciente = self.inicio.paciente
        self.inicio = self.inicio.proximo

        return paciente

class Sala:
    def __init__(self, numero):
        self.numero = numero
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def remover_paciente(self, paciente):
        self.pacientes.remove(paciente)

class Atendimento:
    def __init__(self):
        self.fila = Fila()
        self.salas = {}

    def obter_senha(self, medico, nome):
        paciente = Paciente(nome, None, None)
        self.fila.inserir(paciente)

        # Gera a senha
        numero_senha = 1
        senha = "N0" + str(numero_senha)

        # Incrementa o número da senha
        numero_senha += 1

        return senha

    def chamar_paciente_para_cadastro(self):
        paciente = self.fila.remover()
        paciente.nome = input("Digite o nome do paciente: ")
        paciente.cpf = input("Digite o CPF do paciente: ")
        paciente.data_nascimento = input("Digite a data de nascimento do paciente (dd/mm/yyyy): ")

    def chamar_paciente_para_o_consultorio(self, sala, paciente):
        self.salas[sala].adicionar_paciente(paciente)

    def consultar_posição_atual(self, paciente):
        if paciente.cpf in self.fila.inicio.paciente.cpf:
            return "Em fila"
        elif paciente.cpf in self.salas:
            return "Na sala " + str(self.salas[paciente.cpf])
        else:
            return "Atendido"

    def painel_de_atendimento(self):
        print("     Painel de Atendimento")
        print("Cadastro     Consultório Médico")
        print("============ ======================")

        # Imprime os pacientes na fila de cadastro
        for paciente in iter(self.fila):
            print("   ", paciente.cpf, end=" ")

        # Imprime os pacientes nos consultórios
        for sala in self.salas:
            sala_pacientes = self.salas[sala].pacientes
            for paciente in iter(sala_pacientes):
                print(" > ", paciente.cpf, " ", paciente.nome)

