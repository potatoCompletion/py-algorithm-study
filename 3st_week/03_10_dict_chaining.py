# 해쉬 충돌을 chaining 방식으로 해결한 구현 코드

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
        return None

class LinkedDict:
    def __init__(self):
        default_size = 8
        self.items = []
        for i in range(default_size):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


dict = LinkedDict()
dict.put("name", "김완수")
dict.put("job", "BE developer")

dict.put("1", "a")
dict.put("2", "b")
dict.put("3", "c")
dict.put("4", "d")
dict.put("5", "e")
dict.put("6", "f")
dict.put("7", "g")
dict.put("8", "h")
dict.put("9", "i")
dict.put("10", "k")
dict.put("11", "l")
dict.put("12", "m")
dict.put("13", "n")

print(dict.get("name"))
print(dict.get("job"))

for i in range(1, 14):
    print(dict.get(str(i)))