import random


class Toy:
    def __init__(self, id, name, quantity, weight):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.weight = weight

    def update_weight(self, new_weight):
        self.weight = new_weight


class ToyShop:
    def __init__(self):
        self.toys = []

    def add_toy(self, toy):
        self.toys.append(toy)

    def update_weight(self, toy_id, new_weight):
        for toy in self.toys:
            if toy.id == toy_id:
                toy.update_weight(new_weight)
                break

    def get_max_id(self) -> int:
        if len(self.toys) == 0:
            return 0
        else:
            return int(self.toys[-1].id)

    def read_toys_from_file(self, filename="toys.txt", mode="r"):
        with open(filename, mode) as file:
            lines = file.readlines()
            for line in lines:
                id, name, quantity, weight = line.strip().split(",")
                toy = Toy(id, name, int(quantity), int(weight))
                self.toys.append(toy)

    def write_toys_to_file(self, filename="toys.txt", mode="w"):
        with open(filename, mode) as file:
            for toy in self.toys:
                file.write(
                    f"{toy.id},{toy.name},{toy.quantity},{toy.weight}\n")

    def read_prizes_from_file(self,
                              filename="prizes.txt",
                              mode="r") -> list[str]:
        prizes = []

        with open(filename, mode) as file:
            prizes = file.read().splitlines()

        return prizes

    def write_prizes_to_file(self,
                             prizes: list[str],
                             filename="prizes.txt",
                             mode="a"):
        with open(filename, mode) as file:
            for prize in prizes:
                file.write(f"{prize}\n")

    def write_prize_to_file(self, prize: str, filename="prizes.txt", mode="a"):
        self.write_prizes_to_file([prize], filename, mode)

    def play_game(self):
        prizes = []

        for toy in self.toys:
            for _ in range(toy.weight):
                prizes.append(toy)

        if len(prizes) == 0:
            print("Нет доступных игрушек для розыгрыша")
            return

        prize = random.choice(prizes)
        prizes.remove(prize)
        prize.quantity -= 1

        self.write_prize_to_file(prize.name)

    def pick_up_toy(self):
        prizes = self.read_prizes_from_file()
        prizes.pop(0)
        self.write_prizes_to_file(prizes, mode="w")

toy_shop = ToyShop()
toy_shop.read_toys_from_file(mode="r")

toy1 = Toy(str(toy_shop.get_max_id() + 1), "Doll", 10, 20)
toy_shop.add_toy(toy1)

toy2 = Toy(str(toy_shop.get_max_id() + 1), "Car", 15, 30)
toy_shop.add_toy(toy2)

toy3 = Toy(str(toy_shop.get_max_id() + 1), "Cat", 5, 10)
toy_shop.add_toy(toy3)

toy4 = Toy(str(toy_shop.get_max_id() + 1), "Dog", 25, 40)
toy_shop.add_toy(toy4)

toy_shop.update_weight(1, 40)
toy_shop.update_weight(2, 30)
toy_shop.update_weight(3, 20)
toy_shop.update_weight(4, 10)

toy_shop.play_game()
toy_shop.play_game()
toy_shop.play_game()

toy_shop.pick_up_toy()
toy_shop.pick_up_toy()

toy_shop.write_toys_to_file()