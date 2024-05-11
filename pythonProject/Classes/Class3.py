class Funcionario:
    def __init__(self, matricula, nome, numero, email, cpf, rg):
        self.matricula = matricula
        self.nome = nome
        self.numero = numero
        self.email = email
        self.cpf = cpf
        self.rg = rg

class Medico(Funcionario):
    def __init__(self,matricula, nome, numero, email, cpf, rg, crm):
        super().__init__(matricula, nome, numero, email, cpf, rg)
        self.crm = crm
        self.especialidades = []
        self.horario = {}

    def especialidade(self, especialidade, horario):
        self.especialidades.append(especialidade)
        self.horario[especialidade] = horario

    def atende(self, especialidade, horario, dia):
        print(f"Especialidade: {especialidade}, Horário: {horario} Dia: {dia}")


class Enfermeiro(Funcionario):
    def __init__(self, matricula, nome, numero, email, cpf, rg, coren):
        super().__init__(matricula, nome, numero, email, cpf, rg)
        self.coren = coren

medico1 = Medico("120", "Dr.Jeraldo", "21966994340", "al6421797@gmail.com", "964.893.610-27", "42.456.195-5", "0123456789")
medico1.especialidade("Cardiologia", {"Terça": "14:00 - 20:00", "Quarta": "08:00 - 18:00"})
medico1.especialidade("Dermatologia", {"Sexta": "14:30 - 21:00", "Domingo": "08:00 - 12:00"})


enfermeiro = Enfermeiro("530", "Maria Cecília", "21955994240", "mariaciça@gmail.com", "055.243.050-18", "47.976.470-0", "0123456788")

print("Horário de atendimento:")
medico1.atende()