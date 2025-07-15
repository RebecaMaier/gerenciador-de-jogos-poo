# 🎮 Gerenciador de Jogos em Python

Este projeto é um sistema interativo em Python onde é possível criar **jogos, jogadores, NPCs**, interagir com uma **loja de itens**, e **simular uma partida** com diferentes elementos de um RPG.

Desenvolvido para a disciplina de **Programação Orientada a Objetos**, com foco na aplicação de conceitos como herança, encapsulamento e interação entre classes.

---

## 📌 Principais funcionalidades

- **Cadastro de Jogo:** Defina título, gênero, classificação e desenvolvedora.

- **Criação de Jogadores:** Com nome, personagem (alter ego), habilidades, inventário e dinheiro inicial.

- **Criação de NPCs:** Nível, habilidades, alter ego e recompensa em dinheiro.

- **Loja de Itens:** Adicione e compre itens organizados por gênero de jogo.

- **Simulação de Partida:** Interaja com NPCs, ganhe pontos/dinheiro e compre na loja.

---

## 🧱 Estrutura do código

O código é organizado nas seguintes classes principais:

| Classe         | Função essencial |
|----------------|------------------|
| `Jogo`         | Dados básicos do jogo.|
| `Personagem`   | Classe base para `Jogador` e `NPC`, com atributos como alter ego, habilidades e itens |
| `Jogador`      | Herda de `Personagem` e adiciona nome, pontuação e dinheiro |
| `NPC`          | Herda de `Personagem` e representa inimigos com nível e recompensas |
| `Loja`         | Gerencia os itens disponíveis por gênero e permite que jogadores comprem itens |
| `Partida`      | Controla a adição de jogadores e o fluxo de início e encerramento da sessão de jogo |

---

## ▶️ Como executar

1. Tenha o **Python 3** instalado.
2. Salve o código como `gerenciador_jogos.py`.
3. Execute no terminal:

```bash
python gerenciador_jogos.py
```

4. Siga as instruções interativas no console.
