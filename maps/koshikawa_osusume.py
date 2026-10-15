from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "ソフトクリーム"

    def get_summary(self):
        return "250円で比較的安く、美味しい。"

    def get_author(self):
        return "越川"