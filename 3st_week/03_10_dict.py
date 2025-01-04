class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


dict = Dict()
dict.put("name", "김완수")
dict.put("job", "BE developer")

print(dict.get("name"))
print(dict.get("job"))