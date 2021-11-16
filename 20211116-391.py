class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        point_dict = {}
        area_sum = 0
        max_point = rectangles[0]
        for x, y, a, b in rectangles:
            for p in [(x, y), (x, b), (a, y), (a, b)]:
                if p not in point_dict:
                    point_dict[p] = 0
                point_dict[p] += 1
            area_sum += (a-x)*(b-y)
            max_point = [min(max_point[0], x), min(max_point[1], y), max(max_point[2], a), max(max_point[3], b)]
        cnt = 0
        print(point_dict)
        for p in point_dict:
            if point_dict[p] == 1:
                cnt += 1
            elif point_dict[p] != 2 and point_dict[p] != 4:
                return False
        real_area = (max_point[2] - max_point[0]) * (max_point[3] - max_point[1])
        for p in [(max_point[0], max_point[1]), (max_point[0], max_point[3]), (max_point[2], max_point[3]), (max_point[2], max_point[1])]:
            if p not in point_dict or point_dict[p] != 1:
                return False
        return cnt == 4 and real_area == area_sum


t = Solution().isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
print(t)