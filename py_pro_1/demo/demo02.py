class Message:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "Message:%s" % self.message


print(Message("i have a secret"))
