class Solution:
    def alertNames(self, keyName, keyTime):
        name_dict = {}
        for name, time_str in zip(keyName, keyTime):
            time = int(time_str[:2]) * 60 + int(time_str[3:])
            if name not in name_dict:
                name_dict[name] = [time]
            else:
                name_dict[name].append(time)
        result = []
        for name in name_dict:
            sorted_time = sorted(name_dict[name])
            if len(sorted_time) < 3:
                continue
            for i in range(len(sorted_time) - 2):
                if sorted_time[i] - sorted_time[i + 2] >= -60:
                    result.append(name)
                    break
        return sorted(result)


result = Solution().alertNames(["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                               ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"])
print(result)
