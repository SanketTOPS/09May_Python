class master:
    def getheader(self,menu): #original
        print("This is Header Part:",menu)


class homepage(master):
    def getheader(self, menu): #xerox
        return super().getheader(menu)

class aboutpage(master):
    def getheader(self, menu):
        return super().getheader(menu)


h=homepage()
h.getheader("HOME")

a=aboutpage()
a.getheader("ABOUT")
