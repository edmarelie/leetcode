class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Initialize mapping for phone number
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # List of Result
        res = []
        i = 0

        # Backtrack function
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # 1. i=0, curStr="", mapping[digits[0]]="abc"
            #    a. i=1, curStr="a", mapping[digits[1]]="def"
            #       -) i=2, curStr="ad", res=["ad"]
            #       -) i=2, curStr="ae", res=["ad", "ae"]
            #    ...
            for c in mapping[digits[i]]:
                backtrack(i+1, curStr+c)

        # Start backtrack
        # Example: digits = "23"
        if digits:
            backtrack(0, "")

        return res
