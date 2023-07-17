"""Initialize a few books into the catalog."""
alice_in_wonderland = Book("Alice in Wonderland", "Lewis Carroll")

def main(): 
    startupMessage = "Hello. Welcome to your e-Reader."
    print(startupMessage)
    option = ""
    userKindle = Kindle()

    while option != "4":
        option = input("What would you like to do? Input a number. \n1) View books. \n2) Buy books. \n3) Read a book. \n4) Quit.").strip()
        if option not in "1234":
            print("Invalid input. Try again.\n")
            break

        match option:
            case "1":
                Kindle.view_purchased()
            case "2":
                Kindle.buy_books()
            case "3":
                Kindle.read_book()
            case "4":
                break


class Kindle:
    def __init__(self):
        ownedBooks = []

    def view_purchased(self, ownedBooks):
        print("My books:")
        for book in ownedBooks: 
            print(book.title)

    def buy_books(self, ownedBooks):
        print("Available books: ")
        for book in CATALOG:
            print(book.title)



class Book:
    def __init__(self, title, author, filename):
        self.title = title
        self.author = author
        self.filename = filename