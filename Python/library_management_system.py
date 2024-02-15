class Library:
    def __init__(self, file_path="books.txt"):
        self.file_path = file_path
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books_list = self.file.read().splitlines()
        for book_info in books_list:
            book_details = book_info.split(',')
            if len(book_details) == 4:
                title, author, release_date, num_pages = book_details
                print(f"Title: {title}, Author: {author}, Release Date: {release_date}, Number of Pages: {num_pages}")
            else:
                print(f"Invalid book info format: {book_info}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        books_list = self.file.read().splitlines()
        updated_books_list = [book_info for book_info in books_list if title_to_remove not in book_info]

        self.file.seek(0)
        self.file.truncate()
        self.file.writelines("\n".join(updated_books_list))
        print("Book removed successfully!")

lib = Library()

while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")