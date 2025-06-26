print("Bem-vindo ao gerenciador de jogos")

class Jogo:
    def __init__(self, titulo, genero, classificacao, desenvolvedora):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.desenvolvedora = desenvolvedora

    def getTitulo(self):
        return self.titulo

    def getGenero(self):
        return self.genero

    def getClassificacao(self):
        return self.classificacao

    def getDesenvolvedora(self):
        return self.desenvolvedora


class Personagem:
    def __init__(self, alterego, habilidade, item):
        self.alterego = alterego
        self.habilidade = habilidade
        self.item = item

    def getAlterego(self):
        return self.alterego

    def getHabilidade(self):
        return self.habilidade

    def getItem(self):
        return self.item

    def jogar(self, jogo):
        print(f"{self.getAlterego()} está jogando {jogo.getTitulo()}.")

    def ganharPontos(self, pontos):
        print(f"{self.getAlterego()} ganhou {pontos} pontos.")
        return pontos


class Jogador(Personagem):
    def __init__(self, nome, alterego, habilidades, inventario, dinheiro):
        super().__init__(alterego, habilidades, inventario)
        self.nome = nome
        self.pontuacao = 0
        self.dinheiro = dinheiro

    def getNome(self):
        return self.nome

    def getPontuacao(self):
        return self.pontuacao

    def getDinheiro(self):
        return self.dinheiro

    def adicionarDinheiro(self, valor):
        self.dinheiro += valor

    def exibirInfo(self):
        print(f"Nome do Jogador: {self.nome}")
        print(f"Pontuação: {self.pontuacao}")
        print(f"Dinheiro: {self.dinheiro}")
        print(f"Personagem: {self.getAlterego()}")
        print(f"Habilidades: {', '.join(self.getHabilidade())}")
        print(f"Inventário: {', '.join(self.getItem())}")


class NPC(Personagem):
    def __init__(self, nivel, alterego, habilidades, recompensa_dinheiro):
        super().__init__(alterego, habilidades, [])
        self.nivel = nivel
        self.recompensa_dinheiro = recompensa_dinheiro

    def interagir(self, jogador):
        print(f"{self.getAlterego()}, um NPC de nível {self.nivel}, apareceu!")
        print(f"{jogador.getNome()} está interagindo com o NPC...")

        # Solicitar ao jogador a quantidade de pontos ganhos
        pontos_ganhos = int(input("Digite a quantidade de pontos que você ganhará ao derrotar o NPC: "))

        jogador.ganharPontos(pontos_ganhos)

        print(f"{self.getAlterego()} foi derrotado por {jogador.getNome()}!")
        jogador.adicionarDinheiro(self.recompensa_dinheiro)
        print(f"{jogador.getNome()} recebeu {self.recompensa_dinheiro} de dinheiro.")


class Loja:
    def __init__(self):
        self.estoque = {}

    def adicionarItem(self, genero, item):
        if genero not in self.estoque:
            self.estoque[genero] = []
        self.estoque[genero].append(item)

    def exibirItens(self, genero):
        if genero in self.estoque:
            print(f"Itens disponíveis na loja para o gênero {genero}:")
            for item in self.estoque[genero]:
                print(f"- {item}")
        else:
            print("Loja não oferece itens para este gênero.")

    def comprarItem(self, jogador, item, genero):
        if genero in self.estoque and item in self.estoque[genero]:
            if jogador.getDinheiro() >= 10:  # Considerando que cada item custa 10 unidades de dinheiro
                jogador.getItem().append(item)
                jogador.adicionarDinheiro(-10)
                print(f"{jogador.getNome()} comprou {item} por 10 de dinheiro!")
            else:
                print(f"{jogador.getNome()} não tem dinheiro suficiente para comprar {item}.")
        else:
            print("Item não disponível na loja para este gênero.")


