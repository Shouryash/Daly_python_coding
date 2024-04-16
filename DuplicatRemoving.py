
Sentence = input("Enter the sentence: ")
output = ""
Sentence2 = list(Sentence)
print(Sentence2)

for I in Sentence2:
    if I not in output:

        output += I
print("Output without duplicates:",output)


# this is second method

Sentence = input("Enter the sentence: ")

# Remove duplicates and sort the characters
unique_chars = sorted(set(Sentence))

# Join the sorted characters back into a string
output = ''.join(unique_chars)

print("Output without duplicates, sorted:", output)
