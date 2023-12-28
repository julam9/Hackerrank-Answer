##What's your name?
# Objective : Given first and last name, print the first and last name in desired format
def print_full_name(first, last):
    #using string format
    print("Hello {0} {1}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