class Partida:
    def __init__(self, jogo):
        self.jogo = jogo
        self.jogadores = []

    def adicionarJogador(self, jogador):
        self.jogadores.append(jogador)

    def iniciar(self):
        print(f"A partida do jogo {self.jogo.getTitulo()} está iniciando.")

    def encerrar(self):
        print(f"A partida do jogo {self.jogo.getTitulo()} está encerrando.")


# informações sobre o jogo
titulo_jogo = input("Digite o título do jogo: ")
genero_jogo = input("Digite o gênero do jogo: ")
classificacao_jogo = input("Digite a classificação indicativa do jogo: ")
desenvolvedora_jogo = input("Digite a desenvolvedora do jogo: ")
jogo1 = Jogo(titulo_jogo, genero_jogo, classificacao_jogo, desenvolvedora_jogo)

# criação de jogadores
num_jogadores = int(input("Quantos jogadores deseja criar? "))
jogadores = []
for _ in range(num_jogadores):
    print("\n- Novo jogador -\n")
    nome_jogador = input("Digite o nome do Jogador: ")
    alterego_jogador = input("Digite o alterego do personagem: ")
    habilidades_jogador = []  # lista
    qnt_hab = int(input("Quantas habilidades o personagem tem? "))
    for _ in range(qnt_hab):
        habilidade = input("Digite uma habilidade do personagem: ")
        habilidades_jogador.append(habilidade)
    inventario_jogador = []  # lista
    qnt_item = int(input("Quantos itens o jogador tem no inventário? "))
    for _ in range(qnt_item):
        item = input("Digite um item do inventário: ")
        inventario_jogador.append(item)
    dinheiro_jogador = int(input("Digite a quantidade inicial de dinheiro do jogador: "))
    jogador = Jogador(nome_jogador, alterego_jogador, habilidades_jogador, inventario_jogador, dinheiro_jogador)
    jogadores.append(jogador)
    print("-" * 30)

# criação de NPCs
npcs = []
num_npcs = int(input("Quantos NPCs deseja criar? "))
for _ in range(num_npcs):
    print("\n- Novo NPC -\n")
    nivel_npc = int(input("Digite o nível do NPC: "))
    alterego_npc = input("Digite o alterego do NPC: ")
    habilidades_npc = []  # lista
    qnt_hab_npc = int(input("Quantas habilidades o NPC tem? "))
    for _ in range(qnt_hab_npc):
        habilidade_npc = input("Digite uma habilidade do NPC: ")
        habilidades_npc.append(habilidade_npc)
    recompensa_dinheiro_npc = int(input("Digite a recompensa de dinheiro por derrotar o NPC: "))
    npc = NPC(nivel_npc, alterego_npc, habilidades_npc, recompensa_dinheiro_npc)
    npcs.append(npc)
    print("-" * 30)

# criação da loja
loja = Loja()
print("\n- Configurando a Loja -\n")
num_itens_loja = int(input("Quantos itens deseja adicionar na loja? "))
for _ in range(num_itens_loja):
    print("\n- Novo Item na Loja -\n")
    genero_item_loja = input("Digite o gênero do item: ")
    item_loja = input("Digite o nome do item: ")
    loja.adicionarItem(genero_item_loja, item_loja)

# associação de jogadores em uma partida
partida = Partida(jogo1)
for jogador in jogadores:
    partida.adicionarJogador(jogador)

# simulação de partida
print("\nIniciando a partida...")
partida.iniciar()
for jogador in partida.jogadores:
    jogador.jogar(jogo1)
    jogador.exibirInfo()

    # Interagindo com NPCs
    for npc in npcs:
        npc.interagir(jogador)

    # Visitando a loja
    print("\nVisitando a Loja...")
    loja_genero = input("Digite o gênero para ver os itens disponíveis na loja: ")
    loja.exibirItens(loja_genero)
    item_compra = input("Digite o nome do item que deseja comprar na loja: ")
    loja.comprarItem(jogador, item_compra, loja_genero)

print("\nEncerrando a partida...")
partida.encerrar()
