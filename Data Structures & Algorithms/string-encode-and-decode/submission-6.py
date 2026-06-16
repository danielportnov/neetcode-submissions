class Solution:
    indexed = {}

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs)):
            self.indexed[i] = strs[i]
            res += str(i)
            res += " "

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        indicies = s.split(" ")[:-1]

        print(self.indexed[0])

        for index in indicies:
            res.append(self.indexed[int(index)])

        print(res)
        return res