def main():
    height = get_height()  # get height
    build_pyramid(height)  # print pyramid


def get_height():
    while True:
        try:
            h = int(input('Height: '))  # get input from user
            if 1 <= h <= 8: # return value if valid
                return h
        except ValueError:
            print("Enter an integer between 1-8 inclusive")


def build_pyramid(height):
    hashes = 1
    space = height - 1
    # build pyramid line by line
    for i in range(height):
        hashes, space = build_line(hashes, space)


def build_line(hashes_num, spaces_num):
    # build line with hasesh and space
    print((" " * spaces_num) + "#" * hashes_num + "  " + "#" * hashes_num + (" " *spaces_num)  )
    return hashes_num + 1, spaces_num - 1
    

main()