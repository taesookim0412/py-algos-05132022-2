class Solution:

    def evaluate_expr(self, stck):
        if not stck or type(stck[-1]) == str:
            stck.append(0)
        res = stck.pop()
        while stck and stck[-1] != ')':
            sign = stck.pop()
            if sign == '+':
                res += stck.pop()
            else:
                res -= stck.pop()
        return res

    # 321
    # 3 * 10 + 2 = 32
    # 32 * 10 + 1 = 321
    # num = 3
    # n = 1 => num = 10 * num + ch => 30 + 2 = 32
    # n = 2 => num = 10 * num + ch => num = 10 * 32 + ch = 321

    # 321
    # 1
    # 20 + 1 = 21
    # num = 10 ** nthPlace * int(char) + num
    # ch = 1 => 1 * 1 + 0 = 1
    # ch = 2 => 10 * 2 + 1 = 21
    # backwards pass number
    def calculate(self, s: str) -> int:
        exprs = []
        nthPlace = 0
        num = 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char.isnumeric():
                num = 10 ** nthPlace * int(char) + num
                nthPlace += 1
            elif char != ' ':
                if nthPlace:
                    exprs.append(num)
                    nthPlace = 0
                    num = 0
                if char == '(':
                    res = self.evaluate_expr(exprs)
                    exprs.pop()
                    exprs.append(res)
                else:
                    exprs.append(char)
        if nthPlace:
            exprs.append(num)

        return self.evaluate_expr(exprs)

