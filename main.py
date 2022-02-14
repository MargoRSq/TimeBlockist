from sys import argv as av
from time import sleep

from src.exc import invalid_arguments_amount
from src.timeblockist import set_priorities

def main():
    if ((len(av) - 1) % 4) != 0:
        raise invalid_arguments_amount("\nEnter 4 arguments:\n1)Label\n2,3,4)Time segment for BLUE, YELLOW and RED priorities")

    while (1):
        for i in range(1, (len(av) - 1) // 4 + 1):
            mn = 0 if i == 1 else 3
            print(av[i+mn:i+mn+4])
            set_priorities(av[(i + mn)],
                           av[(i + mn) + 1],
                           av[(i + mn) + 2],
                           av[(i + mn) + 3])
        sleep(30)

if __name__ == '__main__':
    main()
