from diaries.DiarySample import DiarySample
from diaries.UsidaDiary import UsidaDiary
# ↓のリストには、メンバーの各日記が格納されます。 diaries = [DiarySample(), ]
diaries = [DiarySample(), UsidaDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()