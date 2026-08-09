products = {
            "backpack": "add-to-cart-sauce-labs-backpack",
            "bike light": "add-to-cart-sauce-labs-bike-light",
            "bolt t shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "fleece jacket": "add-to-cart-sauce-labs-fleece-jacket",
            "labs onesie": "add-to-cart-sauce-labs-onesie",
            "shirt red": "add-to-cart-test.allthethings()-t-shirt-(red)",
            }


def add_thing(part_name: str) -> None:
    """нажимает кнопку добавления товара по названию или
    части названия, переданной в качестве аргумента"""
    part_name_lower = part_name.lower()
    for full_name, locator in products.items():
        if part_name_lower in full_name:
            print(locator)
            return
    raise ValueError(f"Товар с подстрокой '{part_name}' не найден")


add_thing("back")

