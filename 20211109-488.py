# ac
# by pruning
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def eliminate(s):
            if len(s) == 0:
                return ''
            last = s[0]
            cnt = 0
            res = ''
            for i in range(len(s)):
                if s[i] == last:
                    cnt += 1
                else:
                    if cnt < 3:
                        res += s[i - cnt:i]
                    cnt = 1
                    last = s[i]
            if 0 < cnt < 3:
                res += s[len(s) - cnt:]
            if res == s:
                return res
            else:
                return eliminate(res)
        if len(board + hand) < 3:
            return -1
        letter_rec = {}
        for x in board:
            if x not in letter_rec:
                letter_rec[x] = 0
            letter_rec[x] += 1
        for x in hand:
            if x in letter_rec:
                letter_rec[x] += 1
        for k in letter_rec:
            if letter_rec[k] < 3:
                
                return -1
        board = eliminate(board)
        if board == '' or eliminate(board) == '':
            
            return 0
        if len(hand) == 0 and board == eliminate(board):
            # print(board, hand)
            return -1
        # print(board, hand)
        results = []
        for i in range(len(board)+1):
            rec = {}
            for j in range(len(hand)):
                if i == 0 and hand[j] != board[i]:
                    continue
                if i == len(board) and hand[j] != board[i-1]:
                    continue
                if hand[j] != board[i-1] and hand[j] != board[i] and board[i-1] !=board[i]:
                    continue
                if hand[j] not in rec:
                    rec[hand[j]] = 0
                rec[hand[j]] += 1
                if rec[hand[j]] > 1:
                    continue
                new_board = board[:i] + hand[j]
                if i < len(board):
                    new_board += board[i:]
                new_hand = hand[:j]
                if j < len(hand)-1:
                    new_hand += hand[j+1:]
                used_ball = self.findMinStep(new_board, new_hand)
                if used_ball >= 0:
                    results.append(used_ball)
        if len(results) == 0:
            
            return -1
        else:

            return min(results) + 1


print(Solution().findMinStep("RRWWRRBBRR", "WB"))
