import csv


class NameGenerator:
    def __init__(self):
        self.data = []
        name_collection = csv.reader(open(r"Collection.csv", 'r', encoding='UTF8'))
        for row in name_collection:
            temp = list(map(lambda x: x.lstrip(), row))
            temp = [x for x in temp if x != '']
            self.data.append(temp)

    def check(self, row: list, name, family_name=None):
        check1 = family_name is not None        # 姓氏验证
        check2 = False                          # 字号验证
        if (check1 is True) and (self.check_family_name(row, family_name) is False):    # 该行中不含所要姓氏
            return False
        else:
            for item in row:
                if name in item:
                    check2 = True
                    break
        return check2

    def check_family_name(self, row: list, family_name:str):
        for item in row:
            if family_name in item:
                return True
        else:
            return False

    def generate(self, name, family_name=None):
        print(name)
        if family_name is not None:
            name = name.strip(family_name)
        for row in self.data:
            if self.check(row, name, family_name):
                return row
        else:
            return None


if __name__ == '__main__':
    name_gen = NameGenerator()
    print(name_gen.generate("苏轼"))
    print(name_gen.generate("东坡", family_name="苏"))
    print(name_gen.generate("苏东坡", family_name="苏"))
    print(name_gen.generate("六一居士"))
    print(name_gen.generate("放翁"))





