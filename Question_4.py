# Start

strings = []

while True:
    text = input("Enter string: ")

    if text == "quit":
        break

    strings.append(text)

reversed_match_found = False

for text in strings:
    reversed_text = text[::-1]

    if reversed_text in strings:
        reversed_match_found = True
        break

if reversed_match_found:
    print("Reversed match found")
else:
    print("No reversed match found")

# Stop