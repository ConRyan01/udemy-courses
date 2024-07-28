import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            
            # Keeps shift amount within range of alphabet index
            if cipher_direction == 'encode':
                while new_position > 25:
                    new_position = new_position - 26
            
            elif cipher_direction == 'decode':
                while new_position < 0:
                    new_position = new_position + 26

            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    user_choice = input('Would you like to go again? Type yes or no: ').lower()

    if user_choice == 'yes':
        should_continue = True
    elif user_choice == 'no':
        should_continue = False

print('Goodbye')