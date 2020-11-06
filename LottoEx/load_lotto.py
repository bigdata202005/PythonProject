import json


def read_lotto(file_name):
    with open(file_name, 'r', encoding="utf-8-sig") as json_file:
        json_data = json.load(json_file)
        return json_data


if __name__ == '__main__':
    lotto = read_lotto('lotto.json')
    print(type(lotto))
    print(len(lotto), "개", sep="")
    for key in lotto.keys():
        print(key, '회 : ', lotto[key][:6], sep='')
