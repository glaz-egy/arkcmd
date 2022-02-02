class rconConfig:
    def __init__(self, conf):
        self.__conf = conf
        self.__addr = self.__conf['addr']
        self.__port = int(self.__conf['rconPort'])
        self.__password = self.__conf['adminPass']

    @property
    def addr(self):
        return self.__addr
    
    @property
    def port(self):
        return self.__port
    
    @property
    def password(self):
        return self.__password
