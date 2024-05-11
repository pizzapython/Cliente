class Funcionario:
    def __init__(self, matricula, nome, telefone, email, cpf, rg):
        self.matricula = matricula
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.rg = rg

class Medico(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, crm):
        super().__init__(matricula, nome, telefone, email, cpf, rg)
        self.crm = crm
        self.especialidades = []
        self.horarios = {}

    def adicionar_especialidade(self, especialidade, horarios):
        self.especialidades.append(especialidade)
        self.horarios[especialidade] = horarios

    def atende(self):
        for especialidade, horarios in self.horarios.items():
            print(f"Especialidade: {especialidade}")
            print("Horários de atendimento:")
            for dia, horario in horarios.items():
                print(f"Dia: {dia}, Horário: {horario}")

class Enfermeiro(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, coren):
        super().__init__(matricula, nome, telefone, email, cpf, rg)
        self.coren = coren

# Criando objetos
medico1 = Medico(matricula="123", nome="Dr. João", telefone="123456789", email="joao@example.com", cpf="12345678901", rg="1234567", crm="CRM123")
medico1.adicionar_especialidade("Cardiologia", {"Segunda": "08:00 - 12:00", "Quarta": "14:00 - 18:00"})
medico1.adicionar_especialidade("Dermatologia", {"Terça": "10:00 - 14:00", "Quinta": "08:00 - 12:00"})

enfermeiro1 = Enfermeiro(matricula="456", nome="Enf. Maria", telefone="987654321", email="maria@example.com", cpf="98765432109", rg="7654321", coren="COREN456")

# Testando o método atende
print("Horários de atendimento do médico:")
medico1.atende()