def the_second_function_is_true():
    if the_first_function_is_not_true():
        return not True
    elif not the_first_function_is_not_true():
        return not not True

def the_first_function_is_not_true():
    if the_second_function_is_true():
        return True
    elif not the_second_function_is_true():
        return not True


print(the_second_function_is_true())
