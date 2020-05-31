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
        check1 = family_name is None        # 如果没有指定姓氏，就不需要check1
        check2 = False
        for item in row:
            if name in item:
                check2 = True
                break
        if family_name is not None and check2:
            for item in row:
                if family_name in item:
                    check1 = True
                    break
        return check1 and check2

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
    print(name_gen.generate("六一"))





