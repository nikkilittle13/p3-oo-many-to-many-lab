class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    pass


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]
    pass


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Invalid author")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Invalid book")
        self.all.append(self)
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("Invalid date")
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("Invalid royalties")

    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]
    pass