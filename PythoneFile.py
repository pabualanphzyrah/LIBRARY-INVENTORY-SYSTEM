print("==============================")
print("   LIBRARY INVENTORY SYSTEM")
print("==============================")

books = []

while True:
    print("\nMain Menu")
    print("1. Add Book")
    print("2. View All Books")
    print("3. View Book by ID")
    print("4. View Book by Category")
    print("5. Edit Book")
    print("6. Delete Book")
    print("7. Exit")
    

    choice = input("\n   Choice (1-7): ")

    # ADD BOOK
    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        category = input("Category: ")

        # Check if book ID already exists
        exists = False
        for book in books:
            if book["id"] == book_id:
                exists = True
                break

        if exists:
            print("Book ID already exists.")
        else:
            books.append({
                "id": book_id,
                "title": title,
                "author": author,
                "category": category
            })
            print("Book added.")

    # VIEW ALL BOOKS
    elif choice == "2":
        if len(books) == 0:
            print("No books in library.")
        else:
            print("\nAll Books")
            for book in books:
                print("ID:", book["id"], "| Title:", book["title"],
                      "| Author:", book["author"], "| Category:", book["category"])
            print("-------------------------------------------------------------")

    # VIEW BOOK BY ID
    elif choice == "3":
        book_id = input("Book ID: ")
        found = False
        for book in books:
            if book["id"] == book_id:
                print("\nID:", book["id"], "| Title:", book["title"],
                      "| Author:", book["author"], "| Category:", book["category"])
                found = True
                break
        if not found:
            print("Book not found.")

    # VIEW BOOK BY CATEGORY
    elif choice == "4":
        print("\nSelect Category:")
        print("1. Fiction")
        print("2. Non-Fiction")
        print("3. Science")
        print("4. History")
        print("5. Technology")

        cat_choice = input("Enter category number (1-5): ")

        categories = {
            "1": "Fiction",
            "2": "Non-Fiction",
            "3": "Science",
            "4": "History",
            "5": "Technology"
        }

        category_name = categories.get(cat_choice)

        if category_name:
            found = False
            print(f"\nBooks under category: {category_name}")
            for book in books:
                if book["category"].lower() == category_name.lower():
                    print("ID:", book["id"], "| Title:", book["title"],
                          "| Author:", book["author"])
                    found = True
            if not found:
                print("No books found in this category.")
        else:
            print("Invalid category choice.")

    # EDIT BOOK
    elif choice == "5":
        book_id = input("Book ID to update: ")
        found = False
        for book in books:
            if book["id"] == book_id:
                new_title = input("New Title (leave blank to keep '{}'): ".format(book["title"]))
                new_author = input("New Author (leave blank to keep '{}'): ".format(book["author"]))
                new_category = input("New Category (leave blank to keep '{}'): ".format(book["category"]))
                if new_title != "":
                    book["title"] = new_title
                if new_author != "":
                    book["author"] = new_author
                if new_category != "":
                    book["category"] = new_category
                print("Book updated.")
                found = True
                break
        if not found:
            print("Book not found.")

    # DELETE BOOK
    elif choice == "6":
        book_id = input("Book ID to delete: ")
        found = False
        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                print("Book deleted.")
                found = True
                break
        if not found:
            print("Book not found.")

    # EXIT
    elif choice == "7":
        print("\n|-------------------------------------------------------|")
        print("    Thank you for using the Library Inventory System!")
        print("|-------------------------------------------------------|")
        break
