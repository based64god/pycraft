import ability
# import stats
# import stats.buffs as buffs
import ability.talents as talents
import ability.glyphs as glyphs

class CharacterError(BaseException):
    pass

class BaseCharacter:
    def __init__(self,abilities,stats,talents,buffs,glyphs):
        print(abilities,stats,talents,buffs,glyphs)
        # for ability in abilities:
        #     if type(ability) != ability.Ability:
        #         raise CharacterError("Imported ability, %s, is not of type Ability()" % ability)
        self.abilities = abilities

        # if type(stats) != stats.Stats:
        #     raise CharacterError("Imported stats, %s, are not of type Stats()" % stats)        
        self.stats = stats

        # for talent in talents:
        #     if type(talent) != talent.Talent:
        #         raise CharacterError("Imported talent, %s, is not of type Talent()" % talent)
        self.talents = talents

        # if len(Glyphs) != 6:
        #     raise CharacterError("You must select 6 glyphs, but selected %d" % len(glyphs))
        # for glyph in Glyphs:
        #     if type(glyph) != glyph.Glyph:
        #         raise CharacterError("Imported glyph, %s, is not of type Glyph()" % glyph)
        self.glyphs = glyphs

        # for buff in buffs:
        #     if type(buff) != buff.Buff:
        #         raise CharacterError("Imported buff, %s, is not of type Buff()" % buff)
        self.buffs = buffs
