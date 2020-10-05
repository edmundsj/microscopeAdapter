"""
Creates a near-copy of the thorlabs CP33, modified for one side to mate to a 38mm microscope tube
"""
import openpyscad as ops
plate_width = 45
plate_thickness = 8.9
hole_pitch = 30
hole_length = plate_thickness + 1
hole_offset = 1
rod_diameter = 6.1
rod_hole_diameter = rod_diameter
screw_hole_diameter = 2.5
wall_thickness = 3.0
center_bore_od = 37.8
protrusion_length = 15

cage_plate = ops.Cube([plate_width, plate_width, plate_thickness])
cage_plate = cage_plate.translate([-plate_width/2, -plate_width/2, 0])
rod_holes = [ops.Cylinder(h=hole_length, d=rod_hole_diameter, fn=20) for x in range(4)]
rod_holes[0] = rod_holes[0].translate([hole_pitch/2, hole_pitch/2, hole_offset])
rod_holes[1] = rod_holes[1].translate([-hole_pitch/2, hole_pitch/2, hole_offset])
rod_holes[2] = rod_holes[2].translate([hole_pitch/2, -hole_pitch/2, hole_offset])
rod_holes[3] = rod_holes[3].translate([-hole_pitch/2, -hole_pitch/2, hole_offset])
inner_holes = [ops.Cylinder(h=plate_thickness, d=screw_hole_diameter) for x in range(4)]
inner_holes[0] = inner_holes[0].translate([hole_pitch/2, hole_pitch/2, -hole_offset])
inner_holes[1] = inner_holes[1].translate([-hole_pitch/2, hole_pitch/2, -hole_offset])
inner_holes[2] = inner_holes[2].translate([hole_pitch/2, -hole_pitch/2, -hole_offset])
inner_holes[3] = inner_holes[3].translate([-hole_pitch/2, -hole_pitch/2, -hole_offset])

microscope_cylinder = ops.Cylinder(d=center_bore_od, h=protrusion_length + plate_thickness)
microscope_cylinder = microscope_cylinder.translate([0, 0, -protrusion_length])
center_bore = ops.Cylinder(d=center_bore_od - 2 * wall_thickness, h=protrusion_length + plate_thickness + 1)
center_bore = center_bore.translate([0, 0, -protrusion_length - 0.5])

cage_plate = cage_plate + microscope_cylinder - center_bore - \
        rod_holes[0] - rod_holes[1] - rod_holes[2] - rod_holes[3] - \
        inner_holes[0] - inner_holes[1] - inner_holes[2] - inner_holes[3]

filename = 'thorlabs_microscope_adapter.scad'
cage_plate.write(filename)

with open(filename, 'r+') as scad_file:
    content = scad_file.read()
    scad_file.seek(0, 0)
    scad_file.write('$fa=0.5;\n$fs=0.5;\n')
