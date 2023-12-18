from diaries.AbstractDiary import AbstractDiary 

class UsidaDiary(AbstractDiary):

    def get_date(self):
        return "2023-12-14"

    def get_summary(self):
        return "今日は木曜日だった。"

    def get_author(self):
        return "Usida"