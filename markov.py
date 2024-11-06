import random
import argparse

def get_text(filepath):
    with open(filepath, 'r', errors="ignore") as file:
        text_file = " ".join ([i.strip for i in file.readlines()])
    return text_file

parser = argparse.ArgumentParser()
parser.add_argument("text")
parser.add_argument("start")
parser.add_argument("length", type=int)
args = parser.parse_args()

text = get_text(args.text) 
words = text.split()
transitions = {}
tokens = []
token = ""

for word in words:
    for char in word: # Breaks the words in the word list into a single char
        if char in '.?!,:;"': # So it can then check if its a punctuation mark
            if token:
                tokens.append(token)
                token = ""
            tokens.append(char)
        else:
            token += char
    if token:
        tokens.append(token)
        token = ""

for i in range(len(tokens) - 1):
    token = tokens[i]
    next_token = tokens[i + 1]

    if token not in transitions:
        transitions[token] = []
    transitions[token].append(next_token)
                

def generate_text(start_word, num_words):
    current_word = start_word
    result = [] # Literally building the sentence word by word
    start_sentence = True # The check for the first word of a sentence

    for _ in range(num_words):
        if start_sentence: # If it's the start of a sentence
            result.append(current_word.capitalize()) # Capitalize the word and add it to the list
            start_sentence = False # Can't capitalize any following words until the next sentence
        else: 
            result.append(current_word) # Else add the word as is
                # Allowing the words to be added as they are will allow for proper nouns to be correctly processed and whatnot
        
        if current_word in transitions: # Finishes out the rest of the sentence contruction
            current_word = random.choice(transitions[current_word])
        else:
            break

    return " ".join(result) # Joins all the words with a space :)

print(generate_text(args.start, args.length))
