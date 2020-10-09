#mast project by Randeep
class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}
        
    # To show all the books in library
    def displayBooks(self):
        print(f"There are following books with us: {self.name}")
        for book in self.booklist:
            print(book)
    # To Carry/lend book from library
    def lendBook(self, user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take your book now")
        else:
            print(f"Book is already taken by:{self.lendDict[book]}")
         
    # To add a new book in library
    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added")
        
    # To Return the book into the library
    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ =='__main__':
    nitin = Library(['Boots,Belts and Berrets','Alchemist','2 States','C++ basics'],"Nitin's Library")

    while(True):
            print(f"Welcome to the {nitin.name} library. Enter your choice to continue")
            print("1 for Displaying books")
            print("2 for Lending a book")
            print("3 for Adding a book")
            print("4 for Returning a book")
            user_choice= input()
            if user_choice not in ["1","2","3","4"]:
                print("Enter a valid choice")
                continue
            else:
                user_choice = int(user_choice)
            if user_choice == 1:
                nitin.displayBooks()
            elif user_choice == 2:
                book = input("Enter the name of the book you want to lend")
                user = input("Enter your name")
                nitin.lendBook(user, book)
            elif user_choice == 3:
                book = input("Enter the name of the book you want add")
                nitin.addBook(book)
            elif user_choice == 4:
                book = input("Enter the book you want return")
                nitin.returnBook()
            else:
                print("Not valid option")

            print("Press q to QUIT and c to continue")
            user_choice2 = input()
            while user_choice2 != "q" and user_choice2 != "c":
                print("Try again")
                user_choice2 = input()
            if user_choice2 == "q":
                exit()
            if user_choice2 == "c":
                continue
