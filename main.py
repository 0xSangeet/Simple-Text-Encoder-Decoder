import random

def encode():
    my_str = input("Enter the string that you want to encode: ")
    og_list = my_str.split()
    new_list = []
    for word in og_list:
        if len(word) <= 2:
            a = word[::-1]
        else:
            first_char = word[0]
            a = word[1:] + first_char
            random_str = randomString() 
            a = random_str + a + random_str 
        new_list.append(a)
    print(f"Encoded string: {' '.join(new_list)}")

def decode():
    my_str = input("Enter the string that you want to decode: ")
    og_list = my_str.split()
    new_list = []
    for word in og_list:
        if len(word) <= 2:
            a = word[::-1]
        else:
            x = word[3:][-4::-1][::-1]
            last_char = x[-1]
            a = last_char + x[:-1]
        new_list.append(a)
    print(f"Decoded string: {' '.join(new_list)}")

def randomString():
    random_char = ''
    for _ in range(3):
        while True:
            random_int = int(random.random() * 100)
            if random_int >= 33 and random_int <= 126:
                random_char += chr(random_int)
                break
    return random_char

choice = int(input("Enter 1 to encode and 2 to decode: "))
if choice == 1:
    encode()
elif choice == 2:
    decode()
else:
    print("Please enter a valid choice!")