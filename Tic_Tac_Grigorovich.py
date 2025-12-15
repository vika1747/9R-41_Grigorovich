
# -*- coding: utf-8 -*-

#создание поля
def create_board():
    return [['.' for _ in range(3)] for _ in range(3)]
#отображение поля
def display_board(board):
    print("\n   1 2 3")
    for i in range(3):
        print(f"{i+1}  {' '.join(board[i])}")
#общая проверка выигрыша
def check_winner(board, symbol):
    # проверка столбцов и строк
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True
    
    # проверка даигоналей
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2-i] == symbol for i in range(3)):
        return True
    
    return False
#проверка на ничью    
def check_draw(board):
    return all(cell != '.' for row in board for cell in row)
# функция получения хода от игрока
def get_move(symbol):
    while True:
        #условие для проверки ввода
        try:
            move = input(f"\nХод {symbol} (Введите строку и ряд): ").split()
            if len(move) != 2:
                #проверка расстояния между числами
                print("Введите числа через пробел")
                continue
            
            row, col = int(move[0])-1, int(move[1])-1
            #проверка введенных чисел
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Введите числа от 1 до 3")
        #вывод ошибки ввода неверных символов
        except ValueError:
            print("Вводите числа.")
#основная исполнительная функция
def main():
    board = create_board()
    current = 'x'
    
    while True:
        display_board(board)
        
        row, col = get_move(current)
        
        if board[row][col] != '.':
            print("Клетка уже занята")
            continue
        
        board[row][col] = current
        
        if check_winner(board, current):
            display_board(board)
            print(f"\n{current} победили!")
            break
        
        if check_draw(board):
            display_board(board)
            print("\n Ничья!")
            break
        
        current = 'o' if current == 'x' else 'x'
#запуск исполнительной функции
if __name__ == "__main__":
    main()