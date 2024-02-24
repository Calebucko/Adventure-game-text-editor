# Adventure-game-text-editor

    main() 
        Runs the main loop
        Calls and prints a menu
        creates a loop where if the menu option is exit it closes the program and the loop closes
        keeps going it there are valid menu choices sent to it 
        Sends control to other parts of the program
    getMenuChoice()
        prints a menu of user option
        gets input from user 
        repeats if input is invalid
        returns a valid menu choice
    playGame()
        plays the game
        Keeps going until next node is "quit"
    playNode()
        given the game data and a node,
        plays out the node
        monitors if correct data has been inputed
        returns the next node
    getDefaultGame()
        creates a single-node default game
        returns that data structure
    editNode()
        given the current game structure...
        list all the current node names
        print dictionary from json files
        check through dictionary keys
        get a node name
        if that node exists
            copy that node to newNode
        otherwise...
            create newNode with empty data
        show list of varibles that will change with edit field function
        use editField() to allow user to edit each node
        return the now edited newNode
    editField()
        get a field name
        print the field's current value
        if the user presses 'enter' immediately
            retain the current value
        otherwise...
            use the new value
    saveGame()
        save the game to a data file
        you can preset the file name (eg 'game.dat')
        print the current game dictionary in human-readable format
        Save the file in JSON format
    loadGame()
        presume there is a data file named 'game.dat' in the current directory
        open that file
        load the data into the game object
        return that game object
