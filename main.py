import json
import os
import msvcrt
import sys

os.makedirs("data", exist_ok=True)

STATS_FILE = "data/game_data.json"


def load_stats():
    try:
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        stats = {"1": None, "2": None, "3": None}
        save_stats(stats)
        return stats


def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


def find_player(stats, nome):
    for slot, data in stats.items():
        if data is not None and data["nome"].lower() == nome.lower():
            return slot, data
    return None, None


def get_player_stats(stats, nome):
    _, data = find_player(stats, nome)
    if data is not None:
        return data
    return {"nome": nome, "vitorias": 0, "derrotas": 0, "empates": 0}


def save_player_result(stats, nome, resultado):
    slot, data = find_player(stats, nome)
    if data is None:
        slot = next((s for s, v in stats.items() if v is None), None)
        if slot is None:
            print(f"⚠️  Todos os slots estão ocupados. {nome} não foi salvo.")
            return
        data = {"nome": nome, "vitorias": 0, "derrotas": 0, "empates": 0}
    if resultado == "vitoria":
        data["vitorias"] += 1
    elif resultado == "derrota":
        data["derrotas"] += 1
    elif resultado == "empate":
        data["empates"] += 1
    stats[slot] = data

def print_board(board, jogador1, jogador2):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"  {board[0]} │ {board[1]} │ {board[2]}")
    print(" ───┼───┼───")
    print(f"  {board[3]} │ {board[4]} │ {board[5]}")
    print(" ───┼───┼───")
    print(f"  {board[6]} │ {board[7]} │ {board[8]}")
    print("")

def empate(board):
    return all(cell in ("X", "O") for cell in board)
