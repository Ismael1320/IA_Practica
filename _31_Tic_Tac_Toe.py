from random import randrange #Importa la función para numeros alatorios

#Crea el tablero inicial.
board = [[1, 2, 3],
         [4, 'x', 6],
         [7, 8, 9]]

def display_board(board): #muestra el tablero
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", row[0], "  |  ", row[1], "  |  ", row[2], "  |  ")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board): #Movimiento del usuario
   while True:
        move = int(input("Ingresa tu movimiento: "))
        if move < 1 or move > 9: #Valida que el número ingresado esta dentro del rango
            print("Movimiento invalido.")
            continue

        for r in range(3):
            for c in range(3):
                if board[r][c] == move: #Si la casilla esta libre
                    board[r][c] = 'O' #se coloca una O
                    return
        print("Ese cuadro ya esta ocupado.")

def make_list_of_free_fields(board): #Lista de casillas libres
    free = []
    for r in range(3):
        for c in range(3):
            if type(board[r][c])== int: #Verifica si ese número está libre
                free.append((r, c))
    return free


def victory_for(board, sign): #Verifica ganador
    for r in range(3): #Filas
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True
        
    for c in range(3):#Columnas
        if board[0][c] == sign and board[1][c] == sign and board[2][c] == sign:
            return True
        
        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: #Diagonal
            return True
        
        if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: #Diagonal
            return True
        
    return False

def draw_move(board): #Movimiento de la maquina
    free = make_list_of_free_fields(board)
    if free:
        r, c= free[randrange(len(free))] #Elige una posición alatoria
        board[r][c] = 'x'

while True: #Ciclo inicial del juego
    display_board(board)

    enter_move(board) #Turno del jugador

    if victory_for(board, 'O'): #Si gana el usuario.
        display_board(board)
        print("¡Has Ganado!") #Muestra este mensaje de victoria.
        break

    if not make_list_of_free_fields(board): #Si ya no quedan espacios y ninguno se declara ganador.
        display_board(board)
        print("Empate") #Muestra este mensaje.
        break

    draw_move(board) #Turno de la maquina

    if victory_for(board, 'x'): #Si gana la maquina.
        display_board(board)
        print("¡Has perdido!") #Muestra este mensaje de derrota.
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("Empate")
        break