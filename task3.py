import random


class GameSheet:
    def __init__(self) -> None:
        self._sheet = [' ' for i in range(9)]

    def print_sheet(self) -> None:
        print(f"[{self._sheet[0]}][{self._sheet[1]}][{self._sheet[2]}]\n"
              f"[{self._sheet[3]}][{self._sheet[4]}][{self._sheet[5]}]\n"
              f"[{self._sheet[6]}][{self._sheet[7]}][{self._sheet[8]}]\n")

    def write_symbol(self, cell: int, symbol: str) -> bool:
        if self.is_game_end():
            return False
        if cell < 1 or cell > 9:
            return False
        if symbol not in ['x', 'o']:
            return False
        if self._sheet[cell-1] != ' ':
            return False
        self._sheet[cell-1] = symbol
        return True

    def is_game_end(self) -> bool:
        return ' ' not in self._sheet

    def winner(self) -> int:
        if self._check_loser('o'):
            return 1
        if self._check_loser('x'):
            return 2
        if not self.is_game_end():
            return 0
        return 3

    def empty_cells(self) -> list:
        return [i+1 for i in range(0, 9) if self._sheet[i] == ' ']

    def _check_loser(self, symbol: str) -> bool:
        if symbol not in self._sheet[0:3] and ' ' not in self._sheet[0:3]:
            return True
        if symbol not in self._sheet[3:6] and ' ' not in self._sheet[3:6]:
            return True
        if symbol not in self._sheet[6:9] and ' ' not in self._sheet[6:9]:
            return True
        if symbol not in self._sheet[0:7:3] and ' ' not in self._sheet[0:7:3]:
            return True
        if symbol not in self._sheet[1:8:3] and ' ' not in self._sheet[1:8:3]:
            return True
        if symbol not in self._sheet[2:9:3] and ' ' not in self._sheet[2:9:3]:
            return True
        if symbol not in self._sheet[0:9:4] and ' ' not in self._sheet[0:9:4]:
            return True
        if symbol not in self._sheet[2:7:2] and ' ' not in self._sheet[2:7:2]:
            return True
        return False


class Player:
    def __init__(self, symbol: str, sheet: GameSheet) -> None:
        self._symbol = symbol
        self._sheet = sheet

    def symbol(self) -> str:
        return self._symbol

    def sheet(self) -> GameSheet:
        return self._sheet

    def num_cell_write(self) -> int:
        pass


class PlayerHuman(Player):
    def __init__(self, symbol: str, sheet: GameSheet) -> None:
        super().__init__(symbol, sheet)

    def num_cell_write(self) -> int:
        cell = 0
        while True:
            inp = input(f"Игрок [{self.symbol()}], в какой клетке сделать ход? Доступны {self.sheet().empty_cells()}\n")
            cell = int(inp)
            if not self._sheet.write_symbol(cell, self.symbol()):
                print("Недопустимый номер клетки, попробуйте еще раз.")
                continue
            break
        return cell


class PlayerBot(Player):
    def __init__(self, symbol: str, sheet: GameSheet) -> None:
        super().__init__(symbol, sheet)

    def num_cell_write(self) -> int:
        cells=self.sheet().empty_cells()
        index=random.randint(0, len(cells)-1)
        self._sheet.write_symbol(cells[index], self.symbol())
        return cells[index]


class GameManager:
    def __init__(self) -> None:
        self._sheet = GameSheet()
        self._players = []

    def CreateGame(self):
        if len(self._players) > 1:
            return
        inp = input("Выбирите тип игры:\n"
                    "1 - человек против человека\n"
                    "2 - человек против компьютера\n")
        if inp == '1':
            self._players.append(PlayerHuman('x',self._sheet))
            self._players.append(PlayerHuman('o',self._sheet))
        elif inp == '2':
            if random.randint(0,1) >0:
                self._players.append(PlayerBot('x',self._sheet))
                self._players.append(PlayerHuman('o',self._sheet))
            else:
                self._players.append(PlayerHuman('x',self._sheet))
                self._players.append(PlayerBot('o',self._sheet))
        else:
            print("Указан неверный тип игры.")
            self.CreateGame()

    def StartGame(self):
        i = 0
        while self._sheet.winner()==0:
            player = self._players[i].symbol()
            print(f"Ходит игрок [{player}]...")
            self._players[i].num_cell_write()
            self._sheet.print_sheet()
            i = i+1 if i < len(self._players)-1 else 0
        winner=self._sheet.winner()
        if winner==1:
            print("Игрок [x] победил!!!")
        elif winner==2:
            print("Игрок [o] победил!!!")
        else:
            print("Ничья!!!")
        print(f"Игра окончена.")


print("Программа для игры в крестики-нолики.")
try:
    gameManager = GameManager()
    gameManager.CreateGame()
    gameManager.StartGame()
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")