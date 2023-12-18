from diaries.AbstractDiary import AbstractDiary

class ToriiDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-18"
    def get_summary(self):
        return """github使いにくいです。間違っていないかどうか不安です。"""
    def get_author(self):
        return "Torii"