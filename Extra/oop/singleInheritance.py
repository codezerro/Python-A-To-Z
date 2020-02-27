class Apple:
    manufacturer="Apple Inc"
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us ,log on to ",self.contactWebsite)


class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2019

    
    def manufacturerDetails(self):
        print("This MacBook was manufactured in the year {} by {} ".format(self.yearOfManufacture,self.manufacturer))
    

macBook = MacBook()
macBook.manufacturerDetails()
macBook.contactDetails()