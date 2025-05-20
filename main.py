def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Controlla righe, colonne e diagonali
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]):
        return True

    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Benvenuto a Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            move = input(f"Giocatore {current_player}, inserisci la tua mossa (riga,colonna): ")
            row, col = map(int, move.split(","))

            if board[row][col] != " ":
                print("Casella già occupata. Riprova.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Giocatore {current_player} ha vinto!")
                break

            if is_draw(board):
                print("Pareggio!")
                break

            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("Input non valido. Inserisci due numeri separati da una virgola (es. 0,2).")

if __name__ == "__main__":
    tic_tac_toe()
