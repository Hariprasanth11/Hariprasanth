def characters(string):
    frequency_dict = {}
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    result = ''.join([char for char in string if frequency_dict[char] == 1])
    
    return result

string = "hello world"
unique_character = characters(string)
print(unique_character)
