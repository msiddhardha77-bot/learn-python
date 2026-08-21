#library managemment system



class Library():
    def __init__(self):
        self.books=[]
    def add_books(self,books):
        
        self.books.extend(books)
        print("book added")
    def display_books(self):
        print("books are", self.books)
    def search_book(self):
        search=input("enter the book name").strip()
        if search in self.books:
            print("Books are:", search)
        else:
            print("not found")
    def issue_book(self):
        search=input("enter the book name").strip()
        if search in self.books:
            self.books.remove(search)
            print("Book issued")
        else:
            print("not found")
        
    def return_book(self):
        book=input("enter book name").strip()
        self.books.append(book)
        print("return success full")
    def exit(self):
        print("Thank you")
class member(Library):
    def add_member(self,name,id):
        self.name=name
        self.id=id
        
        print("you membership was success")
    
    def show_member_details(self):
        print("name of member:", self.name)
        print("ID of member :",self.id)

        
lib=member()
while True:
    opt=int(input("""
    1.Add books
    2.Disply Book
    3.search Book
    4.return book
    5.add a member
    6.Issue a book
    7.retunr a book
    8.show member detail
    9.exit
    choose your options"""))
            
    if opt==1:
        lib.add_books(input("Enter the book names: ").split(","))
    elif opt==2:
        lib.display_books()
    elif opt==3:
        lib.search_book()
    elif opt==4:
        lib.return_book()
    elif opt==5:
        lib.add_member(input("enter name"),int(input("enter ID")))
    elif opt==6:
        lib.issue_book()
    elif opt==7:
        lib.return_book()
    elif opt==8:
        lib.show_member_details()
    elif opt==9:
        lib.exit()
        break
    else:
        print("choose the correct option")
        

    
