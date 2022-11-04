import requests 
import datetime 
import time
# https://xzc.2miners.com/api/accounts/a3uR4t957vhSXPSbutU4CTkrVen1jeQdet my miner
# test a3jihwZ8USdsKScYe4feeoJWmcb5rKfdao
class MinerSystem_stat:
    
    def __init__(self, reciever_id):
        self.BASE_URL = "https://xzc.2miners.com/api/accounts/"
        self.ID = reciever_id
        self.URL_REQUEST = f"{self.BASE_URL}{self.ID}"
        self.worker_status = "---" 
        self.hashrate = "---"
        
    def request_miner_stat(self):
        # request data
        response = requests.get(self.URL_REQUEST)

        # update to display system
        data = response.json()

        self.check_worker_status(worker_num = data["workersOnline"])
        self.hash_rate_calc(data["currentHashrate"])
        

    def check_worker_status(self, worker_num):
        if worker_num > 0:
            self.worker_status = "online" 
        else:
            self.worker_status = "offline" 

    def hash_rate_calc(self, hash_rate):
        mega_hash = hash_rate*10**-6
        self.hashrate = mega_hash
        

    def run(self):
        while True:
            self.request_miner_stat()
            print(f"Worker Status : {self.worker_status} and Hash rate : {self.hashrate}MH/s")
            time.sleep(5)

if __name__ == "__main__":
    x = MinerSystem_stat(reciever_id="a3uR4t957vhSXPSbutU4CTkrVen1jeQdet")
    x.run()
