clients = ["John","Marry","Kate"]
clients_High_Priority = ["Tob","Pete"]
clients_Low_Priority = ["Vicky","Lessly"]
clients.insert(0,"Tob")
clients.insert(1,"Pete")
clients.extend(clients_Low_Priority)
print(clients)

        



