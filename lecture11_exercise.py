'''
Create a dictionary and take input from the user and return the meaning of the word from the dictionary if the word is present in the dictionary.
'''
word = input(
    "Enter a word from hypnopedia, piebald, dauntless, syncope, sinsyne: ")

dictionary = {"hypnopedia": "the act or process of learning during sleep by listening to recordings repeatedly.",
              "piebald": "having patches of black and white or of other colors; parti-colored.",
              "dauntless": "fearless; intrepid; bold.",
              "syncope": "the contraction of a word by omitting one or more sounds from the middle.",
              "sinsyne": "from that time; since then."}

print(dictionary[word.lower()].capitalize())
