def count_words(text):
    word_list=text.split()
    return len(word_list)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents=f.read()
        return file_contents

def get_char_count(book_text):
    text=book_text.lower()
    char_count={}
    for char in text:
        char_count[char]=char_count.get(char,0)+1
    return char_count
    
def sort_on(char_freq):
    return char_freq["num"]

def sort_char_counts(char_count):
    char_list=[]
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char":char, "num":count})
    char_list.sort(key=sort_on,reverse=True)
    return char_list