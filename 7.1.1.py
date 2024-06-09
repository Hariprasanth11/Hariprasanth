def frequency(string):
    f_dict = {}
    for char in string:
        if char in f_dict:
            f_dict[char] += 1
        else:
            f_dict[char] = 1
    
    return f_dict
    
string = "hello world"
frequency = frequency(string)
print(frequency)
