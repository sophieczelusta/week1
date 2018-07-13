def addition(a,b):
    print(a + b)

def subtraction(a,b):
    print(a - b)

def multiplication(a,b):
    c = 1
    d = a
    while c < b:
        a = a + d
        c = c + 1
        if c >= b:
            break
    print(a)

def division(x,y):
        c = 0
        d = x
        while d > 0:
            d -= y
            c = c + 1
        print(c)

def exponents(a,b):
    c = 1
    d = a
    while c < b:
        a = a * d
        c = c + 1
        if c >= b:
            break
    print(a)

def modulo(a,b):
    c = 0
    while a >= b:
        a = a - b
        c +=1
    print(a)

def mini(): #minimum
    list = []
    num = 0
    while num != "done":
        num = input("Please enter a number. Type done when you have finished. ")
        list.append(num)
        if num == "done":
            break
    list.sort()
    print(list[0])

def maxi(): #maximum
    list = []
    num = 0
    while num != "done":
        num = input("Please enter a number. Type done when you have finished. ")
        list.append(num)
        if num == "done":
            break
    list.remove("done")
    list = sorted(list)
    last = len(list) - 1
    print(list[last])

def binary(): #binary to base ten
    bi = input("Please enter your binary number. ")
    if "." not in bi:
        length = len(bi)
        count = 0
        answer = 0
        newl = length - 1
        for number in range(length):
            result = int(bi[newl]) * (2 ** count)
            result = float(result)
            answer = result + answer
            count += 1
            newl -= 1
        print(answer)
    else:
        start = bi[0:bi.index(".")]
        end = bi = bi[bi.index("."):len(bi)]
        length = len(start)
        length2 = len(end)
        count = 0
        count2 = 1
        answer = 0
        answer2 = 0
        newl = length - 1
        newl2 = length2 - 1
        for number in range(length):
            result = int(start[newl]) * (2 ** count)
            result = float(result)
            answer = result + answer
            count += 1
            newl -= 1
        for number in range(length2):
            result2 = int(start[newl2]) * (2 ** -count2)
            result2 = float(result2)
            answer2 = result2 + answer2
            count2 += 1
            newl2 -= 1
    print (answer + answer2)

def octal(): #binary to octal
    number = input("Please enter your binary number. Include a decimal. ")
    [predec,postdec] = number.split(".")
    count = 0
    count2 = 0
    side_a = len(predec)
    side_b = len(postdec)
    output = ""
    if side_a % 3 == 1:
        predec = "00" + predec
    elif side_a % 3 == 2:
        predec = "0" + predec
    else:
        predec = predec
    while count < len(predec):
        current = predec[count:count + 3]
        if current == "000":
            output = output + "0"
        elif current == "001":
            output = output + "1"
        elif current == "010":
            output = output + "2"
        elif current == "011":
            output = output + "3"
        elif current == "100":
            output = output + "4"
        elif current == "101":
            output = output + "5"
        elif current == "110":
            output = output + "6"
        elif current == "111":
            output = output + "7"
        else:
            print("Unable to function.")
        count = count + 3
        if count >= len(predec):
            break
    output = output + "."
    if side_b % 3 == 1:
        postdec = postdec + "00"
    elif side_b % 3 == 2:
        postdec = postdec + "0"
    else:
        postdec = postdec
    while count2 < len(postdec):
        current = postdec[count2:count2 + 3]
        if current == "000":
            output = output + "0"
        elif current == "001":
            output = output + "1"
        elif current == "010":
            output = output + "2"
        elif current == "011":
            output = output + "3"
        elif current == "100":
            output = output + "4"
        elif current == "101":
            output = output + "5"
        elif current == "110":
            output = output + "6"
        elif current == "111":
            output = output + "7"
        else:
            print("Error 404. Number not found.")
        count2 = count2 + 3
        if count2 >= len(postdec):
            break
    print(output)

