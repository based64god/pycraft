

class BaseCharacter:
    def __init__(self,abilities,stats,talents,buffs):
        self.__abilities = dict(abilities)
        self.__stats = dict(stats)
        self.__talents = dict(talents)
        self.__buffs = dict(buffs)
