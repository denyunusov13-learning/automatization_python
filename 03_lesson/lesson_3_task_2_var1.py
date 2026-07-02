from smartphone import Smartphone


catalog = [
    Smartphone("techno", "pova4", "+79998887766"),
    Smartphone("xiaomi", "redmi10", "+79115554433"),
    Smartphone("honor", "400", "+79239239923"),
    Smartphone("iphone", "15", "+79133191919"),
    Smartphone("oppo", "nova10", "+79513515151")
]

for smart in catalog:
    print(f"{smart.brand} - {smart.model}. {smart.tel_num}")
