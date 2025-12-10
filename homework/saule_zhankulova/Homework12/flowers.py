class Flower:
    def __init__(self, flower_name, color, stem_length, price, durability):
        self.__flower_name = flower_name
        self.__stem_length = stem_length
        self.__price = price
        self.__color = color
        self.__durability = durability

    @property
    def flower_name(self):
        return self.__flower_name

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def price(self):
        return self.__price

    @property
    def color(self):
        return self.__color

    @property
    def durability(self):
        return self.__durability


class Rose(Flower):
    def __init__(self, color, stem_length, price, durability):
        super().__init__("Rose", color, stem_length, price, durability)


class Tulip(Flower):
    def __init__(self, color, stem_length, price, durability):
        super().__init__("Tulip", color, stem_length, price, durability)


class Peony(Flower):
    def __init__(self, color, stem_length, price, durability):
        super().__init__("Peony", color, stem_length, price, durability)


red_rose = Rose('red', 150, 150, 4)
white_rose = Rose('white', 150, 150, 4)
red_tulip = Tulip('red', 50, 80, 2)
yellow_tulip = Tulip('yellow', 50, 80, 2)
peony = Peony('pink', 120, 130, 5)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.price for flower in self.flowers)

    def average_time_for_a_bouquet_to_fade(self):
        if not self.flowers:
            return 0
        return sum(flower.durability for flower in self.flowers) / len(self.flowers)

    def sort_by(self, key):
        self.flowers.sort(key=lambda x: getattr(x, key))

    def search_by_durability(self, min_days, max_days):
        return [
            flower for flower in self.flowers
            if min_days <= flower.durability <= max_days
        ]

    def __str__(self):
        if not self.flowers:
            return "Пустой букет"

        result = [
            f"Букет (цветов: {len(self.flowers)}, "
            f"стоимость: {self.total_cost()} руб.):"
        ]
        for i, flower in enumerate(self.flowers, 1):
            result.append(
                f"  {i}. {flower.flower_name} ({flower.color}), "
                f"длина: {flower.stem_length}см, "
                f"цена: {flower.price} руб., "
                f"срок: {flower.durability} дней"
            )
        return "\n".join(result)


if __name__ == "__main__":
    bouquet = Bouquet()
    bouquet.add_flower(red_rose)
    bouquet.add_flower(white_rose)
    bouquet.add_flower(red_tulip)
    bouquet.add_flower(yellow_tulip)
    bouquet.add_flower(peony)

    print(bouquet)
    print(f"Общая стоимость: {bouquet.total_cost()} руб.")
    print(f"Среднее время увядания: {bouquet.average_time_for_a_bouquet_to_fade():.1f} дней")

    bouquet.sort_by('price')
    bouquet.sort_by('durability')
    print("\nПосле сортировки по цене:")
    print(bouquet)

    found_flowers = bouquet.search_by_durability(4, 5)
    print("\nЦветы с жизнью 4-5 дней:")
    for flower in found_flowers:
        print(f"  - {flower.flower_name} ({flower.color}): {flower.durability} дней")
