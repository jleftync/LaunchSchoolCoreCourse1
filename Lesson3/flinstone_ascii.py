def add_hyphen(input_string):
    hyphen_counter = 0
    while hyphen_counter < 10:
        input_string = "-" + input_string
        print(input_string)
        hyphen_counter += 1
       
add_hyphen('The Flintstones Rock!')