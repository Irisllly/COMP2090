import json
Data_board="board.json"  
#import os
#scriptDir=os.path.dirname(os.path.abspath(__file__))
#Data_board=os.path.join(scriptDir,"board.json")

#Types of plates sold in registered store
class Board:
    def __init__(self,brand,color,factory):
        self.brand=brand
        self.color=color
        self.factory=factory
class BoardLibrary:
    def __init__(self):
        self.board_list=[]  #Storage of plate data

        self.load_boardList()  #Read data

    #save all data of board in board.json
    def save(self):
        data=[{"brand":b.brand,"color":b.color,"factory":b.factory} for b in self.board_list]
        try:
            with open(Data_board,"w",encoding="utf-8")as f:
                json.dump(data,f,ensure_ascii=False,indent=2)
            if not data:
                print("List is empty, board.json has been deleted.")
            else:
                print(f"Successfully saved{len(self.board_list)}board(s)")
        except Exception as e:
            print(f"Failed to load data:{e}")

    #add board
    def add_board(self,brand, color,factory):
        for i in self.board_list:
            if i.brand==brand and i.color==color:
                return False
        #place new_board into board_list
        new_board=Board(brand,color,factory)
        self.board_list.append(new_board)
        #save data at once
        self.save()
        return True
        
    #Delete board
    def delete_board(self,index):
        if index>=0 and index<len(self.board_list):
            del self.board_list[index]
            self.save()
            return True
        return False

    
    
       
    #read boardList when start
    def load_boardList(self):
        self.board_list=[]
        try:
            with open(Data_board,"r",encoding="utf-8")as f:
                data=json.load(f)
                self.board_list=[]
                for i in data:
                    boa=Board(i["brand"], i["color"], i["factory"])
                    self.board_list.append(boa)
        except:
            self.board_list=[]  #no file->clear list
    
    #Return to board_list
    def get_allBoard(self):
        return self.board_list
    