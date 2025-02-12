from tools.send import Send


class PermissionRequest():
    def subscribe_request(stock, ai_model):
        sr1 = Send.send_request("subscribe", stock)  
        print(ai_model + " has requested to subscribe to " + stock)