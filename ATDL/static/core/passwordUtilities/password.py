import hashlib
class Password:
    '''
    mat khau bao gim chu cai tieng anh, chu so, dau gach duoi
    phan loai muc do:
        very week: >=0.9
        week: 0.8 =< P <0.9
        medium: 0.5 <= P <0.8
        strong 0.3 =< P < 0.5
        very strong p < 0.3
    '''
    def __init__(self, password):
        self.password = password
        self.lenght = len(password)
        self.soluongkitu = 0
        self.hasDigit = False
        self.hasUper = False
        self.hasLower = False
        self.hasSym = False
        self.nhan = ''
        self.xacsuat = 0
        self.khonggianmk = 0
        self.andersonTime = 6*30*24*60*60
        self.andersonP = 0
        self.andersonG = 10**5
        self.md5 = None
        #salt bit
        self.salt = '_B1'


    def themmuoi(self):
        self.password = self.password + self.salt

    def hashMD5(self):
        self.md5 = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        return self.md5

    def khongGianMK(self):
        tohop = 0
        if(any(char.isdigit() for char in self.password)):
            self.hasDigit =  True
            tohop += 10
        if(any(char.isupper() for char in self.password)):
            self.hasUper = True
            tohop += 26
        if(any(char.islower() for char in self.password)):
            self.hasLower= True
            tohop += 26
        if(any(char == '_' for char in self.password)):
            self.hasSym = True
            tohop += 1
        self.soluongkitu = tohop
        self.khonggianmk = tohop**self.lenght
        return self.khonggianmk

    def anderson(self):
        '''
        tinh anderson P >= GT/N
        :return: xac suat
        '''
        self.khongGianMK()
        self.andersonP = ((self.andersonTime*self.andersonG)/self.khonggianmk) *100
        return self.andersonP

    def ganNhan(self):
        if (self.andersonP < 0.3):
            self.nhan = 'Very Strong'
        elif (self.andersonP < 0.5):
            self.nhan = 'Strong'
        elif (self.andersonP < 0.8):
            self.nhan = 'Medium'
        elif (self.andersonP < 0.9):
            self.nhan = 'Week'
        else:
            self.nhan = 'Very Week'

    def checkPassword(self):
        self.anderson()
        self.ganNhan()





if __name__ == '__main__':
    mypass = Password("Hoang10asdad")
    mypass.hashMD5()
    mypass.checkPassword()
    print('Độ dài:', mypass.lenght)
    print("Có dấu _ :", mypass.hasSym)
    print('Có chữ số :', mypass.hasLower)
    print('Có chữ cái thường: ', mypass.hasUper)
    print('Có chữ cái hoa :', mypass.hasDigit)
    print('Xác suất: ', mypass.andersonP)
    print('Nhan: ',mypass.nhan)

    print('hash: ', mypass.md5)

