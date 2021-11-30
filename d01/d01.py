from sys import argv

if __name__ == '__main__':
    try:
        print(argv[-1])
    except:
        print(argv[0])