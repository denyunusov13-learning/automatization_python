# данный вариант решения написал сам, перемудрил, потому что не прорешал
# практику переод выполнением упражнений, хотел без подсказок
from smartphone import Smartphone

catalog = []

smart1 = Smartphone("techno", "pova4", "+79998887766")
character1 = []
character1.append(smart1.brand)
character1.append(smart1.model)
character1.append(smart1.tel_num)
catalog.append(character1)

smart2 = Smartphone("xiaomi", "redmi10", "+79115554433")
character2 = []
character2.append(smart2.brand)
character2.append(smart2.model)
character2.append(smart2.tel_num)
catalog.append(character2)

smart3 = Smartphone("honor", "400", "+79239239923")
character3 = []
character3.append(smart3.brand)
character3.append(smart3.model)
character3.append(smart3.tel_num)
catalog.append(character3)

smart4 = Smartphone("iphone", "15", "+79133191919")
character4 = []
character4.append(smart4.brand)
character4.append(smart4.model)
character4.append(smart4.tel_num)
catalog.append(character4)

smart5 = Smartphone("oppo", "nova10", "+79513515151")
character5 = []
character5.append(smart5.brand)
character5.append(smart5.model)
character5.append(smart5.tel_num)
catalog.append(character5)


for brand, model, tel_num in catalog:
    print(f"{brand} - {model}. {tel_num}")
