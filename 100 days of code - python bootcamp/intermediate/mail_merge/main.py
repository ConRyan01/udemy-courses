
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace('[name]', stripped_name)
        with open(f"Output/ReadyToSend/{stripped_name}_letter.txt", mode='w') as file:
            file.write(new_letter)
