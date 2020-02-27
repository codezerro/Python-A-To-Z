class Library:

    def __init__(self,listOfBooks):
        self.availableBooks=listOfBooks
    
    def displayAvailablebooks(self):
        print()
        print("List of Available Books \n")
        for book in self.availableBooks:
            print(book)

    def lendBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("you have now borrow the book : ")
            self.availableBooks.remove(requestedBook)
        else:
            print("Your requested book not available")

    def addBoook(self,addedBook):
        self.availableBooks.append(addedBook)
        print("You have successfully return the book")
        
    
class Customer:
    def requestBook(self):
        print("Enter the book name you would like to borrow : ")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the name of Book which you want to returning : ")
        self.book=input()
        return self.book
    



library = Library(["Think and Grow Rich","who are you","For one more time","Paradoxical Sajid"])
customer=Customer()
# print("Enter 1 to display the availbooks")
# print("Enter 2 to request for a book")
# print("Enter 3 for returning Book")
# print("Enter 4 for exiting ")
# userChoice=int(input())

while True :

    print("Enter 1 to display the availbooks")
    print("Enter 2 to request for a book")
    print("Enter 3 for returning Book")
    print("Enter 4 for exiting ")
    userChoice=int(input())

    if userChoice is 1:
        library.displayAvailablebooks()
    elif userChoice is 2:
        bookSearch=customer.requestBook()
        library.lendBook(bookSearch)
    elif userChoice is 3:
        returnBook=customer.requestBook()
        library.addBoook(returnBook)
    elif userChoice is 4:
        quit()
    