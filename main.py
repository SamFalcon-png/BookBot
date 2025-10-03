from stats import wordcount
def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text 
def main():
   booktext = get_book_text("books/frankenstein.txt")
   total = wordcount(booktext)
   print(f"Found {total} total words")
main()
    
