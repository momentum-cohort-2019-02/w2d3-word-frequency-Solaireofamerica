import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


# function that returns only words with no formatting
def clean_text(text):
    text = text.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits
    cleaned_text = ""
    for char in text:
        if char in valid_chars:
            cleaned_text += char

    text = cleaned_text
    text = text.replace("\n", " ")
    text = text.lower()
    return text


def print_word_freq(filename):
    """Read in `file` and print out the frequency of words in that file."""
    with open("seneca_falls.txt") as file:
        text = file.read()
    text = text.lower()
    text = clean_text(text)
    words = []

    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)
    total_count = {}

    for char in words:
        total_count[char] = total_count.get(char, 0) + 1

    word_freq = sorted(total_count.items(), key=lambda x: x[1], reverse=True)

    ordered_dict = dict(word_freq)

    for key, value in ordered_dict.items():
        print(key, " | ", value, " * " * value)


print_word_freq("seneca_falls.txt")


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
