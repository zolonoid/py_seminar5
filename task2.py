import random


class GameTable:
    def __init__(self) -> None:
        self._candies = 2021
        self._lastPlayer = 0

    def candies_count(self) -> int:
        return self._candies if self._candies > 0 else 0

    def take_candies(self, player: int, count: int) -> None:
        if self._candies > 0:
            self._lastPlayer = player
        self._candies -= count

    def is_game_end(self) -> bool:
        return False if self._candies > 0 else True

    def last_player(self) -> int:
        return self._lastPlayer


class Player:
    _last_id = 0

    def __init__(self) -> None:
        Player._last_id += 1
        self._id = Player._last_id

    def id(self) -> int:
        return self._id

    def how_many_candies(self) -> int:
        pass


class PlayerHuman(Player):
    def __init__(self) -> None:
        super().__init__()

    def how_many_candies(self) -> int:
        count = 0
        while True:
            inp = input(f"Игрок №{self.id()}, cколько конфет вы возьмете?\n")
            count = int(inp)
            if count < 1 or count > 28:
                print("Недопустимое количество, попробуйте еще раз.")
                continue
            break
        return count


class PlayerBot(Player):
    def __init__(self) -> None:
        super().__init__()

    def how_many_candies(self) -> int:
        return random.randint(1, 28)


class GameDealer:
    def __init__(self) -> None:
        self._table = GameTable()
        self._players = [PlayerHuman()]

    def CreateGame(self):
        if len(self._players) > 1:
            return
        inp = input("Выбирите тип игры:\n"
                    "1 - человек против человека\n"
                    "2 - человек против компьютера\n")
        if inp == '1':
            self._players.append(PlayerHuman())
        elif inp == '2':
            self._players.append(PlayerBot())
        else:
            print("Указан неверный тип игры.")
            self.CreateGame()

    def StartGame(self):
        i = random.randint(0, len(self._players)-1)
        while not self._table.is_game_end():
            print(f"Конфет на столе: {self._table.candies_count()}.")
            player = self._players[i].id()
            print(f"Ходит игрок №{player}...")
            count = self._players[i].how_many_candies()
            self._table.take_candies(player, count)
            print(f"Игрок №{player} взял {count} конфет со стола.")
            i = i+1 if i < len(self._players)-1 else 0
        print(f"Игрок №{self._table.last_player()} победил!!!")
        print(f"Игра окончена.")


print("Программа для игры с конфетами.")
try:
    gameDealer = GameDealer()
    gameDealer.CreateGame()
    gameDealer.StartGame()
except Exception as exc:
    print(f"Что-то пошло не так...\n{exc}")
