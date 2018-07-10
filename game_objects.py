import game_types
import components
from pyraknet.bitstream import *

'''
GameObjects are objects placed inside scenes
'''

class GameObject(game_types.BaseObject):
	def __init__(self, parent, zone, object_id : int = None, name : str = "GameObject"):
		super().__init__(parent)
		self._name = name
		self._components = []
		self.zone = zone
		global game
		game = zone.get_parent().get_parent().get_parent()
		if(object_id is None):
			self._object_id = game.generate_object_id()
		else:
			self._object_id = object_id

	def add_component(self, component):
		self._components.append(component)

	def get_component(self, component):
		for object_component in self._components:
			if(object_component.__class__ == component.__class__):
				return object_component

	def get_object_id(self):
		return self._object_id

	def update(self):
		self.zone.update(self)

class ReplicaObject(GameObject):
	def __init__(self, parent, zone, config : dict):
		object_id = None
		name = ""
		if("object_id" in config):
			object_id = config["object_id"]
		if ("name" in config):
			name = config["name"]
		super().__init__(parent, zone, object_id, name)
		self.lot = 0
		self.spawner_id = None
		self.spawner_node_id = None
		self.world_state = None
		self.gm_level = None
		self.json = {}
		self.add_component(components.Transform)
		if("gm_level" in config):
			self.gm_level = config["gm_level"]
		if("world_state" in config):
			self.world_state = config["world_state"]
		if("lot" in config):
			self.lot = config["lot"]
		if("spawner_id" in config):
			self.spawner_id = config["spawner_id"]
		if("spawner_node_id" in config):
			self.spawner_node_id = config["spawner_node_id"]
