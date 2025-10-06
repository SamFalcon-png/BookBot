
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
def sort_key(char_dict):
   
    dict_list = [{"char": l, "num": n} for l, n in char_dict.items()]

    dict_list.sort(key=lambda item: item["num"], reverse=True)
    return dict_list
    