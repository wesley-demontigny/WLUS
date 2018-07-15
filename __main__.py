import game
import services
import session_service
import os
import asyncio
import configparser
import player_service
import threading
import sys
import replica_service
from importlib import reload


def console_loop():
	while True:
		input_str = input()
		args = input_str.split(" ")
		if(args[0] == "exit"):
			sys.exit(0)
		if(args[0] == "py"):
			try:
				del args[0]
				exec(''.join(str(e) for e in args))
			except Exception as e:
				print("Console Error :", e)

if __name__ == "__main__":
	game = game.Game()

	config = configparser.ConfigParser()
	config.read("config.ini")
	game_config = config["GAME_CONFIG"]
	game.set_config("address", str(game_config["address"]))
	game.set_config("auth_port", int(game_config["auth_port"]))
	game.set_config("world_port", int(game_config["world_port"]))
	game.set_config("auth_max_connections", int(game_config["auth_max_connections"]))
	game.set_config("world_max_connections", int(game_config["world_max_connections"]))
	game.set_config("accept_custom_names", bool(game_config["accept_custom_names"]))

	#Append all game scripts to Game
	for file in os.listdir("./game_scripts"):
		if file.endswith(".py"):
			mod = __import__(f'game_scripts.{file[:-3]}', fromlist=["Main"])
			game.add_script(getattr(mod, 'Main')(game))

	database = services.DatabaseService(game)
	game.register_service(database)

	player = player_service.PlayerService(game)
	game.register_service(player)

	session = session_service.SessionService(game)
	game.register_service(session)

	auth_server = services.AuthServerService(game)
	game.register_service(auth_server)

	world_server = services.WorldServerService(game)
	game.register_service(world_server)

	replica = replica_service.ReplicaService(game)
	game.register_service(replica)

	world = services.WorldService(game)
	game.register_service(world)

	game.start()

	console_thread = threading.Thread(target=console_loop)
	console_thread.start()

	loop = asyncio.get_event_loop()
	loop.run_forever()
	loop.close()