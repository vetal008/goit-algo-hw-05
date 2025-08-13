from colorama import Fore, Style
"""
Код взятий із попереднього дз і він виконує абсолютне ті ж самі
команди і  дії. Але в кожній окремій функції окрім декоратора
не відбувається жодної перевірки на помилку 'try, except'
"""

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            if func.__name__ == 'get_phone' or func.__name__ == 'remove_number':
                return Fore.RED + 'Waiting for 1 param([name])' + Style.RESET_ALL
            elif func.__name__ == 'add_contact' or func.__name__ == 'change_phone':
                return Fore.RED + 'Waiting for 2 params([name] [phone])' + Style.RESET_ALL
        except TypeError as exception:
            return Fore.RED + str(exception) + Style.RESET_ALL
        except ValueError:
            return Fore.RED + 'No phone numbers found' + Style.RESET_ALL
        except KeyError:
            return Fore.RED + 'No contacts with that name.' + Style.RESET_ALL
    return inner

def user_input(mes_to_user):
    first_param, *args = input(mes_to_user).split()
    first_param = first_param.lower()
    return first_param, *args

def greeting():
    print_mes = Fore.YELLOW +  "Hi! I`m a simple bot which works with phone numbers.\n    " + Style.RESET_ALL +  "You can have some help: write 'help'"
    return print_mes

@input_error
def get_phone(phone_numbers, *args):
    if len(args) != 1:
        raise IndexError
    else:
        return f"{args[0]} number: {phone_numbers[args[0]]}"

@input_error
def get_all_phones(phone_numbers, *args):
    if phone_numbers:
        return [x for x in phone_numbers.items()]
    else:
        raise ValueError

@input_error
def add_contact(phone_numbers, *args):
    if not args[0].isalpha():
        raise TypeError('Only alpha characters are allowed in [name].')
    elif not args[1].isdigit():
        raise TypeError('Only digit numbers are allowed in [phone].')
    elif (len(args)) > 2:
        raise IndexError
    else:
        phone_numbers[args[0]] = int(args[1])
        return Fore.YELLOW + 'Contact added.' + Style.RESET_ALL

@input_error
def change_phone(phone_numbers, *args):
    if not args[0].isalpha():
        raise TypeError('Only alpha characters are allowed in [name].')
    elif args[0] not in phone_numbers:
        raise KeyError
    elif not args[1].isdigit():
        raise TypeError('Only digit numbers are allowed in [phone].')
    elif (len(args)) > 2:
        raise IndexError
    else:
        phone_numbers[args[0]] = int(args[1])
        return Fore.YELLOW + 'Contact changed.' + Style.RESET_ALL

@input_error
def remove_number(phone_numbers, *args):
    del phone_numbers[args[0]]
    return Fore.YELLOW + 'Contact removed.' + Style.RESET_ALL

def help_command():
    help_message = Fore.YELLOW + "Use next commands:\n"  + Style.RESET_ALL + \
    "    'add' to add a number.(add [name] [number])\n\
    'change' to change number.(change [name] [new number])\n\
    'phone' to get a phone number.(phone [name])\n\
    'all' to get all numbers.\n\
    'remove' to remove a number(remove [name]).\n\
    'close' or 'exit' or 'quit' to exit the bot."
    return help_message

def main():
    phone_numbers = dict()
    print(Fore.BLUE + 'Welcome to my first bot!' + Style.RESET_ALL)
    while True:

        first_param, *args = user_input(Fore.BLUE + 'Enter a command: ' + Style.RESET_ALL)
        match str(first_param):
            case 'greeting':
                print(greeting())
            case 'help':
                print(help_command())
            case 'add':
                print(add_contact(phone_numbers, *args))
            case 'change':
                print(change_phone(phone_numbers, *args))
            case 'phone':
                print(get_phone(phone_numbers, *args))
            case 'remove':
                print(remove_number(phone_numbers, *args))
            case 'all':
                number_list = get_all_phones(phone_numbers, *args)
                if type(number_list) == str:
                    print(number_list)
                elif type(number_list) == list:
                    print(*number_list, sep='\n')
            case 'close' | 'exit' | 'quit':
                print(Fore.YELLOW + 'Goodbye!' + Style.RESET_ALL)
                break
            case _:
                print(Fore.RED + "Invalid command. Print 'help' for have some help" + Style.RESET_ALL)

if __name__ == '__main__':
    main()

"""
py fourth_exercise.py
"""