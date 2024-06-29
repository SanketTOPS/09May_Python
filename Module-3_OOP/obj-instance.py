class student:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Object of class
"""st=student()
st.getdata()
st.stid=30
st.stnm="Nirav"
st.getdata()"""


#Instance
student().getdata()
student().stid=14
student().stnm="Mitesh"
student().getdata()