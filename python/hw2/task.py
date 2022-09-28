import json


class ColorizeMixin:
    def __str__(self):
        return (f"\033[{0};{self.repr_color_code};{40}m{self.__repr__()}")


class WrapperMap:
    def __init__(self, d: dict):
        self.d = d

    def get_value(self):
        return self.d

    def __getattr__(self, item: str) -> 'WrapperMap':
        return self.__class__(self.d.get(item))

    def __repr__(self):
        return repr(self.d)


class Advert(ColorizeMixin):
    repr_color_code = 32

    def __init__(self, dict):
        self.data = WrapperMap(dict)
        if "price" in self.data.d:
            if self.data.d["price"] < 0:
                raise ValueError("must be >= 0")

    def get_value(self):
        return self.data.d

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    def __getattr__(self, item):
        if item not in self.data.d:
            raise ValueError("This attribute is missing!")
        else:
            return self.data.__getattr__(item)

    @property
    def price(self):
        if "price" in self.data.d:
            return self.data.d["price"]
        else:
            return 0


if __name__ == '__main__':
    try:
        lesson_str = '''{
        "title": "python", "price": -1,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
        }'''
        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)
        print("\nlocation.address:", lesson_ad.location.address)
        print("price:", lesson_ad.price)
    except ValueError as error:
        print(repr(error), "test 1")
    try:
        lesson_str = '{"title": "python"}'
        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)
        print("\nprice:", lesson_ad.price)
    except ValueError as error:
        print(repr(error), "test 2")
    try:
        lesson_str = '''{
        "title": "python", "price": 100,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
        }'''
        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)
        print("\nlocation.address:", lesson_ad.location.address)
        print("price:", lesson_ad.price)
        print("repr:", lesson_ad)
    except ValueError as error:
        print(repr(error), "test 3")
    try:
        lesson_str = '''{
        "title": "python", "price": -5,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
        }'''
        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)
        print("\nlocation.address:", lesson_ad.location.address)
        print("price:", lesson_ad.price)
        print("repr:", lesson_ad)
    except ValueError as error:
        print(repr(error), "test 4")
'''
исправил ошибки falke8 после дедлайна
(так как не знал, что это и проустил в задание,
а так задание выложил на гит еще 21,
обсудил с Александром стоило ли сейчас делать поправки)
'''
