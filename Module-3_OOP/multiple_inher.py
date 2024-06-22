class sanket:
    sid=0
    ssub=""

    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.ssub=input("Enter Sanket's Subject:")

class mitesh:
    mid=0
    msub=""

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.msub=input("Enter Mitesh's Subject:")

class nirav:
    nid=0
    nsub=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")


class tops(sanket,mitesh,nirav):
    def printdata(self):
        print("----------Sanket's Data---------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Subject:",self.ssub)
        print("----------Mitesh's Data---------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Subject:",self.msub)
        print("----------Nirav's Data---------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)


tp=tops()
tp.s_getdata()
tp.m_getdata()
tp.n_getdata()
tp.printdata()