def hexa():
    binary = input("Please enter your binary number. ")
    [predec,postdec] = binary.split(".")
    count = 0
    count2 = 0
    side_a = len(predec)
    side_b = len(postdec)
    output = ""
    if side_a % 4 == 1:
        predec = "000" + predec
    elif side_a % 4 == 2:
        predec = "00" + predec
    elif side_a % 4 == 3:
        predec = "0" + predec
    else:
        predec = predec
    if side_b % 4 == 1:
        postdec = postdec + "000"
    elif side_b % 4 == 2:
        postdec = postdec + "00"
    elif side_b % 4 == 3:
        postdec = "0" + postdec
    else:
        postdec = postdec
    while count < len(predec):
        current = predec[count:count + 4]
        if current == "0000":
            output = output + "0"
        elif current == "0001":
            output = output + "1"
        elif current == "0010":
            output = output + "2"
        elif current == "0011":
            output = output + "3"
        elif current == "0100":
            output = output + "4"
        elif current == "0101":
            output = output + "5"
        elif current == "0110":
            output = output + "6"
        elif current == "0111":
            output = output + "7"
        elif current == "1000":
            output = output + "8"
        elif current == "1001":
            output = output + "9"
        elif current == "1010":
            output = output + "A"
        elif current == "1011":
            output = output + "B"
        elif current == "1100":
            output = output + "C"
        elif current == "1101":
            output = output + "D"
        elif current == "1110":
            output = output + "E"
        elif current == "1111":
            output = output + "F"
        else:
            print("Error 404. Number not found.")
        count += 4
    output = output + "."
    while count2 < len(postdec):
        current = postdec[count2:count2 + 4]
        if current == "0000":
            output = output + "0"
        elif current == "0001":
            output = output + "1"
        elif current == "0010":
            output = output + "2"
        elif current == "0011":
            output = output + "3"
        elif current == "0100":
            output = output + "4"
        elif current == "0101":
            output = output + "5"
        elif current == "0110":
            output = output + "6"
        elif current == "0111":
            output = output + "7"
        elif current == "1000":
            output = output + "8"
        elif current == "1001":
            output = output + "9"
        elif current == "1010":
            output = output + "A"
        elif current == "1011":
            output = output + "B"
        elif current == "1100":
            output = output + "C"
        elif current == "1101":
            output = output + "D"
        elif current == "1110":
            output = output + "E"
        elif current == "1111":
            output = output + "F"
        else:
            print("Error 404. Number not found.")
        count2 += 4
    print(output)



def calc(): #final
    operation = input("Please enter one of the following: simple operations, exponents, conversions. or lists. ")

    if operation == "simple operations":
        operation = input("Please choose addition, subtraction, multiplication, or division. ")

        if operation == "addition":
            uno = float(input("Enter your first number. "))
            dos = float(input("Enter your second number. "))
            addition(uno,dos)

        elif operation == "subtraction":
            uno = float(input("Enter your first number. "))
            dos = float(input("Enter your second number. "))
            subtraction(uno,dos)

        elif operation == "multiplication":
            uno = float(input("Enter your first number. "))
            dos = float(input("Enter your second number. "))
            multiplication(uno,dos)

        elif operation == "division":
            type = input("Would you like to find the remainder only, or divide? ")
            if type == "remainder":
                a = float(input("Enter your first number. "))
                b = float(input("Enter your second number. "))
                modulo(a,b)
            else:
                a = float(input("Enter your first number. "))
                b = float(input("Enter your second number. "))
                division(a,b)
        else:
            print("Error 404. Operation not found.")

    elif operation == "exponents":
        a = float(input("Enter your base number. "))
        b = float(input("Enter your exponent. "))
        exponents(a,b)

    elif operation == "conversions": #conversion operations
        operation = input("Please choose binary to octal, binary to hexadecimal, or binary to base ten. ")
        if operation == "binary to base ten":
            binary()
        elif operation == "binary to octal":
            octal()
        elif operation == "binary to hexadecimal":
            hexa()
        else:
            print("Error 404. Conversion not found.")

    elif operation == "lists":
        type = input("Find the maximum or minimum? ")
        if type == "minimum":
            mini()
        elif type == "maximum":
            maxi()
        else:
            print("Error 404. List not found.")
    else:
        print("Error 404. Function not found.")

if __name__ == '__main__':
    print
    calc()
