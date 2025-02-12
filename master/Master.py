from tools import receive
from tools.send import Send
class master:
    def get_permission_request(subscriber):
        request1 = receive.receive_request()
        if request1 == "subscribe":
            s1 = Send()
            s1.send_new_subscriber(subscriber)

        