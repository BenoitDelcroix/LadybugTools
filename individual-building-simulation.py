from dragonfly.model import Model
from dragonfly.building import Building
from dragonfly.story import Story
from dragonfly.room2d import Room2D
from dragonfly.windowparameter import SimpleWindowRatio
from honeybee_energy.lib.programtypes import office_program
from ladybug_geometry.geometry3d.pointvector import Point3D
from ladybug_geometry.geometry3d.face import Face3D

# create the Building object
pts_1 = (Point3D(0, 0, 3), Point3D(0, 10, 3), Point3D(10, 10, 3), Point3D(10, 0, 3))
pts_2 = (Point3D(10, 0, 3), Point3D(10, 10, 3), Point3D(20, 10, 3), Point3D(20, 0, 3))
pts_3 = (Point3D(0, 10, 3), Point3D(0, 20, 3), Point3D(10, 20, 3), Point3D(10, 10, 3))
pts_4 = (Point3D(10, 10, 3), Point3D(10, 20, 3), Point3D(20, 20, 3), Point3D(20, 10, 3))
room2d_1 = Room2D('Office1', Face3D(pts_1), 3)
room2d_2 = Room2D('Office2', Face3D(pts_2), 3)
room2d_3 = Room2D('Office3', Face3D(pts_3), 3)
room2d_4 = Room2D('Office4', Face3D(pts_4), 3)
story = Story('OfficeFloor', [room2d_1, room2d_2, room2d_3, room2d_4])
story.solve_room_2d_adjacency(0.01)
story.set_outdoor_window_parameters(SimpleWindowRatio(0.4))
story.multiplier = 4
building = Building('OfficeBuilding', [story])

# assign energy properties
for room in story.room_2ds:
    room.properties.energy.program_type = office_program
    room.properties.energy.add_default_ideal_air()

# create the Model object
model = Model('NewDevelopment', [building])

# serialize the dragonfly Model to Honeybee Models and convert them to IDF
hb_models = model.to_honeybee('Building', use_multiplier=False, tolerance=0.01)
idfs = [hb_model.to.idf(hb_model) for hb_model in hb_models]

# write the IDF files to disk
i = 0
for idf in idfs:
    i+=1
    with open('idf'+str(i)+'.idf', 'w') as f:
           f.write(idf)

print('IT WORKS!!!')