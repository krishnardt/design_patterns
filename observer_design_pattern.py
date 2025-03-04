from abc import ABC, abstractmethod

class StockObservable(ABC):

    # def __init__(self):
    #     self.displays = []

    def add(self):
        pass
    def remove(self):
        pass
    def notify(self):
        pass
    def get_data(self):
        pass
    def set_data(self):
        pass


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


class EmailObserver(Observer):
    def __init__(self, name, obs: StockObservable):
        self.name = name
        self.obs = obs
    

    def update(self):
        return self.send_email(self.name, "product is live now")
    

    def send_email(self, name, message):
        print(f"message sent to {name}:  {message}")



class IphoneObserver(Observer):

    def __init__(self, name, obs: StockObservable):
        self.name = name
        self.obs = obs
    

    def update(self):
        return self.send_iphone(self.name, "product is live now...")
    

    def send_iphone(self, name, message):
        print(f"message sent to {name}:  {message}")



class IphoneStock(StockObservable):

    def __init__(self):
        self.observers = []
        self.count= 0
    

    def add(self, obs: Observer):
        self.observers.append(obs)
    

    def remove(self,obs: Observer):
        self.observers.remove(obs)
    
    def notify(self):
        print(len(self.observers))
        for each in self.observers:
            each.update()
    

    def set_data(self, count):
        print("count:  ", self.count)
        if self.count == 0:
            self.notify()
        
        self.count += count
    

    def get_data(self):
        return self.count




# class WSImpl(WSObservable):
#     def __init__(self):
#         self.displays = []
    

#     # def add()

#     def notify(self):
#         for each in self.displays:
#             each.update()



# class DisplayObserver(ABC):

#     def update(self):
#         pass




# class MobileDisplay(DisplayObserver):

#     def __init__(self, wso: WSObservable):
#         self.wso = wso
    

#     def update(self):
#         self.wso.notify()



# class TVDisplay(DisplayObserver):
#     def __init__(self, wso: WSObservable):
#         self.wso = wso
    
#     def update(self):
#         self.wso.get_data()





if __name__ == "__main__":

    iphone_stock = IphoneStock()


    obs1 = EmailObserver(name="krishn@gmail.com", obs=iphone_stock)
    obs2 = EmailObserver(name="krishn1@gmail.com", obs=iphone_stock)
    obs3 = EmailObserver(name="krishn2@gmail.com", obs=iphone_stock)
    obs4 = IphoneObserver(name="krishn3", obs=iphone_stock)


    iphone_stock.add(obs1)
    iphone_stock.add(obs2)
    iphone_stock.add(obs3)
    iphone_stock.add(obs4)
    print(obs1.update())
    print(obs2.update())
    print(obs3.update())
    print(obs4.update())

    iphone_stock.set_data(10)

    print(iphone_stock.get_data())
