import random
import argparse
import re

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
text = "Akina woke up at the crack of dawn. A soft white cat and black dog rested next to her. Outside, snow gently fell from the sky. Each snowflake makes a small twinkle as it hits the ground. She had about two hours until class started and decided it was still too early to wake up for morning training."
transitions = {} # Just so u remember this is the word key dictionary thingy

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""  
# Note to self: u probably don't wanna include ' since that's usually APART of the word itself
# Another note to self: u might wanna make a tokener function and a split function for the sake of ur sanity
words = re.split(r"\s+", text) # Yknow regular expressions kind of suck but I'll make it work lol
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""
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

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""
print(generate_text("a", 20))