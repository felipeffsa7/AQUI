
class Matematica():
    def __init__(self, nome, idade, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

    def caracteristicas(self):
        print("O professor " + self.nome.title() + " possui " +
              str(self.idade) + " anos e ele é " + self.nacionalidade.title())

    def soma(self, primeiro, segundo):
        somatoria = primeiro + segundo
        print("A soma entre os numeros " + str(primeiro) +
              " e " + str(segundo) + " é " + str(somatoria))
        return somatoria

    def subtraçao(self, primeiro, segundo):
        sub = primeiro - segundo
        print(sub)


professor_1 = Matematica("jailson", 34, "brasileiro")
sn_prof_1 = professor_1.soma(14, 35)
print("A soma aqui deu: " + str(sn_prof_1))

professor_1.subtraçao(17, 5)
professor_1.caracteristicas()
print("O professor " + str(professor_1.idade))
print(professor_1.nacionalidade)
