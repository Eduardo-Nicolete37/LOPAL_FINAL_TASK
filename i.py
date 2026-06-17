# 
import os

def menu():
    print("\033[96m")

    print("    ██╗ ██████╗  ██████╗  ██████╗ ")
    print("    ██║██╔═══██╗██╔════╝ ██╔═══██╗ ")
    print("    ██║██║   ██║██║ ████ ██║   ██║ ")
    print("██  ██║██║   ██║██║   ██║██║   ██║ ")
    print("██████║╚██████╔╝╚██████╔╝╚██████╔╝ ")
    print("      ╚═╝ ╚═══╝  ╚═════╝  ╚═════╝   ")
    print("      ██████╗  █████╗ ")
    print("      ██╔══██╗██╔══██╗ ")
    print("      ██║  ██║███████║")
    print("      ██║  ██║██╔══██║")
    print("      ██████╔╝██║  ██║")
    
    print("  ██╗     ██╗ ███████╗ ██╗      ██╗   ██╗  █████╗  ")
    print("  ██║     ██║ ██╔════╝ ██║      ██║   ██║ ██╔══██╗")
    print("  ██║     ██║ █████╗   ██║      ████████║ ███████║ ")
    print("    ██  ██ ╔╝ ██╔══╝   ██║      ██║   ██║ ██╔══██║")
    print("      ██ ╔═╝  ███████╗ ███████╗ ██║   ██║ ██║  ██║")
    print("       ╚═╝    ╚══════╝ ╚══════╝ ╚═╝   ╚═╝ ╚═╝  ╚═╝")
    




    print("\033[95m")
    print("                     ❌  VS  ⭕")
    print("\033[0m")

    print("\n\033[97m1. Começar jogo")
    print("2. Regras")
    print("3. Estatísticas")
    print("4. Créditos")
    print("5. Sair\033[0m")

    print("\n\033[97m      ╭──────────────────────────╮")
    print("      │  1 ▸ Começar jogo        │")
    print("      │  2 ▸ Regras              │")
    print("      │  3 ▸ Estatísticas        │")
    print("      │  4 ▸ Créditos            │")
    print("      │  5 ▸ Sair                │")
    print("      ╰──────────────────────────╯\033[0m")

    print("\n\033[90m      ✦ Escolha uma opção para continuar ✦\033[0m\n")

def main():
    clear()
    menu()

main()
    print("    ██")
import os
import time
import random

cores = ["\033[95m", "\033[96m", "\033[94m", "\033[92m", "\033[93m"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo(cor):
    print(cor)