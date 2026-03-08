import json
import time
class Order:
    def __init__(self,community,roomNum,boardList,status="pending"):
        self.community=community
        self.roomNum=roomNum
        self.boardList=boardList
        self.status=status
        self.createTime=time.strftime("%Y-%m-%d %H:%M:%S")
    def toDict(self):
        return{"community":self.community,"room number":self.roomNum,"board list":self.boardList,"status":self.status,"create time":self.createTime}
class OrderManagement:
    def __init__(self):
        self.fileName="orders.json"
        self.orderList=self.loadOrders()
    def loadOrders(self):
        try:
            with open(self.fileName,"r",encoding="utf-8")as f:
                data=json.load(f)
                orders=[]
                for i in data:
                    order=Order(community=i["community"],roomNum=i["room number"],boardList=i["board list"],status=i["status"])
                    order.createTime=i["create time"]
                    orders.append(order)
            return self.sortOrders(orders)
        except:
            return[]
    #save orders in order
    def sortOrders(self,orders):
        return sorted(orders,key=lambda x:(0 if x.status=="pending" else 1,x.createTime),reverse=True)
    
    #add orders
    def addOrders(self,community,roomNum,boardList,status="pending"):
        newOrder=Order(community,roomNum,boardList,status)
        self.orderList.append(newOrder)
        #rearrange orders
        self.orderList=self.sortOrders(self.orderList)
        self.saveOrders()
        return newOrder
    
    #delete orders
    def deleteOrders(self,index):
        if index>=0 and index<len(self.orderList):
            del self.orderList[index]
            self.saveOrders()
            self.orderList=self.sortOrders(self.orderList)
            return True
        return False

    
    #save orders in orders.json
    def saveOrders(self):
        data=[i.toDict() for i in self.orderList]
        with open (self.fileName,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
    
    #change status
    
    def changestatus(self,OrderInd):
        if 0<=OrderInd<len(self.orderList):
            order=self.orderList[OrderInd]
            if order.status=="pending":
                order.status="completed"
            else:
                order.status="pending"
            self.saveOrders()
            self.orderList=self.sortOrders(self.orderList)
            return order.status
        return None

if __name__=="__main__":
    ormgm=OrderManagement()
    testBoardList=[{"brand":"CLEAF","color":"LR27","qty":5},{"brand":"EGGER","color":"H3043 ST12","qty":3}]
    ormgm.addOrders(community="Harbour Place",roomNum="4tower25C",boardList=testBoardList,status="pending")
    print("Order saved successfully! Check your folder for orders.json")