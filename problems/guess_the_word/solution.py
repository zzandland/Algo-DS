# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        match = lambda a, b: len([1 for ca, cb in zip(a, b) if ca == cb])
        while True:
            ws = {*wordlist}
            t = random.choice(wordlist)
            guess = master.guess(t)
            print(guess, len(wordlist))
            if guess == 6: break
            for w in wordlist:
                m = match(t, w)
                if guess == -1 and m != 0: ws.remove(w)
                elif m != guess: ws.remove(w)
            wordlist = list(ws)