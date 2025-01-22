def is_an_ip_number(input_number):
    if input_number in range(0, 256):
        return True
    else:
        return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    for separate_result in dot_separated_words:
        try:
            int(separate_result)

        except ValueError:
            return False

    while len(dot_separated_words) > 0:
        
        word = int(dot_separated_words.pop())
        if not is_an_ip_number(word):
            return False

    return True

#print(is_dot_separated_ip_address("1.1.1.a"))