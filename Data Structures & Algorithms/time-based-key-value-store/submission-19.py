class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.setdefault(key, []).append([value, timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        searchmap = self.timemap.get(key)
        res = ""
        if not searchmap:
            return res

        l, r = 0, len(searchmap) - 1
        while l <= r:
            mid = (l + r) // 2
            if searchmap[mid][1] <= timestamp:
                res = searchmap[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res