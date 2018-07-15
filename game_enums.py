from enum import *
import game_types

class PacketHeaderEnum(Enum):
	HANDSHAKE = b'S\x00\x00\x00\x00\x00\x00\x00'
	DISCONNECT_NOTIFY = b"S\x00\x00\x01\x00\x00\x00\x00"
	CLIENT_LOGIN_INFO = b'S\x01\x00\x00\x00\x00\x00\x00'
	LOGIN_RESPONSE = b'S\x05\x00\x00\x00\x00\x00\x00'
	CLIENT_USER_SESSION_INFO = b"S\x04\x00\x01\x00\x00\x00\x00"
	CLIENT_MINIFIGURE_LIST_REQUEST = b"S\x04\x00\x02\x00\x00\x00\x00"
	MINIFIGURE_LIST = b"S\x05\x00\x06\x00\x00\x00\x00"
	CLIENT_MINIFIGURE_CREATE_REQUEST = b"S\x04\x00\x03\x00\x00\x00\x00"
	MINIFIGURE_CREATION_RESPONSE = b"S\x05\x00\x08\x00\x00\x00\x00"
	CLIENT_DELETE_MINIFIGURE_REQUEST = b'S\x04\x00\x06\x00\x00\x00\x00'
	WORLD_INFO = b'S\x05\x00\x02\x00\x00\x00\x00'
	CLINET_ENTER_WORLD = b'S\x04\x00\x04\x00\x00\x00\x00'
	CLIENT_LOAD_COMPLETE = b'S\x04\x00\x13\x00\x00\x00\x00'
	DETAILED_USER_INFO = b'S\x05\x00\x04\x00\x00\x00\x00'
	ROUTED_PACKET = b'S\x04\x00\x15\x00\x00\x00\x00'
	CLIENT_GAME_MESSAGE = b'S\x04\x00\x05\x00\x00\x00\x00'
	SERVER_GAME_MESSAGE = b'S\x05\x00\x0c\x00\x00\x00\x00'
	CLIENT_POSITION_UPDATES = b'S\x04\x00\x16\x00\x00\x00\x00'

class ReplicaTypes(IntEnum):
	CONSTRUCTION = 0
	SERIALIZATION = 1

class LoginResponseEnum(IntEnum):
	SUCCESS = 0x01
	BANNED = 0x02
	INVALID_PERM = 0x03
	INVALID_LOGIN_INFO = 0x06
	ACCOUNT_LOCKED = 0x07

class DisconnectionReasonEnum(IntEnum):
	UNKNOWN_ERROR = 0x00
	DUPLICATE_LOGIN = 0x04
	SERVER_SHUTDOWN = 0x05
	SERVER_CANNOT_LOAD_MAP = 0x06
	INVALID_SESSION_KEY = 0x07
	CHARACTER_NOT_FOUND = 0x09
	CHARACTER_CORRUPTION = 0x0a
	KICKED = 0x0b

class ItemLOTs(IntEnum):
	SHIRT_BRIGHT_RED = 4049
	SHIRT_BRIGHT_BLUE = 4083
	SHIRT_BRIGHT_YELLOW = 4117
	SHIRT_DARK_GREEN = 4151
	SHIRT_BRIGHT_ORANGE = 4185
	SHIRT_BLACK = 4219
	SHIRT_DARK_STONE_GRAY = 4253
	SHIRT_MEDIUM_STONE_GRAY = 4287
	SHIRT_REDDISH_BROWN = 4321
	SHIRT_WHITE = 4355
	SHIRT_MEDIUM_BLUE = 4389
	SHIRT_DARK_RED = 4423
	SHIRT_EARTH_BLUE = 4457
	SHIRT_EARTH_GREEN = 4491
	SHIRT_BRICK_YELLOW = 4525
	SHIRT_SAND_BLUE = 4559
	SHIRT_SAND_GREEN = 4593

	PANTS_BRIGHT_RED = 2508
	PANTS_BRIGHT_ORANGE = 2509
	PANTS_BRICK_YELLOW = 2511
	PANTS_MEDIUM_BLUE = 2513
	PANTS_SAND_GREEN = 2514
	PANTS_DARK_GREEN = 2515
	PANTS_EARTH_GREEN = 2516
	PANTS_EARTH_BLUE = 2517
	PANTS_BRIGHT_BLUE = 2519
	PANTS_SAND_BLUE = 2520
	PANTS_DARK_STONE_GRAY = 2521
	PANTS_MEDIUM_STONE_GRAY = 2522
	PANTS_WHITE = 2523
	PANTS_BLACK = 2524
	PANTS_REDDISH_BROWN = 2526
	PANTS_DARK_RED = 2527

class GameMessages(IntEnum):
	SERVER_DONE_LOADING_OBJECTS = 0x066a
	PLAYER_READY = 0x01fd
	READY_FOR_UPDATES = 0x0378

class MinifigureCreationResponseEnum(IntEnum):
	SUCCESS = 0x00
	ID_NOT_WORKING = 0x01
	NAME_NOT_ALLOWED = 0x02
	PREDEFINED_NAME_IN_USE = 0x03
	NAME_IN_USE = 0x04