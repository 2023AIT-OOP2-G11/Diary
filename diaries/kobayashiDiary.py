from diaries.AbstractDiary import AbstractDiary

class kobayashiDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return "今日も元気だった"

    def get_author(self):
        return "Kobayashi"