# 1. Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},
    ]
]


# потрібно брати по черзі с кожного списку id і класти в список res,
# якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
# в результат має записатись тільки 5 id
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]

class Gen:

    @staticmethod
    def get_item(item_list):
        for item in item_list:
            yield item["id"]


arr_data = [Gen.get_item(item) for item in data]

res = []

while len(res) < 5:
    current_item = arr_data.pop(0)
    try:
        next_item = next(current_item)
        if next_item not in res:
            res.append(next_item)
            arr_data.append(current_item)
        else:
            arr_data.insert(0, current_item)
    except StopIteration:
        pass
print(res)
