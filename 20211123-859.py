class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        pos1 = -1
        cnt = 0
        res = False
        same_letters = {}
        for i in range(len(s)):
            if s[i] != goal[i]:
                cnt += 1
                if cnt > 2:
                    return False
                if pos1 == -1:
                    pos1 = i
                else:
                    if s[pos1] == goal[i] and goal[pos1] == s[i]:
                        res = True
                    else:
                        return False
            if s[i] == goal[i]:
                if s[i] not in same_letters:
                    same_letters[s[i]] = 0
                same_letters[s[i]] += 1
        if cnt == 2 and res:
            return True
        if cnt == 0:
            for k in same_letters:
                if same_letters[k] > 1:
                    return True
        return False


