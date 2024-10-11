class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author
    self._is_checked_out = False
  def CheckOut(self):
# this method returns false if the book is already checked outindicating that the checkout operation was no successful
    if self._is_checked_out:
      return False
    self._is_checked_out = True
    return True
  def return_book(self):
    if not self._is_checked_out:
      return False
    self._is_checked_out = False
    return True
class Library:
  def __init__(self):
    self._books = []
  def add_book(self,book):
   if book.title not in self.title:
     self._books.append(book)
  def check_out_title(self,title):
    for book in self._books:
      if book.title == title:
          if book.check_out():
                    print(f"Checked out '{title}' successfully.")
                    return
          else:
                    print(f"'{title}' is already checked out.")
                    return
      print(f"Book '{title}' not found in the library.")
    
  def return_book(self,title):
    for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}' successfully.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
    print(f"Book '{title}' not found in the library.")
  def list_available_books(self):
   for book in self._books:
      print(book.title)