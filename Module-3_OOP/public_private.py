class student:
    #private
    __stid=12
    __stnm="Sanket"

    #private method
    def __getdata(self):
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def printdata(self):
        self.__getdata()


st=student()
#st.getdata()
st.printdata()
