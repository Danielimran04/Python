# magic method = Dunder methods (double underscore) __init__,__str__,__eq__
#                They are automatically called by many Python's built-in operations.
#                They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

#function nih untuk ubah dari dia tunjuk memory address tukar ke ayat kita sendiri
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    #function nih untuk detect same ade object1==object2 or object1!=object2
    def __eq__(self,other): # other means other book
        return self.title == other.title and self.author == other.author
    
    # function nih untuk kita detect either object1<object2 or not
    def __lt__(self,other):
        return self.num_pages<other.num_pages
    
    #function nih kita detect either object1>object2 or not
    def __gt__(self,other):
        return self.num_pages>other.num_pages
    
    #function nih untuk kita tambah 2 object punya nilai pages 
    def __add__(self,other):
        return f" {self.num_pages+other.num_pages} pages"
    
    #function nih untuk kita detect either dlm object tu ade value yang kita nak tak
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    #nih kita nak tgk key dia iaitu value of the title atau pun lain lain pun boleh setkan lah dkt if
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Sorry the {key} was cannot found"





book1 = Book("The Hobbit", "J.R.R. Tolkien",310)
book2 = Book("Harry Potter", "J.K Rowling",172)
book3 = Book("math", "J.R.R. Tolkien",189)
book4 = Book("The Hobbit", "J.R.R. Tolkien",310)

print(book1) # selalu kalau xde def __str__(self) dia akan keluar address location 
# so guna magic method means kita boleh tukar behaviour dia 

# kalau xde magic __eq__ dia akan selalu jadi false walaupun betul so adenye __eq__ baru dia boleh tahu either object tu sama or not
print(book1==book2)
print(book1==book4)

#call method for __it__
print(book1<book2)

# call methos for __gt__
print(book1>book2)

# call method for __add__
print(book1+book2)

#call method for __contain__
print("The Hobbit" in book1)

#call method for __getItem__
print(book1['title'])
print(book1['author'])
print(book1['num_pages'])
print(book1['audio'])
