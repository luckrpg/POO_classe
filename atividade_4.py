class Transacao:
    def __init__(self, nome, data_da_transacao, codigo, transacao, dinheiro =False, tranferiu=False):
        self.nome = nome
        self.data_da_transacao = data_da_transacao
        self.codigo = codigo
        self.dinheiro = dinheiro
        self.tranferiu = tranferiu
        self.transacao = transacao

    def apresentar(self):
        print(f'Olá sou {self.nome}, minha data de nascimento é {self.data_da_transacao}'
              f', meu codigo é {self.codigo}')

        if self.dinheiro:
            print(f'tenho dinheiro  ')
        else:
            print(f'Não tenho dinheiro')

        if self.tranferiu:
            print(f'vou transferir')
        else:
            print(f'Não vou transferir')

    def estudar(self):
        if not self.dinheiro:
            self.dinheiro = True
            print(f'{self.nome} começou a estudar')
        elif self.tranferiu and self.tranferiu:
            self.transacao += 1000
            print(
                f"{self.nome} "
                f" começou a estudar e aumentou seu salario para "
                f"{self.transacao:.2f}"
            )
        else:
            print(f'{self.nome} ja esta estudando')

    def transferiu(self):
        if not self.tranferiu:
            self.tranferiu = True
            self.transacao += 100
            print(f'{self.nome} transferido com sucesso !')
        else:
            print(f'{self.nome} ja transferido  !')

class Recebimento_financeiro(Transacao):
    def __init__(self, nome, data_da_transacao, registro, transacao=0,
                 dinheiro=False, tranferiu=False):
        super().__init__(nome, data_da_transacao, registro, dinheiro, tranferiu)
        self.tem_dinheiro = True
        self.recebeu = True
        self.transferiu_ou_nao = False

    def apresentar(self):
        print(f'Opa eae? {self.nome}, minha data de nascimento é {self.data_da_transacao}'
              f', meu codigo é {self.codigo}')

        if self.tem_dinheiro:
            print(f'O {self.nome} tem dinheiro')
        else:
            print(f'O {self.nome} não tem dinheiro')

        if self.recebeu:
            print(f'O {self.nome} recebeu a transacao  ')
        else:

            print(f'O {self.nome} nao recebeu a transacao')

        if self.transferiu_ou_nao:
            print(f'O {self.nome} transferiu')
        else:
            print(f'O {self.nome} nao transferiu')

    def ressebeu_ou_nao(self):
        if not self.fome:
            print(' funcionou')
        else:
            self.fome = False
            self.chorando = False
            print(f'{self.nome} nao funcionou')
            print('funcionou')

    def dormir(self):
        if not self.fome:
            self.dormindo = True
            print('bebe foi dormir')
        else:
            print('bebe está com fome não pode dormir')



print('-_-' * 20)
p1 = Transacao("Lucas", "03/07/2021", "15553",1200,True, True)
p1.apresentar()
print('-_-' * 20)
b1 = Recebimento_financeiro('caio','24/07/2024', '23451')
b1.apresentar()
print('-_-' * 20)