def asteriskpyr():
    lines = int(input("How many lines of pattern?"))
    count = 1
    pattern = "*"
    for number in range(lines): #check this
        print(count * pattern)
        count +=1

def asterisktri():
    lines = int(input("How many stars at the top?"))
    count = lines
    pattern = "*"
    for number in range(lines):
        print(count * pattern)
        count -= 2

def asteriskchain():
    size = int(input("How many stars per arrow?"))
    many = int(input("How many arrows?"))
    count = 0
    for number in range(many):
        while count < size:
            print(count * "*")
            count += 1
            if count >= size:
                break
        while count > 1:
            print(count * "*")
            count -= 1
            if count <=1:
                break
    print("*")

def dollarpyr():
    size = int(input("How many lines of pattern?"))
    count = 0
    width = (2 * size) + 1
    constant = size
    for number in range(size):
        count += 1
        print((constant * " ") + (count * "$ ") + (constant * " "))
        constant -= 1

def pascals(): #incomplete
    length = int(input("How many lines of Pascal's Triangle?"))
    rows = []
    begin = 1
    rows.append(begin)
    count = 1
    for number in range(length):
        print(rows)
        second = begin * count
        rows.append(second)
        after = second +

def patterns():
    pat = input("Increasing stars(1), decreasing stars (2), repeating pyramids (3), or a pyramid of dollar signs (4)? ")
    if pat == "1":
        asteriskpyr()
    elif pat == "2":
        asterisktri()
    elif pat == "3":
        asteriskchain()
    elif pat == "4":
        dollarpyr()
    else:
        print("Error 404. Pattern not found.")
if __name__ == '__main__':
    print
    patterns()
