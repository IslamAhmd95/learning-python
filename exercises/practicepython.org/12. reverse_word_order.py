"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

"My name is Michele"  to "Michele is name My"
"""

def reserve_words(sentence: str):
    return " ".join(sentence.split()[::-1])

"""
sentence.split() → Converts the sentence into a list of words.
[::-1] → Reverses the list.
" ".join(...) → Joins the reversed words back into a string.
"""
user_input = input("Enter a long string containing multiple words: ").strip()
print(reserve_words(user_input))