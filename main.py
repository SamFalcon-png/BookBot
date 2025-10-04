from stats import wordcount,get_book_text,count_char

def main():
   booktext = get_book_text("books/frankenstein.txt")
   total = wordcount(booktext)
   letters = count_char(booktext)
   print(f"Found {total} total words")
   print(letters)

main()
    
