from sys import argv as av
from time import sleep

from src.exc import invalid_arguments_amount
from src.timeblockist import set_priorities

def main():
    av_len = len(av)
    av_len_range = range(0, av_len)
    if ((av_len - 1) % 4) != 0:
        raise invalid_arguments_amount("\nEnter 4 arguments:\n1)Label\n2,3,4)Time segment for BLUE, YELLOW and RED priorities")

    while (1):
        for i in av_len_range[1::4]:
            label = av[i]
            blue = av[i + 1]
            yellow = av[i + 2]
            red = av[i + 3]
            set_priorities(label, blue, yellow, red)
        sleep(30)

if __name__ == '__main__':
    main()
