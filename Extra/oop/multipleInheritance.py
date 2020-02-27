class OperatingSystem:
    multitasking = True

class Apple:
    website = 'www.apple.com'

class MacBook(OperatingSystem,Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is multitasking operating system visit {} for more details.".format(self.website))


macbook=MacBook()
# macbook.__init__()