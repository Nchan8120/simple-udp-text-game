A simple text based adventure game
a player can enter the game, exit the game, look around, take items, drop items, and check their inventory
A game server represents a single room or area in the game.  It has a name, a description, a list of items currently in it, and a list of players currently in it
You start the game by launching your game server.  It needs to be first so that your game client can message it to play the game.  
Players play using the game client.  It gives them a text-based interface to send commands to the game server and display responses that come back.
When the player is done playing, they press Ctrl-C or use the exit command to tell the server they are done, and the server no longer considers them as part of the game.  
The game server should run persistently; however, it should also terminate when given a Ctrl-C signal. 
When a room server starts, it registers its name and address with the discovery service.  Later, when player clients or other room servers need to connect with it, they can lookup the address for the server by querying the discovery service. 
This way, the various parts of the game need only identify themselves by name, and the discovery service handles the yucky part of keeping track of all of the corresponding addresses.  
