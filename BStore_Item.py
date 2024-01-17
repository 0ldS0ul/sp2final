class Item():
    def __init__(self, num, name, year, genre, price, availb):
        self.name = name
        self.year = year
        self.genre = genre
        self.price = price
        self.availb = availb  

        self.tuple = (num, name, year, genre, price, availb)