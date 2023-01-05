import json

def chatbot():
    # Load the vocabulary from the JSON file
    with open("vocab.json", "r") as f:
        definitions = json.load(f)

    # infinite loop to keep the chatbot running
    while True:
        # get user input
        user_input = input("Enter a word or phrase: ")

        # check if user input is in the dictionary
        if user_input in definitions:
            # print the definition
            print("")
            print(definitions[user_input])
        elif user_input in ["never mind", "forget it", "idk", "i don't know"]:
            # skip and start the loop again
            continue
        elif user_input.startswith("what I meant by") or user_input.startswith("is"):
            # get the word the user is asking about
            word = user_input.split("by ")[-1] if user_input.startswith("what I meant by") else user_input.split("is ")[-1]
            # get the definition from the user
            definition = input(f"What does '{word}' mean? ")
            # add the definition to the dictionary
            definitions[word] = definition
            print("")
            print("Got it, I'll remember that.")

            # Save the updated vocabulary to the JSON file
            with open("vocab.json", "w") as f:
                json.dump(definitions, f)
        else:
            # print that the chatbot didn't understand
            print("")
            print("Sorry, I didn't understand that.")


# start the chatbot
chatbot()