# Start

def camel_to_hyphen(text: str) -> str:
    result = ""

    for char in text:
        if char.isupper():
            result += "-"
            result += char.lower()
        else:
            result += char

    return result

print(camel_to_hyphen("helloPython")) # hello-python
print(camel_to_hyphen("myVariableName")) # my-variable-name
print(camel_to_hyphen("python")) # python
print(camel_to_hyphen("aBigTest")) # a-big-test

# Stop