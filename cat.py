
word = input("Give your cat a name: ")

def cat_latin(word):
    if word.lower().endswith("y"):
        return (word[:-1] + "iful")
    else:
        return (word + "y")

print(cat_latin(word))