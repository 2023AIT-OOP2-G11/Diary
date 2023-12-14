from diaries.DiarySample import DiarySample
from diaries.YamamotoDiary import YamamotoDiary
from diaries.ToriiDiary import ToriiDiary
from diaries.ItoDiary import ItoDiary
from diaries.kageyamaDiary import kageyamaDiary
from diaries.UsidaDiary import UsidaDiary
from diaries.KobayashiDiary import KobayashiDiary

# ↓のリストには、メンバーの各日記が格納されます。 diaries = [DiarySample(), ]
diaries = [
    DiarySample(),
    YamamotoDiary(),
    ToriiDiary(),
    ItoDiary(),
    kageyamaDiary(),
    UsidaDiary(),
    KobayashiDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
