class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):

        if not isinstance(author, Author):
            raise TypeError("Author must be instance of Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be instance of Book class")
        if not type(date) == str:
            raise TypeError("date must be in string format")
        if not type(royalties) == int:
            raise TypeError("royalties must be of type int")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)