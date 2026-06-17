from address import Address
from mailing import Mailing


address_to = Address("633456", "Тогучин", "Заводская", "1", "1")
address_from = Address("633333", "Новосибирск",
                       "Проспект ленина", "225", "405")

message = Mailing(address_to, address_from, 500, "152334")
print(f"Отправление {message.track} из {address_from.index}, "
      f"{address_from.city}, {address_from.street}, {address_from.house} - "
      f"{address_from.apartment} в {address_to.index}, {address_to.city}, {address_to.street},"
      f" {address_to.house} - {address_to.apartment}. Стоимость {message.cost} рублей."
)
