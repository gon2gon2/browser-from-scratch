from url import URL
from browser import Browser

if __name__ == "__main__":
    import sys
    import tkinter

    # url = URL(sys.argv[1])
    # browser = Browser().load(url=url)
    browser = Browser().show_font()
    tkinter.mainloop()
