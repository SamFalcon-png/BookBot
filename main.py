import sys
from stats import wordcount,get_book_text,count_char,sort_key

def main(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    text = get_book_text(book_path)
    word_total = wordcount(text)
    print("----------- Word Count ----------")
    print(f"Found {word_total} total words")
    
    char_counts = count_char(text)
    # Filter only alphabetical characters
    alpha_counts = {l: n for l, n in char_counts.items() if l.isalpha()}
    sorted_chars = sort_key(alpha_counts)
    
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
    
if __name__ == "__main__":
   if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   else:
      main(sys.argv[1])