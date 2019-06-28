import bpy
import random
import numpy

for ii in range(1000):
    # Size
    size = random.uniform(0.5,2)
    # Location
    loc=[
        random.uniform(-5,5),
        random.uniform(-5,5),
        random.uniform(0.6,5)
    ]

    # Rotation
    rot=[numpy.deg2rad(90),0,0]

    bpy.ops.mesh.primitive_cube_add(
        size=size,
        location=loc,
        rotation=rot,
        enter_editmode=True
    )
    bpy.ops.rigidbody.object_add()
    bpy.context.object.rigid_body.mass = 100*size**3
    bpy.context.object.rigid_body.collision_shape = 'MESH'

    # Get data from spawned object
    cube = bpy.context.active_object
    #lastLoc = cube.location

    # Bisecting
    for jj in range(4):
        point = cube.location.copy()
        normal = [
                random.uniform(-1,1),
                random.uniform(-1,1),
                random.uniform(-1,1)
        ]

        for kk in range(3):
            point[kk] = point[kk] + random.uniform(-1,1)*size

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bisect(
            plane_co=point,
            plane_no=normal,
            use_fill=True,
            clear_inner=False,
            clear_outer=True,
            xstart=234,
            xend=408,
            ystart=410,
            yend=420)

    # Semi smooth borders
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bevel(
        offset=0.01*size,
        offset_pct=0,
        segments=3,
        release_confirm=True
    )

    bpy.ops.object.editmode_toggle()
    bpy.ops.object.select_all(action='DESELECT')
