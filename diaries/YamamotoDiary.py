from diaries.AbstractDiary import AbstractDiary 
class YamamotoDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    def get_summary(self):
        return "リーダーになってしまった。"
    def get_author(self):
        return "Yamamoto"