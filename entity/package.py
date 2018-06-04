'卡包类'

class Package(object):
    def __init__(self,id='',name='undefine'):
        self.__id=id
        self.__name=name
        self.__size=0
        self.__list=[]

    def to_string(self):
        return self.__id+' '+self.__name

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name
    
    def get_size(self):
        return len(self.__list)
