def upper_title(input_user):
    '''Функция делает все буква заглавными'''
    input_user = input_user.upper()
    return input_user


def upper_one(input_user):
    '''Функция делает первую букву заглавной'''
    upper_str = input_user
    lst = [word[0].upper() + word[1:] for word in upper_str.split()]
    upper_str = " ".join(lst)
    return upper_str


input_user = input("Введите строку")
print(upper_title(input_user))
print(upper_one(input_user))
