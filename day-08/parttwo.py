def start_dict(number_dict, all_numbers):
    chaser = 0
    for encode in all_numbers:
        if len(encode) == 2:
            number_dict[1] = chaser
        elif len(encode) == 4:
            number_dict[4] = chaser
        elif len(encode) == 7:
            number_dict[8] = chaser
        elif len(encode) == 3:
            number_dict[7] = chaser
        chaser += 1
    return (number_dict)
def decipher_first(number_dict, all_numbers, number_builder):
    #This part is deciphering the top middle character between 1 and 7
    top_top = ""
    for character in all_numbers[number_dict[7]]:
        if character not in all_numbers[number_dict[1]]:
            top_top = character
            break
    number_builder[0] = top_top
    #This part is finding number 6 by comparing it to 7, and then filling in
    #The Top Right by finding out which piece is in 7 but not in 6
    chaser = 0
    top_right = ""
    bottom_right = ""
    for decode in all_numbers:
        if len(decode) == 6:
            count = 0
            for character in all_numbers[number_dict[7]]:
                if character in decode:
                    count += 1
            if count == 2:
                for character in all_numbers[number_dict[7]]:
                    if character not in decode:
                        top_right = character
                        number_dict[6] = chaser
                        break
        chaser += 1
    number_builder[2] = top_right
    #This piece just quickly grabs the bottom right, by figuring out which is not filled in 7 yet
    for character in all_numbers[number_dict[7]]:
        if character not in number_builder:
            bottom_right = character
            break
    number_builder[5] = bottom_right
    # print(all_numbers)
    # print(number_dict)
    # print(number_builder)
    return(number_dict, number_builder)
def decipher_four(number_dict, all_numbers, number_builder):
    chaser = 0
    #This part of the code determines the numbers 0 and 9 in the list based on comparing to 4 which is known
    #If len is 6, and the current number is not already in the dictionary as #6 then it has to be 0 or 9
    #and if they share 3 numbers, its 9, if they share 4 its 9
    for encode in all_numbers:
        if len(encode) == 6 and chaser is not number_dict[6]:
            count = 0
            for character in all_numbers[number_dict[4]]:
                if character in encode:
                    count += 1
            if count == 3:
                number_dict[0] = chaser
            elif count == 4:
                number_dict[9] = chaser
        chaser += 1
    #This solves where the top left and middle middle letter
    #The first if determins the middle middle, as if its in 4 but not 0 it has to be middle, and the other determines that if its not
    #Already been filled in, then the final one has to be the top left
    for character in all_numbers[number_dict[4]]:
        if character not in all_numbers[number_dict[0]]:
            number_builder[3] = character
        elif character in all_numbers[number_dict[0]] and character not in number_builder:
            number_builder[1] = character
    return(number_dict, number_builder)
def final_decipher(number_dict, all_numbers, number_builder):
    #This figures out which is number five, three, and two
    #If it is five, then the top left must already be in the number_build
    #If it is three, there will be 4 matches, but none of them will be the top left
    #If it has 3 matches, it has to be two.
    chaser = 0
    for encode in all_numbers:
        if len(encode) == 5:
            for character in encode:
                if character == number_builder[1]:
                    number_dict[5] = chaser
                    break
        chaser += 1
    for character in all_numbers[number_dict[5]]:
        if character not in number_builder:
            number_builder[6] = character
            break
    chaser = 0
    for encode in all_numbers:
        count = 0
        if len(encode) == 5:
            for character in encode:
                if character in number_builder:
                    count += 1
        if count == 5 and chaser not in number_dict:
            number_dict[3] = chaser
        elif count == 4 and chaser not in number_dict:
            number_dict[2] = chaser
        chaser += 1
    for character in all_numbers[number_dict[2]]:
        if character not in number_builder:
            number_builder[4] = character
    return (number_dict, number_builder)

def sum_string(string):
    sum_digit = 0
    for char in string:
        sum_digit = sum_digit + ord(char)
    return (sum_digit)

def add_number(line, number_dict, all_numbers):
    to_decode = line.split()[11:]
    answer = []
    answer_code = []
    print(to_decode)
    print(all_numbers)
    print(number_dict)
    for puzzle in to_decode:
        # print(puzzle)
        for i in range(10):
            if sorted(puzzle) == sorted(all_numbers[number_dict[i]]):
                # print(i)
                # print(number_dict[i])
                answer_code.append(number_dict[i])
                answer.append(i)
                break
    print(answer_code)
    print(answer)
    if (len(answer) != 4):
        return (-1)
    strings = [str(integer) for integer in answer]
    answer = "".join(strings)
    print(answer)
    return (int(answer))
def check_dict(number_dict):
    check = []
    for number in number_dict:
        if number in check:
            return (-1)
        if number != -1:
            check.append(number)
    return (0)
def num_dict(number_dict):
    check = []
    for number in number_dict:
        if number in check:
            return (-1)
        if number != -1:
            check.append(number)
    return (0)

def start_solve(line):
    all_numbers = line.split()[:10]
    number_dict = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    number_builder = [-1,-1,-1,-1,-1,-1,-1]
    number_dict = start_dict(number_dict, all_numbers)
    number_dict, number_builder = decipher_first(number_dict, all_numbers, number_builder)
    number_dict, number_builder = decipher_four(number_dict, all_numbers, number_builder)
    number_dict, number_builder = final_decipher(number_dict, all_numbers, number_builder)
    if (check_dict(number_dict) == -1):
        print(number_dict)
        print(number_builder)
        print("Ayo Error")
        return (-1)
    if (num_dict(number_builder) == -1):
        print(number_builder)
        print("Ayo Error")
        return (-1)
    return(add_number(line, number_dict, all_numbers))

with open("input.txt", "r") as f:
    Lines = f.readlines()
running_total = 0
count = 0
for line in Lines:
    count += 1
    error_check = start_solve(line)
    if (error_check == -1):
        print("Error")
        break
    running_total += error_check
print(count)
print(running_total)