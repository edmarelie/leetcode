class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n = 3

        ( -> (( -> ((( -> ((() -> ((()) -> ((()))
                -> (() -> (()( -> (()() -> (()())
                       -> (()) -> (())( -> (())()
          -> () -> ()( -> ()(( -> ()(() -> ()(())
                       -> ()() -> ()()( -> ()()()
        
        1. Only can start with opening until n
        2. Add closing only when num of closing < num of opening
        '''
        pStack = []
        res = []

        def backtrack(openP, closeP):
            # Base
            if openP==n and closeP==n:
                res.append("".join(pStack))
                return
            
            # Decision
            if openP < n:
                pStack.append("(")
                backtrack(openP+1, closeP)
                pStack.pop()
            
            if closeP < openP:
                pStack.append(")")
                backtrack(openP, closeP+1)
                pStack.pop()

        backtrack(0, 0)

        return res
