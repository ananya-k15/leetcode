class TimeMap:

    def __init__(self):
        self.timestamps = dict()
        self.values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timestamps:
            self.timestamps[key].append(timestamp)
        else:
            self.timestamps[key] = [timestamp]
            self.values[key] = dict()
        self.values[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        # print('For', timestamp)
        arr = self.timestamps[key]
        if arr and arr[-1] < timestamp:
            return self.values[key][arr[-1]]
        l, r = 0, len(arr)-1
        ans = -1
        while l <= r:
            mid = (l+r)//2
            # print(arr[l:r+1])
            # print(arr[l], timestamp, mid)
            if arr[mid] == timestamp:
                return self.values[key][timestamp]
            elif arr[mid] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return "" if r < 0 else self.values[key][arr[r]]
        #     if arr[mid] == timestamp:
        #         return self.values[key][timestamp]
        #     elif arr[mid] > timestamp:
        #         r = mid - 1
        #     else:
        #         ans = mid
        #         l = mid + 1
        # return self.values[key][arr[l]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# ["TimeMap","set","set","set","set","set","get","get","get","get","get","get","get"]
# [[],["foo","bar",1],["foo","bar2",2],["foo","bar3",4],["foo","bar4",7],["foo","bar5",9],["foo",1],["foo",2],["foo",3],["foo",4],["foo",5],["foo",8],["foo",11]]