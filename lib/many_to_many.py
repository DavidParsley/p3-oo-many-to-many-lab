class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def add_contract(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise Exception("contract must be an instance of Contract")
        
    def books(self):
        book_list = []
        for contract in self._contracts:
            book_list.append(contract.book)
        return book_list 

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract 

    def total_royalties(self):
        total = sum(contract.royalties for contract in self._contracts)
        return total
     



class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []

    def contracts(self):
        return self._contracts 
       
    def add_contract(self, contract):
        if isinstance(contract, Contract):
            self._contracts.append(contract)
        else:
            raise Exception("contract must be an instance of Contract")  

    def authors(self):
        return self._authors 
       
    def add_author(self, author):
        if isinstance(author, Author):
            self._authors.append(author)
        else:
            raise Exception("author must be an instance of Author")
                        


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("author must be an instace of Author")
        if isinstance(book, Book):    
            self.book = book
        else:
            raise Exception("book must be an instace of Book")
        if  not isinstance(date, str):
            raise Exception("date must be a String")
        else:
            self.date = date    
        if not isinstance(royalties, int):
            raise Exception("royalities must be an Integer")
        else:
            self.royalties = royalties

        author.add_contract(self)
        book.add_contract(self)
        book.add_author(author)
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
       
 