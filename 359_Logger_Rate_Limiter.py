class Logger:

    def __init__(self):
        self.lastPrinted = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if not(message in self.lastPrinted):
            self.lastPrinted[message] = timestamp
            return True
        
        lastPrintedTime = self.lastPrinted[message]


        shouldPrint = (timestamp - lastPrintedTime) >= 10
        if shouldPrint:
            self.lastPrinted[message] = timestamp
            return True
        else:
            return False
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)