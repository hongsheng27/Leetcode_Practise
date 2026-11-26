class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []
        for log in logs:
            ident, content = log.split(" ", 1)
            if content[0].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda log: (log.split()[1:], log.split()[0]))
        return letters + digits