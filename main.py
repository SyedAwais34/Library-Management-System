import json
import random
import string
from pathlib import Path
from datetime import date, timedelta, datetime

class Library:
    database = 'data.json'
    books_database = 'books.json'
    data = []
    book_data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")        
    except Exception as err:
        print(f"An error occured as {err}")
        

    try:
        if Path(books_database).exists():
            with open(books_database) as fs:
                book_data = json.loads(fs.read())
        else:
            print("No such file exists")        
    except Exception as err:
        print(f"An error occured as {err}")




    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Library.data))


    @classmethod
    def __bookupdate(cls):
        with open(cls.books_database, 'w') as fs:
            fs.write(json.dumps(Library.book_data))        

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)  
        spchr = random.choices("!@#$%^&*", k = 1) 
        id = alpha + num + spchr
        random.shuffle(id)     
        return "".join(id)
    


    def createaccount(self):
        info = {
            "name" : input("Tell your name :- "),
            "age" : int(input("Tell your age :- ")),
            "email" : input("Tell your email :- "),
            "password" : input("Tell your password :- "),
            "accountNo.": Library.__accountgenerate(),
            "balance" : 0,
            "borrow_book" : []
        }

        if info['age'] < 12:
            print("You must be at least 12 years old to create an account.") 
        elif len(info['password']) < 8:
            print("Password must be at least 8 characters.") 
        else:
            print("Account created successfully")
            for i in info:
                if i != "borrow_book":
                    print(f"{i} : {info[i]}")    
            print("Please note down your account number.")


            Library.data.append(info)  
        
            Library.__update()  


    def adminaccount(self):

        adminemail = input("Please enter your email :- ")
        adminpassword = input("Please enter your password :- ")

        if adminemail == "admin@gmail.com" and adminpassword == "1234":
            while True:
                print("\n=== Admin Dashboard ===")
                print("Press 1 to add a book :- ")
                print("Press 2 to delete a book :- ")
                print("Press 3 to update a book :- ")
                print("Press 4 to view all books :- ")
                print("Press 5 to view all users :- ")
                print("Press 6 to logout :- ")

                option = input("Tell your response :- ")

                if option == "1":
                    addbook = {
                        "book_id": int(input("Enter id for this book :- ")),
                        "book_name": input("Enter title of the book :- "),
                        "book_author": input("Enter author of the book :- "),
                        "book_price": int(input("Enter per day price of a book :- ")),
                        "book_quantity": int(input("Enter quantity of a book :- "))
                    }

                    if addbook['book_price'] < 0:
                        print("Price must be greater than zero")
                    elif addbook['book_quantity'] < 0:
                        print("Quantity must be greater than zero")
                    else:
                        Library.book_data.append(addbook)

                        Library.__bookupdate()
                
                        print("Book Added successfully")           


                if option == "2":
                    book_id = int(input("Press book id to delete a book :- "))
                    
                    for i in Library.book_data:
                        if i["book_id"] == book_id:
                            Library.book_data.remove(i)    
                            print("Book deleted successfully")
                            break
                    else:
                        print("Book not found")
                        
                    Library.__bookupdate()




                if option == "3":
                    book_id = int(input("Enter book id to update: "))
                    
                    for i in Library.book_data:
                        if i["book_id"] == book_id:
                            print("Fill the details for change and leave it empty if no change \n") 
                    
                    
                        book_name = input("Enter new title of the book or press enter to skip :- ")
                        book_author = input("Enter new author of the book or press enter to skip :- ")
                        book_price = int(input("Enter new per day price of a book or press enter to skip :- "))
                        book_quantity = int(input("Enter new quantity of a book or press enter to skip :- "))


                        if book_name != "":
                            i["book_name"] = book_name

                        if book_author != "":
                            i["book_author"] = book_author    

                        if book_price != "":
                            i["book_price"] = book_price

                        if book_quantity != "":
                            i["book_quantity"] = book_quantity


                        print("Book updated successfully")
                        break
                    else:
                        print("Book nor found")    

                    Library.__bookupdate()


                if option == "4":
                    print("All books has been showned :- ")

                    for i in Library.book_data:
                        print(f"{i}")


                if option == "5":
                    print("All users has been showned :- ")

                    for i in Library.data:
                        print(f"{i}")

                elif option == "6":
                        print("Account has been Logout successfully")
                        return


    def loginaccount(self):
        
        accnum = input("Please enter your account number :- ")
        password = input("Please enter your password :- ")

        userdata = [i for i in Library.data if i['accountNo.'] == accnum and i['password'] == password]
        current_user = userdata[0]

        if userdata == False:
            print("Sorry no data found")


        else:
            while True:
                print("\n==== Student Dashboard ====")
                print("Press 1 to View All Books :- ")   
                print("Press 2 to Borrow a Book :- ")
                print("Press 3 to Return a Book :- ")
                print("Press 4 to Add Money to Wallet :- ")
                print("Press 5 to View Account Details :- ")
                print("Press 6 to Update Account :- ")
                print("Press 7 to Delete Account :- ")
                print("Press 8 to Logout :- ")

                option = input("Tell your response :- ")

                if option == "1":
                    print("All books has been shown :- ")

                    for i in Library.book_data:
                        print(f"{i}")

                if option == "2":
                    book_id = int(input("Enter book id to borrow :- "))

                    found = False

                    for i in Library.book_data:
                        if i["book_id"] == book_id:
                            found = True

                            if i["book_quantity"] == 0:
                                print("Book not available")
                                break

                            days = int(input("Enter number of days :- "))
                            total = i["book_price"] * days

                            if current_user["balance"] < total:
                                print("Insufficient balance")
                                break

                            borrow_date = datetime.now().date()
                            due_date = borrow_date + timedelta(days=days)

                            # save proper record
                            current_user.setdefault("borrow_book", []).append({
                                "book_id": book_id,
                                "days": days,
                                "borrow_date": str(borrow_date),
                                "due_date": str(due_date),
                                "total": total
                            })

                            i["book_quantity"] -= 1
                            current_user["balance"] -= total

                            print("Book borrowed successfully")
                            print(f"Borrow date: {borrow_date}")
                            print(f"Due date: {due_date}")
                            print(f"Total cost: {total}")

                            Library.__bookupdate()
                            Library.__update()
                            break

                    if not found:
                        print("Book not found")  



                if option == "3":
                    return_book = int(input("Enter Book id to return :- "))
                    found = False

                    for i in Library.book_data:
                        if i["book_id"] == return_book:
                            found = True

                            for b in current_user["borrow_book"]:

                                if b["book_id"] == return_book:

                                    today = date.today()
                                    due_date = datetime.strptime(b["due_date"], "%Y-%m-%d").date()

                                    # fine calculation
                                    if today > due_date:
                                        late_days = (today - due_date).days
                                        fine = late_days * 10
                                    else:
                                        fine = 0

                                    # deduct fine
                                    current_user["balance"] -= fine

                                    # return book
                                    i["book_quantity"] += 1

                                    # remove from borrowed list
                                    current_user["borrow_book"].remove(b)

                                    print("Book returned successfully")
                                    print(f"Fine: {fine}")

                                    Library.__bookupdate()
                                    Library.__update()
                                    break

                            break

                    if not found:
                        print("Book not found")




                if option == "4":
                    amount = int(input("How much you want to deposit :- "))
                    if amount > 10000 or amount < 0:
                        print("Sorry the amount is too much you can deposit below 10000 and above 0")
                    else:
                        current_user['balance'] += amount
                        Library.__update() 
                        print("Amount despoit successfully")  



                elif option == "5":
                    print("Your Information are \n\n")

                    for i in current_user:
                        print(f"{i} : {current_user[i]}")




                elif option == "6":
                    print("You cannot change the age, accountNo. and your balance")

                    print("Fill the details for change and leave it empty if no change")    

                    newdata = {
                        "name" : input("Please tell new name or press enter :- "),
                        "email" : input("Please tell your new email and press enter to skip :- "),
                        "password" : input("Enter new password or press enter to skip :- ")
                    } 

                    if newdata["name"] == "" :
                        newdata["name"] = current_user["name"]
                    if newdata["email"] == "" :
                        newdata["email"] = current_user["email"]
                    if newdata["password"] == "" :
                        newdata["password"] = current_user["password"]         


                    newdata["name"] = current_user["name"] 
                    newdata["email"] = current_user["email"] 
                    newdata["password"] = current_user["password"] 


                    for i in newdata:
                        if newdata[i] == current_user[i]:
                            continue
                        else:
                            current_user[i] = newdata[i]    
                        
                    Library.__update()                   
                    print("Details updated successfully")


                elif option == "7":
                    check = input("Press y if you actually want to delete your account or press n to bypass :- ")

                    if check == 'n' or check == 'N':
                        print("Bypassed")
                    else:
                        index = Library.data.index(current_user)    
                        Library.data.pop(index)
                        print("Account deleted successfully")        
                        Library.__update()



                elif option == "8":
                        print("Account has been Logout successfully")
                        return




user = Library()

print("\n==== Library Management System ====")
print("Press 1 to create account")
print("Press 2 to login as student")
print("Press 3 to login as admin")
print("Press 4 to exit")

choice = input("Tell your response: ")

if choice == "1":
    user.createaccount()
    
elif choice == "2":
    user.loginaccount()

elif choice == "3":
    user.adminaccount()

elif choice == "4":
    print("System closed. Goodbye!")

else:
    print("Invalid option, try again")