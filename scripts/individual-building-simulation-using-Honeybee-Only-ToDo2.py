from honeybee.model import Model
from honeybee.room import Room
from honeybee_energy.properties.model import ModelEnergyProperties
from honeybee_energy.load import people, lighting, equipment
from honeybee_energy.schedule.fixedinterval import ScheduleFixedInterval as ScheduleFixed
from honeybee_energy.construction.opaque import OpaqueConstruction
from honeybee_energy.material.opaque import EnergyMaterial
from honeybee_energy.simulation.parameter import SimulationParameter
#from honeybee_energy.run import run_energyplus
# 1. Créer une pièce simple (5m x 5m x 3m)
room = Room.from_box('SimpleRoom', 5, 5, 3)
# 2. Définir les propriétés énergétiques
# Matériau de mur simple
material = EnergyMaterial('Generic Wall', 0.2, 0.9, 800, 1000)
construction = OpaqueConstruction('WallConstruction', [material])
room.properties.energy.construction_set = None  # Utiliser des constructions personnalisées
# Charges internes
people = people.People('Occupants', 0.1)  # 0.1 pers/m²
lighting = lighting('Lights', 10)  # 10 W/m²
equipment = equipment.ElectricEquipment('Equipment', 5)  # 5 W/m²
# Horaire constant (présence 24h/24)
schedule = ScheduleFixed('AlwaysOn', 1)
# Appliquer les charges
room.properties.energy.people = people
room.properties.energy.lighting = lighting
room.properties.energy.electric_equipment = equipment
room.properties.energy.people.schedule = schedule
room.properties.energy.lighting.schedule = schedule
room.properties.energy.electric_equipment.schedule = schedule
# 3. Créer le modèle
model = Model('SimpleBuilding', [room])
# 4. Définir les paramètres de simulation
sim_par = SimulationParameter()
# 5. Lancer la simulation (nécessite EnergyPlus installé)
result_folder = './simulation_results'
idf_path, sql_path, zsz_path = run_energyplus(model, sim_par, result_folder)
print(f"Simulation terminée. Résultats :\n- IDF : {idf_path}\n- SQL : {sql_path}")