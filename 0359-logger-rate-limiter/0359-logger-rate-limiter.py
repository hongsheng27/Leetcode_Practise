class Logger:
    def __init__(self):
        self.count = {}
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.count:
            status = timestamp - self.count[message] >= 10
            if status: self.count[message] = timestamp
            return status
        else:
            self.count[message] = timestamp
        return True

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)