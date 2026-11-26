class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []
        for log in logs:
            ident, content = log.split(" ", 1)
            if content[0].isdigit():
                digits.append(log)
            else:
                letters.append((content, ident, log))
        
        letters.sort()
        return [log for _,_,log in letters] + digits