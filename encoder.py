# Liliya Tatchin Encode file.

def encode(password):
    ''' This function takes a string password of 8 characters
        and encodes it by shifting 3 digits up. For example:
        12345555 will change to 45678888
    '''
    if len(password) < 8 or len(password) > 8:
        raise ValueError('Password must be between 8 characters')

    new_password = ""
    # Shift each digit up by 3
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        new_password += str(new_digit)
    return new_password

def decode(encoded_password):
    ''' This function takes the encoded password of 8 characters
        and decodes it by shifting 3 digits down. For example:
        45678888 will change to 12345555
    '''
    pass

def main():
    ''' This is the main function. It will have a looping menu
        with three options:
        1 will refer to the encode function
        and change the password. Then store it.
        2 will reveal the encoded password and the original password.
        3 will exit the loop.
    '''
    encode_loop = True
    password = ''
    encoded_password = ''

    # Create loop
    while encode_loop:
        # Print menu.
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('\nPlease enter an option:', end=' ')
        option = int(input())

        # If else statements.
        if option == 1:
            try:
                # Get password.
                print('Please enter your password to encode:', end=' ')
                password = input()
                # Encode it and store it
                encoded_password = encode(password)
                print('Your password has been encoded and stored!')
            except ValueError as e:
                print(e)
        elif option == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')
        elif option == 3:
            encode_loop = False
        else:
            print('Invalid option. Please try again.')


if __name__ == '__main__':
    main()
