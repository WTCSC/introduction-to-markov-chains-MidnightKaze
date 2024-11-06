import random
import argparse

def get_text(filepath):
    with open(filepath, 'r') as file:
        text = " ".join([i.strip() for i in file.readlines()])
    return text

def generate_the_chain(text):
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

    return transitions
                

def generate_text(start_word, num_words):
    current_word = start_word
    result = [] # Literally building the sentence word by word
    start_sentence = True # The check for the first word of a sentence

    for _ in range(num_words):
        if start_sentence: # If it's the start of a sentence
            result.append(current_word.capitalize()) # Capitalize the word and add it to the list
            start_sentence = False # Can't capitalize any following words until the next sentence
        else:
            if current_word in '.?!,:;"':
                result[-1] = result[-1] + current_word
            else: 
                result.append(current_word) # Else add the word as is
                    # Allowing the words to be added as they are will allow for proper nouns to be correctly processed and whatnot
        
        if current_word in transitions: # Finishes out the rest of the sentence contruction
            current_word = random.choice(transitions[current_word])
        else:
            break
  
    return " ".join(result) # Joins all the words with a space :)

filepath = input("Enter the path to the text file: ")
start_word = input("Enter a starting word: ")
num_words = int(input("Enter the number of words to generate: "))

text = get_text(filepath)

transitions = generate_the_chain(text)

print (generate_text(start_word, num_words))
