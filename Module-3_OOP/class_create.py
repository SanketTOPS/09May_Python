class studninfo:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("This is getdata!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


#Object of class
st=studninfo()
print(st.stid)
print(st.stnm)
st.getdata()
st.getsum(34,65)
