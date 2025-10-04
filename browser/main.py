from url import URL
from util import load

if __name__ == "__main__":
    import sys

    load(URL(sys.argv[1]))
