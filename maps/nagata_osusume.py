from maps.AbstractGakushoku import AbstractGakushoku

class nagata_osusume(AbstractGakushoku):

    def get_menu(self):
        return "ようかん"

    def get_summary(self):
        return "98円で買える、安くて美味しい和菓子です！あとうまい！"

    def get_author(self):
        return "長田"