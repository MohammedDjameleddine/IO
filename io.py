import random, string

def main():
    # read contents of file student_names.txt in string variable
    with open("student_names.txt", "r") as f:
        student_names = f.read()
    # Write a list of random names to the file
    with open("student_names.txt", "w") as f:
        for i in range(10):
            f.write(random.choice(string.ascii_letters, 10))

    # print first n lines in student_names.txt
    with open("student_names.txt", "r") as f:
        for i in range(10):
            print(f.readline())

    # print last n lines in student_names.txt
    with open("student_names.txt", "r") as f:
        lines = f.readlines()
        for i in range(10):
            print(lines[-i])

    # check if name x is in student_names.txt
    with open("student_names.txt", "r") as f:
        for line in f:
            if "x" in line:
                print(line)
                break
        print("x not found")

    # generate files A.txt, B.txt, ..., Z.txt
    for i in range(26):
        with open(chr(ord("A") + i) + ".txt", "w") as f:
            f.write(chr(ord("A") + i))


if __name__ == '__main__':
    main()