"""
Script de modélisation énergétique d'un bâtiment avec Honeybee (Ladybug Tools)
Ce script définit la géométrie, les propriétés de surface, les systèmes CVC, et les gains internes pièce par pièce.
Nécessite : honeybee-core, honeybee-energy, ladybug_geometry, honeybee-radiance, honeybee-openstudio

Installation (dans un environnement Python propre) :
pip install honeybee-core honeybee-energy ladybug_geometry honeybee-radiance honeybee-openstudio

Attention : Ce script est un draft, à compléter selon le projet et la documentation Honeybee.
"""

from honeybee.room import Room
from honeybee.model import Model
from honeybee_energy.load.people import People
from honeybee_energy.load.lighting import Lighting
from honeybee_energy.load.equipment import ElectricEquipment
from honeybee_energy.hvac.idealair import IdealAirSystem
from honeybee_energy.constructionset import ConstructionSet
from ladybug_geometry.geometry3d.pointvector import Point3D
from ladybug_geometry.geometry3d.face import Face3D

# 1. Définition de la géométrie (exemple : deux pièces simples)
def create_room(name, origin, width, length, height):
    pts = [
        Point3D(origin.x, origin.y, origin.z),
        Point3D(origin.x + width, origin.y, origin.z),
        Point3D(origin.x + width, origin.y + length, origin.z),
        Point3D(origin.x, origin.y + length, origin.z)
    ]
    face_floor = Face3D(pts)
    room = Room.from_floor_face(face_floor, height, name)
    return room

room1 = create_room('Bureau', Point3D(0, 0, 0), 5, 4, 3)
room2 = create_room('Salle de réunion', Point3D(5, 0, 0), 6, 4, 3)

# 2. Définition des propriétés de surface (construction set par défaut)
construction_set = ConstructionSet.from_predefined('Generic Office')

room1.properties.energy.construction_set = construction_set
room2.properties.energy.construction_set = construction_set

# 3. Ajout des systèmes de chauffage/climatisation (Idéal pour un draft)
hvac1 = IdealAirSystem()
hvac2 = IdealAirSystem()
room1.properties.energy.hvac = hvac1
room2.properties.energy.hvac = hvac2

# 4. Ajout des gains internes (occupation, éclairage, équipements électriques)
# Bureau
people_bureau = People('Occupants Bureau', 0.1, schedule='Office Occupancy')
lighting_bureau = Lighting('Eclairage Bureau', 10, schedule='Office Lighting')
equip_bureau = ElectricEquipment('Equipements Bureau', 15, schedule='Office Equipment')
room1.properties.energy.people = [people_bureau]
room1.properties.energy.lighting = [lighting_bureau]
room1.properties.energy.electric_equipment = [equip_bureau]

# Salle de réunion
people_salle = People('Occupants Réunion', 0.2, schedule='Meeting Room Occupancy')
lighting_salle = Lighting('Eclairage Réunion', 12, schedule='Meeting Room Lighting')
equip_salle = ElectricEquipment('Equipements Réunion', 20, schedule='Meeting Room Equipment')
room2.properties.energy.people = [people_salle]
room2.properties.energy.lighting = [lighting_salle]
room2.properties.energy.electric_equipment = [equip_salle]

# 5. Création du modèle complet
model = Model('MonBatiment', [room1, room2])

# 6. Export du modèle au format JSON Honeybee ou simulation EnergyPlus
model_dict = model.to_dict()
import json

with open('mon_batiment_honeybee.json', 'w') as f:
    json.dump(model_dict, f, indent=2)

print("Modélisation énergétique du bâtiment générée et exportée dans mon_batiment_honeybee.json")

# Pour aller plus loin : 
# - Ajoutez des fenêtres avec room.add_aperture()
# - Personnalisez les schedules d'occupation et d'équipement
# - Ajoutez des constructions personnalisées
# - Exportez vers OpenStudio ou EnergyPlus pour la simulation dynamique

# Documentation utile :
# https://www.ladybug.tools/honeybee-energy/docs/
# https://www.ladybug.tools/ladybug-geometry/docs/