
def wordcount(bookwords):
    words = bookwords.split()
    return len(words)
def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text 
def count_char(words):
    char = {}
    cased_words = words.lower()
    for word in cased_words:
        for i in word:
            if i not in char:
                char[i]=0
                char[i]+=1
            else:
                char[i]+=1
    return char     

    