import base

class DeathKnight(base.BaseCharacter):
    def __init__(self):
        self._base=base.BaseCharacter(1,2,3,4,5)

x=DeathKnight()
print(dir(x))
