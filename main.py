from maps.koshikawa_osusume import koshikawa_osusume
from maps.matsumoto_osusume import matsumoto_osusume
from maps.miyamoto_osusume import miyamoto_osusume
from maps.nagata_osusume import nagata_osusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [koshikawa_osusume(), matsumoto_osusume(),miyamoto_osusume(),nagata_osusume()] 

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()