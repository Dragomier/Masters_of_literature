import re

def read_dictionary(text_path):
    words = []
    how_many_lines = 0

    with open(text_path, "r", encoding = "utf-8") as file:
        for line in file:
            how_many_lines += 1
            line = line.strip()
            for word in line.split(", "):
                words.append(word)

    return {"title": "DICTIONARY", "list_of_words": words, "how_many_lines": how_many_lines}

def clean_text_line(line):
    line = re.sub(r'[-.,!?;:()"\'«»_–—]', ' ', line)
    line = re.sub(r'\s+', ' ', line)
    line = re.sub(r'é', 'e', line)
    words = [word.lower() for word in line.strip().split() if word]

    return words

def read_work(text_path):
    words = []
    how_many_lines = 0
    with open(text_path, "r", encoding = "utf-8") as file:
        for line in file:
            how_many_lines += 1
            line = line.strip()
            for word in clean_text_line(line):
                words.append(word)
    return {"title": "WORK", "list_of_words": words, "how_many_lines": how_many_lines}
