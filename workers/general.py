import os
import socket
import requests

from workers.baseWorker import BaseWorker


class Worker(BaseWorker):
    def __init__(self, data: dict):
        self.name = "general"

    def getInfo(self, data: dict) -> dict:
        res = {}

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        res["private_ip"] = s.getsockname()[0]
        s.close()
        
        res["modules"] = []
        wl = ["general", "baseWorker", "__init__"]
        for root, _, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
            for file in files:
                flag = True
                for w in wl:
                    if w in file:
                        flag = False
                        break
                if flag:
                    res["modules"].append(file.split(".")[0])
                
        
        return res

    def run(self, data: dict) -> dict:
        if data["function"] == "getInfo":
            return {"res": self.getInfo(data["data"])}

if __name__ == "__main__":
    work = Worker()
    print(work.getInfo())
