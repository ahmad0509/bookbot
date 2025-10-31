import sys
from stats import count_words
from stats import get_book_text
from stats import get_char_count
from stats import sort_char_counts

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path=sys.argv[1]
    text=get_book_text(file_path)
    word_count=count_words(text)

    char_frequency=get_char_count(text)
    sorted_chars=sort_char_counts(char_frequency)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
