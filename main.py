num = int(input('Enter any number: '))

i = 2

isprime = True

if num == 1:
    print('It is neither a prime nor a composite number.')
else:
    while i != num:
        if num % i == 0:
            isprime = False
            break
        else:
            i += 1

    if isprime:
        print('Your number {} is a prime number'.format(num))
    else:
        print('Your number {} is not a prime number'.format(num))

