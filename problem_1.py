def sub_string(input_string):
    characters = {input_string[0]}
    count = 1
    for ch in input_string[1:]:
        if ch in characters:
            break
        else:
            count += 1
            characters.add(ch)
    print(f"Length of substring: {count}")
    return input_string[:count]

# print(sub_string("abcda".lower()))

print(sub_string(input(str("Enter String Input:")).lower()))