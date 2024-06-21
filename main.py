ADD = 1
VIEW = 2
SEARCH = 3
REMOVE = 4
EXIT = 5


#I CREATE A DICTIONARY: VALUE == NAME BOOK, KEY == NUMBER OF COPIES AVIABLE
books = {
    "Clean Code": 5,
    "Padre ricco Padre povero": 10,
    "Linguaggio C": 3,
    "Hello World": 4,
    "7 brevi lezioni di fisica": 6
}

#FUNCTION TO DISPLAY MENU OF PROGRAM
def menu():

    print(">>>Library Management")
    print("1. for add a book to the library ")
    print("2. to view the aviable book and copies")
    print("3. to search a book and it aviable copies")
    print("4 to remove a book from library.")
    print("5 to exit from the program")
    print()

#FUNCTION TO ADD A BOOK
def add_book(dictionary):

    book = input("Enter a name's book: ") # INPUT REQUEST FOR KEY == NAME BOOK, AND VALUE == NUMBER OF COPIES
    copies = int(input("Enter a number of copies: "))

    dictionary[book] = copies # ADDING KEY-VALUE TO DICTIONARY 

    print(f"{book} has been added to library\n")  # PRINT OF UPADTE DICTONARY 

#FUNCTION TO VIEW AVIABLE BOOK
def view_books(dictonary):
    if len(dictonary) == 0:
        print("No books present in the library.\n") # IF LENGHT OF DICT IS 0, PRINT NO BOOK PRESENT IN THE LIBRARY
    else:
        print("Book\tNumber of copies")
        for book, copies in dictonary.items():
            print(f"{book} : {copies}")
        print()
        
#FUNCTION TO SEARCH A BOOK
def search_book(dictonary):
    searching_book = input("Enter name's book:\n")
    
    try:
        copies = dictonary[searching_book]
        print(f"Copies aviable of {searching_book} book: {copies}\n")  # OUTPUT OF COPIES AVIABLE OF SEARCHING BOOK
    except KeyError:
        print("Book not exist in the library.\n")

#FUNCTION TO REMOVE A BOOK
def remove_book(dictonary):
    searching_book_to_remove = input("Which book you want to remove? ")

    try:
        del dictonary[searching_book_to_remove]
        print(f"{searching_book_to_remove} book has been removed\n")  # OUTPUT OF REMOVED BOOK
    except KeyError:
        print("Book not exist in the library.\n")

def main():
    
    #I USE WHILE LOOP TO DO MORE OPERATION UNTIL THE USER DECIDE TO EXIT FROM THE PROGRAM
    choice = 0
    while choice < 1 or choice != 5:
        menu()
        choice = int(input("Enter a number between 1 to 5 to choise: "))
        if choice < 1 or choice > 5:
            print("Error! Enter a valid number (1 to 5)\n")
    
        if choice == 1:
            add_book(books)
        elif choice == 2:
            view_books(books)
        elif choice == 3:
            search_book(books)
        elif choice == 4:
            remove_book(books)
    print("Exit from program...")
     
main()