def vitoria(board):
    combos = [(0,1,2), (3,4,5), (6,7,8),   
              (0,3,6), (1,4,7), (2,5,8),   
              (0,4,8), (2,4,6)]            
    for a, b, c in combos:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return board[a]
    return None
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[96m")
        print("╭─────────────────────────────────────────────────────────────╮")
        print("│     ██╗ ██████╗  ██████╗  ██████╗                           │")
        print("│     ██║██╔═══██╗██╔════╝ ██╔═══██╗                          │")
        print("│     ██║██║   ██║██║ ████ ██║   ██║                          │")
        print("│ ██  ██║██║   ██║██║   ██║██║   ██║                          │")
        print("│ ██████║╚██████╔╝╚██████╔╝╚██████╔╝                          │")
        print("│ ╚═════╝  ╚═══╝   ╚═════╝   ╚════╝                           │")
        print("│       ██████╗  █████╗                                       │")
        print("│       ██╔══██╗██╔══██╗                                      │")
        print("│       ██║  ██║███████║                                      │")
        print("│       ██║  ██║██╔══██║                                      │")
        print("│       ██████╔╝██║  ██║                                      │")
        print("│       ╚═════╝ ╚═╝  ╚═╝                                      │")
        print("│   ██╗     ██╗ ███████╗ ██╗      ██╗   ██╗  █████╗           │")
        print("│   ██║     ██║ ██╔════╝ ██║      ██║   ██║ ██╔══██╗          │")
        print("│   ██║     ██║ █████╗   ██║      ████████║ ███████║          │")
        print("│     ██  ██ ╔╝ ██╔══╝   ██║      ██║   ██║ ██╔══██║          │")
        print("│       ██ ╔═╝  ███████╗ ███████╗ ██║   ██║ ██║  ██║          │")
        print("│        ╚═╝    ╚══════╝ ╚══════╝ ╚═╝   ╚═╝ ╚═╝  ╚═╝          │")
        print("├─────────────────────────────────────────────────────────────┤")
        print("│                │  1 ▸ Começar jogo        │                 │")
        print("│                │  2 ▸ Regras              │                 │")
        print("│                │  3 ▸ Estatísticas        │                 │")
        print("│                │  4 ▸ Créditos            │                 │")
        print("│                │  5 ▸ Sair                │                 │")
        print("╰────────────────┴──────────────────────────┴─────────────────╯")
        print("\033[0m")


        print("")
        while True:
            try:
                choose = int(input("Digite a opção desejada (1-5): "))
                break
            except ValueError:
                print("Valor Inválido! Tente novamente...")
        if choose == 1:
            jogador1 = input("Digite o nome do Jogador 1 (X): ")
            jogador2 = input("Digite o nome do Jogador 2 (O): ")
            os.system('cls' if os.name == 'nt' else 'clear')
            stats = load_stats()
            stats_j1 = get_player_stats(stats, jogador1)
            stats_j2 = get_player_stats(stats, jogador2)
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            players = {"X": jogador1, "O": jogador2}
            current = "X"
            while True:
                print_board(board, jogador1, jogador2)
                print(f"Vez de {players[current]} ({current})")
                try:
                    pos = int(input("Escolha uma posição (1-9): ")) - 1
                except ValueError:
                    print("Valor inválido! Pressione uma tecla...")
                    msvcrt.getch()
                    continue

                if pos < 0 or pos > 8 or board[pos] in ("X", "O"):
                    print("Posição inválida ou ocupada! Pressione uma tecla...")
                    msvcrt.getch()
                    continue

                board[pos] = current

                winner = vitoria(board)
                if winner:
                    print_board(board, jogador1, jogador2)
                    vencedor = players[winner]
                    perdedor = jogador2 if vencedor == jogador1 else jogador1
                    print(f"🏆 {vencedor} venceu!")
                    save_player_result(stats, vencedor, "vitoria")
                    save_player_result(stats, perdedor, "derrota")
                    save_stats(stats)
                    msvcrt.getch()
                    break

                if empate(board):
                    print_board(board, jogador1, jogador2)
                    print("Empate!")
                    save_player_result(stats, jogador1, "empate")
                    save_player_result(stats, jogador2, "empate")
                    save_stats(stats)
                    msvcrt.getch()
                    break

                current = "O" if current == "X" else "X"


        elif choose == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("╭─────────────────────────────────────────────────────────╮")
            print("│                      ✕ ○ REGRAS ○ ✕                     │")
            print("├─────────────────────────────────────────────────────────┤")
            print("│                                                         │")
            print("│   1. OBJETIVO                                           │")
            print("│    - Marque 3 simbolos seus em linha, coluna ou         │")
            print("│       diagonal antes do adversario.                     │")
            print("│                                                         │")
            print("│   2. TABULEIRO                                          │")
            print("│     - Grade 3x3, posicoes numeradas de 1 a 9.           │")
            print("│     - Jogador X sempre comeca a partida.                │")
            print("│                                                         │")
            print("│   3. DECISOES & FLUXO                                   │")
            print("│     - Jogar (Play): Escolhe uma posicao vazia (1-9).    │")
            print("│     - Os jogadores alternam turnos (X e O) ate o        │")
            print("│        tabuleiro encher ou alguem vencer.               │")
            print("│     - Posicao ja ocupada: jogada invalida, repete       │")
            print("│        o turno.                                         │")
            print("│                                                         │")
            print("│   4. RESULTADO                                          │")
            print("│     - Vitoria: 3 simbolos iguais alinhados.             │")
            print("│     - Empate (Draw): tabuleiro cheio sem vencedor.      │")
            print("│                                                         │")
            print("╰─────────────────────────────────────────────────────────╯")
            print("───────────────────────────────────────────────────────────")
            print("           [Pressione qualquer tecla para voltar]")
            msvcrt.getch()
        elif choose == 3:
            try:
                with open("data/game_data.json", "r") as f:
                    stats = json.load(f)
            except FileNotFoundError:
                game_data= {
                    "1": None,
                    "2": None,
                    "3": None
                }
                with open("data/game_data.json", "w") as f:
                    json.dump(game_data, f, indent=4)
                stats = game_data
            os.system('cls' if os.name == 'nt' else 'clear')
            print("╭───────────────────────────────────────────────╮")
            print("│             ✕ ○ ESTÁTISTICAS ○ ✕              │")
            print("╰───────────────────────────────────────────────╯")
            print(" ")
            for num_slot in ["1", "2", "3"]:
                if stats[num_slot] is None:
                    print("╭───────────────────────────────────────────────╮")
                    print(f"│   Slot {num_slot:<39}│")
                    print("│   - SLOT VAZIO -                              │")
                    print("╰───────────────────────────────────────────────╯")
                    print("")
            msvcrt.getch()
        elif choose == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("╭──────────────────────────────────────╮")
            print("│          ✕ ○ CRÉDITOS ○ ✕            │")
            print("├──────────────────────────────────────┤")
            print("│   Desenvolvido por:                  │")
            print("│     Eduardo Nicolete                 │")
            print("│     Lívia de Melo                    │")
            print("│     João Wictor                      │")
            print("│     Giovanna Sangali                 │")
            print("├──────────────────────────────────────┤")
            print("│   GitHub:                            │")
            print("│     github.com/Eduardo-Nicolete37    │")
            print("├──────────────────────────────────────┤")
            print("│   Informações do Sistema:            │")
            print("│     Linguagem: Python 3.14           │")
            print("╰──────────────────────────────────────╯")
            print("")
            print("────────────────────────────────────────")
            print(" [Pressione qualquer tecla para voltar] ")
            msvcrt.getch()
        elif choose == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Obrigado por jogar! Até a próxima.")
            sys.exit()

main()