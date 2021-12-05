import os
import random
from fnmatch import fnmatch

content_folder = "/home/masoko/git/funmasokonet.github.io/content/posts"
pattern = "*.md"


class joke:
    def __init__(self, joketext, category):
        self.joketext = joketext
        self.category = category


jokes = []


def get_file_names(folder, mask):
    joke_files = []
    for path, subdirs, files in os.walk(folder):
        for name in files:
            if fnmatch(name, mask):
                joke_files.append(os.path.join(path, name))
    return joke_files


def get_jokes(joke_files):
    for joke_file in joke_files:
        with open(joke_file) as f:
            lines = f.readlines()
            joke_text = []
            joke_cat = ""
            for line in lines:
                if "Category:" in line:
                    joke_cat = line.split(":")[1].strip()
                elif ("Title:" in line) or ("Date:" in line) or ("Tags:" in line) or (line.strip() == ""):
                    pass
                else:
                    joke_text.append(line)
            text = "".join(joke_text).replace("&minus;", "-")
            jokes.append(joke(text, joke_cat))
    return jokes


joke_files_list = get_file_names(content_folder, pattern)
jokes = get_jokes(joke_files_list)
random_joke = random.choice(jokes)

print(random_joke.joketext)
