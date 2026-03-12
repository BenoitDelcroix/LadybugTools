from honeybee_energy.lib.materials import OPAQUE_MATERIALS
from honeybee_energy.lib.materials import opaque_material_by_identifier
from honeybee_energy.lib.constructions import opaque_construction_by_identifier



from honeybee_energy.lib.construction import LIGHT_WEIGHT_WALL_R_2
from honeybee_energy.lib.hvac import PTAC_ALL_AIR
from honeybee_energy.model import Model
from honeybee_energy.hvac.allair import PTAC
from honeybee_energy.room import Room
from honeybee_energy.geometry.aperture import Aperture

def generate_base_idf_with_hb(output_filename="honeybee_base_file.idf"):
    """
    Generates a base IDF file with a single thermal zone using Honeybee Energy.
    """
    
    # --- 1. Define a Thermal Zone (Room) ---
    # Define the coordinates for a simple 10m x 10m x 3m high room.
    # The 'Room.from_box' method automatically creates walls, floor, and ceiling.
    room_name = "Office_Zone_1"
    room = Room.from_box(
        name=room_name,
        width=10, 
        depth=10, 
        height=3,
        base_plane='XY' # Creates a floor at Z=0
    )
    print(f"Created a thermal zone: {room_name}")

    # Optionally, add a window to the South wall
    # This assumes the south-facing wall is the one with the normal vector (0, 1, 0)
    # in the default box creation.
    # We grab the South-facing wall (the 4th surface in the list)
    south_wall = room.faces[3] 
    
    # Create a simple 2m x 1.5m aperture (window) in the center of the wall
    aperture = Aperture.from_size(
        name='Window_S', 
        width=2, 
        height=1.5,
        base_plane=south_wall.plane
    )
    # Add the aperture to the wall
    south_wall.add_aperture(aperture)
    print("Added a window to the South wall.")

    # --- 2. Add Constructions and HVAC ---
    # Apply a light-weight construction (R-2 wall) to all opaque surfaces.
    # Honeybee uses library objects for typical constructions.
    room.apply_construction(LIGHT_WEIGHT_WALL_R_2)
    print("Applied LIGHT_WEIGHT_WALL_R_2 construction.")

    # Apply a Packaged Terminal Air Conditioner (PTAC) system to the zone.
    # This is a common single-zone system type.
    ptac_hvac = PTAC_ALL_AIR()
    
    # --- 3. Create a Model ---
    # Assemble the zone(s), HVAC, and required simulation settings into a Model object.
    model = Model(
        name='Base_Model_HB',
        rooms=[room],
        hvacs=[ptac_hvac],
        version=9.6 # Set the EnergyPlus version
    )
    print("Assembled all components into the Honeybee Model object.")
    
    # --- 4. Export to IDF ---
    try:
        # The 'to_idf' method handles all the necessary object creation 
        # (Zone, Material, Construction, AirLoopHVAC, etc.)
        model.to_idf(output_filename)
        print(f"\n✅ Successfully generated base IDF file: **{output_filename}**")
        print("This file includes geometry, constructions, a basic HVAC system, and simulation controls.")
    except Exception as e:
        print(f"\n❌ An error occurred while saving: {e}")
        print("Check if you have EnergyPlus installed and the IDD file is accessible if the error persists.")


# ====================================================================

if __name__ == '__main__':
    generate_base_idf_with_hb()