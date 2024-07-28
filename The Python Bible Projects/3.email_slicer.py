# get user email address

email = input('what is your email address?: ').strip()

# slice out user name

username = email[:email.index('@')]

# slice out domain name

domain = email[email.index('@')+1:]

# format message

output = f'your username is {username} and your domain is {domain}'

# display output message

print(output)