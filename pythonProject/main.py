def emoji_converter(message_input):
    words = message_input.split(" ")
    dictionary = {
        ":)": "😀",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += dictionary.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))
