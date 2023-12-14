from diaries.DiarySample import DiarySample
from diaries.YamamotoDiary import YamamotoDiary
from diaries.ToriiDiary import ToriiDiary
from diaries.ItoDiary import ItoDiary
# ↓のリストには、メンバーの各日記が格納されます。 diaries = [DiarySample(), ]
diaries = [DiarySample(), 
　　　　　　　　　　　　　　　　　　  YamamotoDiary(),
           ToriiDiary(),
    　　　　　　　　　　　　　　ItoDiary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()