class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        cur = ["", "", "", ""]

        def validIP():
            for part in cur:
                # no values
                if part == "":
                    return False
                # leading 0
                if len(part) > 1 and part[0] == "0":
                    return False
                # number out of range
                if not (0 <= int(part) <= 255):
                    return False
            return True

        def dfs(i, j):
            print(cur)
            length = len(s)
            # pointer is at the end and the current ip is valid
            if i >= length and validIP():
                value = ".".join(cur)
                res.append(value)
                return
            # Adding beyond 3 dots (4 blocks of numbers)
            if j >= 4:
                return
            # Partitioning between 1 and 3 numbers
            for k in range(1, 4):
                # ensure that the partition is within the bounds of the string
                if i + k <= length and 0 <= int(s[i: i + k]) <= 255:
                    cur[j] += s[i: i + k]
                    dfs(i + k, j + 1)
                    cur[j] = cur[j][:-k]

        dfs(0,0)
        return res