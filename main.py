from diaries.DiarySample import DiarySample
from diaries.YamamotoDiary import YamamotoDiary
from diaries.ToriiDiary import ToriiDiary
from diaries.ItoDiary import ItoDiary
from diaries.kageyamaDiary import kageyamaDiary
from diaries.UsidaDiary import UsidaDiary
from diaries.kobayashiDiary import kobayashiDiary
from diaries.inoriDiary import inoriDiary
# ↓のリストには、メンバーの各日記が格納されます。 diaries = [DiarySample(), ]
diaries = [DiarySample(), 
           YamamotoDiary(),
           ToriiDiary(),
           ItoDiary(),
           kageyamaDiary(),
           UsidaDiary(),
           kobayashiDiary(),
           inoriDiary()
           ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()