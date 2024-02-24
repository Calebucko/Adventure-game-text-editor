# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:26:15 2024

@author: Caleben Jahn
"""
import json
def main():
    game=getBasegame()
    userChoice=input("What would you like to do?")
    keepgoing=True
    while(keepgoing):
        if userChoice=="0":
           print("Exiting editor")
           keepgoing = False
        elif userChoice =="1":
           print("What would you like to do?")
           game=getBasegame()
        elif userChoice =="2":
           print("Please enter file name")
           game=loadGame()
        elif userChoice == "3":
           print("Game saved, you are safe to exit")
           game= saveGame()
        elif userChoice == "4":
           print("Which node would you like to edit?")
           game=editNode()
        elif userChoice == "5":
           print("Game loaded")
           playGame(game)
           
        else:
           print("Please type a correct number man")
def getMenuchoice():
    print(
        "0) Exit editor"
        "1) Load default game"
        "2) Load a file"
        "3) Save current game"
        "4) Edit nodes and games"
        "5) Play current loaded game")
    userChoice= input("What would you like to do?")
    
    return userChoice

def getBasegame():
    basegame={"base": ["start over", "start", "quit", "quit"]}
    return basegame
    
def playGame(game):
    currentnode=playnode(game, "start")
    keepgoing= True 
    while(keepgoing):
        if currentnode== "quit":
            keepgoing = False
        else:
            currentnode=playnode(game, currentnode)
def playnode(game, currentnode):
    {"name:" ["description", "menuA", "nodeA", "menuB", "nodeB"]}
    choice= input(f"""what will you do?
            1) {game[currentnode][1]})
            2) {game[currentnode][3]}""")
    if choice == "1":
        currentnode=game[currentnode][2]
        print(f'{game[currentnode][0]}')
    elif choice == "2":
        currentnode=game[currentnode][4]
        print(f'{game[currentnode][0]}')
    else:
        print("type a number that's 1 or 2 dawg")
    return currentnode

def editNode(game):
    print("game status at the moment")
    print(json.dumps(game, indent=1))
    for nodeName in game.keys():
        print(f"{nodeName}")
    newNodename=input("list the node name you want to make or edit.")
    if newNodename in game.keys():
       newNode = game[nodeName]
    else:
        newNode= ["", "", "", "", ""]
        
    (description, menuA, nodeA, menuB, nodeB)=newNode
    newDesc=editField("description", description)
    newMenuA=editField("menu A", menuA)
    newNodeA=editField("node A", nodeA)
    newMenuB=editField("menu B", menuB)
    newNodeB=editField("node B", nodeB)
    
    game[newNode] = [newDesc, newMenuA, newNodeA, newMenuB, newNodeB]
    
    return game
        
    
        
def editField(newNode, gameDB):
    currentfield= input("hange your node, menu, or description here")
    if currentfield == "":
        currentfield= currentfield
    else:
        currentfield=newNode
    
        
def saveGame(game):
    fileout = open("game.json", "w")
    game=json.dump(game, fileout, indent=1)
    fileout.close()
    print("Game saved, you're safe")
    
def loadGame():
    filein = open("game.json", "r")
    game= json.load(filein)
    filein.close()
    return game
    print("Game loaded, would you like to play?")
    
    
    
    
    

        
    
    
        
           
main()
          