class Logger:
    def __init__(self):
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.log and timestamp - self.log[message] < 10:
            return False
        
        self.log[message] = timestamp
        return True

# If there's a new message, log it in a hash table along with a timestamp
# If that same message appears again, compare that timestamp with the stored timestamp in the hash table
# If it's longer than 10 seconds, then update the timestamp and return true
# Otherwise, return false and don't update