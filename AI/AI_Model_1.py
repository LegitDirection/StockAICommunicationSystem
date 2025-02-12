import os
import sys
import pika

from tools import receive
from tools.PermissionRequest import PermissionRequest

class AI_Model_1:
    def subscribe_and_receive():
        #subscribe_to_stock("AAPL")
        while x == 0:
            if AI_Model_1.get_stock_data("AAPL") == 1:
                print("Stock data received")
                x = 1
            else:
                print("Stock data not received")


    def subscribe_to_stock(stock):
        rs1 = PermissionRequest()
        rs1.subscribe_request(stock, "AI_Model_1")
        while x == 0:
            if receive.receive_text("master") == "subscription_approved":
                print("Subscription request approved")
                x = 1
            else:
                print("Subscription approval not received")


    def get_stock_data(stock):
        rs2 = receive()
        stock_data = rs2.receive_stock_data(stock)
        print(stock_data)
        return 1