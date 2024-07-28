films= {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

while True:

    choice = input('What film would you like to watch?("q" to quit): ').strip().lower().title()

    if choice in films:
        age = int(input('How old are you?: ').strip())
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("Enjoy the film!\n")
                films[choice][1] -= 1
            else:
                print('sorry! we are sold out!\n')
        elif age < films[choice][0]:
            print("You are too young to watch this film.")
        else:
            print('invalid input')

    elif choice == 'Q':
        break

    else:
        print('We do not have that film...')
