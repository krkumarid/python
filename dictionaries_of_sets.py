"""
Put this data in a suitable data structure.

Science Fiction: Journey to the center of the earth, Day of the Triffids
Drama: A Tale of Two cities, Moby Dick

Assume:
1. Categories are unique( cannot have two  categories with the same  name)
2. Book titiles are unique
3. We want to be able to easily determine which boks are in a given category
4. The order of book titles doesn't matter
5. We want to be able to quickly determine if a given book is present in the given category
6. We want to be ablel to easily add books to a category.


Now Programmically add this book

Science Fiction: The War of the Worlds



Docstring for dictionaries_of_sets
"""

def find_book( library,book):
    for books in library.values():
        if book in books:
            return True
    return False
def add_book( library,category,title):
    if not category in library: 
        library[category] = set()# Adding an empty set if the key doesn't exists in the list
    
    library[category].add(title) # Using the add method of set
 
def main():

    library = {
          "Science Fiction":{"Journey to the center of the earth","Day of the Triffids"},
          "Drama":{"A Tale of Two cities","Moby Dick"},
    }
  
    add_book( library,category="Science Fiction",title="The War of the World")

    for category in library:
        books = library[category]
       
        print( category + ": ",end=" ") 
        print( ", ".join(books))
        print()

    print(find_book( library=library,book="The War of the Worlds"))
 
main()