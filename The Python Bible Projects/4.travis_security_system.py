
known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

print(len(known_users))

while True:
    print("Hi! my name is Travis")
    name = input("What is your name? (or 'q' to quit): ").strip().lower().capitalize() #good to use strip to deal with accidental extra spaces

    if name in known_users:
        print("name recognized")
        remove=input("would you like to be removed from the system (y/n): ").lower().strip()

        if remove == "y" or "yes":
            known_users.remove(name)
            print(known_users)
        elif remove == "n" or "no":
            print("No problem, I didn't want you to leave anyway!")

    elif name == 'Q':
        break

    elif name not in known_users: 
        print(f"Hmm... I don't think I have met you yet, {name}")
        add_me = input("Would you like to be added to the system (y/n): ").strip().lower()
        if add_me is 'y' or 'yes':
            known_users.append(add_me)
            print(known_users)

    else:
        print('error: invalid input')
    