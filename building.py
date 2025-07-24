# Import necessary libraries
import os

# Definition of the Building class
class Building:
	"""
	Class representing a building.
	"""
	def __init__(self, name: str, width_m: float, depth_m: float, floor_height_m: float, 
			     n_stories_above_floor: int, n_stories_below_floor: int):
		"""
		Initialize the Building object with its properties.
		:param name: Name of the building.
		:param width_m: Width of the building in meters (x axis).
		:param depth_m: Depth of the building in meters (y axis).
		:param floor_height_m: Height of each floor in meters (z axis).
		:param n_stories_above_floor: Number of stories above the ground floor.
		:param n_stories_below_floor: Number of stories below the ground floor.
		"""
		self.name = name
		self.width_m = width_m
		self.depth_m = depth_m
		self.floor_height_m = floor_height_m
		self.n_stories_above_floor = n_stories_above_floor
		self.n_stories_below_floor = n_stories_below_floor