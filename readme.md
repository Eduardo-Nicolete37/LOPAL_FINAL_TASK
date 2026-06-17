<div align="center">
  <h1>✏️S1_R3 - AT3_LOPAL</h1>
  <p>
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Status-Finalizado-green?style=for-the-badge" alt="Status"/>
  </p>
  <p>✕ ○ Jogo da Velha - Terminal ○ ✕</strong></p>
</div>


### Introdução

Este é um jogo da velha interativo desenvolvido em Python para ser executado diretamente no terminal. O projeto conta com uma interface estilizada em arte ASCII, sistema de turnos para dois jogadores e persistência de dados para salvar o histórico de vitórias, derrotas e empates.

---

## 🚀 Funcionalidades

O jogo possui um menu interativo com as seguintes opções:

1. **Começar Jogo:** Permite registrar dois jogadores locais e iniciar uma partida clássica de Jogo da Velha ($3 \times 3$). O sistema alterna os turnos automaticamente e valida jogadas inválidas ou posições ocupadas.
2. **Regras:** Exibe de forma clara e organizada as instruções e condições de vitória do jogo.
3. **Estatísticas:** Permite buscar o histórico de desempenho (Vitórias, Derrotas e Empates) de qualquer jogador registrado.
4. **Créditos:** Apresenta as informações dos desenvolvedores e da versão do sistema.
5. **Sair:** Encerra a execução do programa com segurança.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Armazenamento de dados:** Arquivos JSON (`data/game_data.json`)
* **Módulos Nativos:**
    * `json`: Para leitura e escrita do histórico dos jogadores.
    * `os`: Para limpar o terminal (`cls` / `clear`) e gerenciar pastas.
    * `sys`: Para manipulação e fechamento do script.
    * `msvcrt`: Para capturar o clique de qualquer tecla (exclusivo para sistemas Windows).

---

## 📂 Estrutura do Projeto

Ao rodar o jogo pela primeira vez, o próprio script cria a pasta de dados:

```text
├── data/
│   └── game_data.json      # Arquivo onde as estatísticas são guardadas
├── main.py                 # Código principal do jogo
└── README.md               # Documentação do projeto
```
---

## 🔍 Análise das Funções do Sistema

    O projeto foi estruturado dividindo as responsabilidades entre persistência de dados, lógica do jogo e interface com o usuário. Abaixo está a explicação do papel de cada função:

## 💾 Persistência e Manipulação de Dados

    load_stats(): Tenta ler o arquivo definido em STATS_FILE. Caso o arquivo ainda não exista, captura a exceção FileNotFoundError, cria um dicionário vazio, invoca a função de salvamento e retorna o objeto. Isso impede que o programa quebre na primeira execução.

    find_player(stats, nome): Percorre as chaves do dicionário de estatísticas aplicando o método .lower() tanto na chave quanto no nome buscado. Permite encontrar o jogador sem diferenciar maiúsculas de minúsculas.

    get_player_stats(stats, nome): Utiliza a função find_player. Se o jogador for encontrado, retorna seus dados. Caso contrário, retorna um dicionário com valores zerados: {"vitorias": 0, "derrotas": 0, "empates": 0}.

## 🎮 Lógica do Jogo
    
    print_board(board, jogador1, jogador2): Limpa a tela do terminal e desenha as linhas divisórias (│ e ───), posicionando cada elemento da lista board (índices de 0 a 8) em seu respectivo quadrante.

    vitoria(board): Possui uma lista de tuplas contendo todas as 8 combinações lineares possíveis de vitória. Varre essas combinações checando se os três índices mapeados possuem o mesmo caractere ("X" ou "O").

    empate(board): Utiliza a função nativa all() do Python para checar se todas as células da lista board já foram preenchidas por "X" ou "O", garantindo que não restam casas disponíveis.
## Autores


| | |
|:---:|:---:|
| **Eduardo Nicolete**<br>[![GitHub](https://img.shields.io/badge/GitHub-Eduardo--Nicolete37-181717?style=flat-square&logo=github)](https://github.com/Eduardo-Nicolete37) | **Lívia de Melo Pondian**<br>[![GitHub](https://img.shields.io/badge/GitHub-Livia--MP--Null-181717?style=flat-square&logo=github)](https://github.com/Livia-MP-Null) |
| **João Wictor**<br>[![GitHub](https://img.shields.io/badge/GitHub-joaorbm09-181717?style=flat-square&logo=github)](https://github.com/joaorbm09) | **Giovanna Sangali**<br>[![GitHub](https://img.shields.io/badge/GitHub-GiovannaSangalli21-181717?style=flat-square&logo=github)](https://github.com/GiovannaSangalli21) |