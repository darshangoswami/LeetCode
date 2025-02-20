class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            for k in reversed(self.store[key].keys()):
                if k <= timestamp:
                    return self.store[key][k]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)