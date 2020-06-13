from display import *
from matrix import *
from draw import *

mesh_v = {}
groups = {}

def parse_obj(file):
    global mesh_v
    global groups
    #quads = []
    #triangles = []
    polygons = []
    #g = None
    #count = 0
    v_index = 1
    for index in range(len(file)):
        #print(file[index])
        if 'v ' in file[index]:
            mesh_v[str(v_index)] = file[index].split(' ')
            v_index += 1
        # elif 'g' in file[index]:
        #             if g:
        #                 groups[g] = count
        #                 count = 0
        #                 g = file[index].split(' ')[1]
        #             else:
        #                 g = file[index].split(' ')[1]
        elif 'f ' in file[index]:
            
            face = file[index].split(' ')
            if len(face) > 4:
                if float(face[1]) >= 0:

                    v1 = [float(x) for x in mesh_v[face[1]][1:]]
                    v2 = [float(x) for x in mesh_v[face[2]][1:]]
                    v3 = [float(x) for x in mesh_v[face[3]][1:]]
                    v4 = [float(x) for x in mesh_v[face[4]][1:]]
                    add_polygon(polygons,v1[0],v1[1],v1[2],
                                v2[0],v2[1],v2[2],
                                v3[0],v3[1],v3[2])
                    add_polygon(polygons,v3[0],v3[1],v3[2],
                                v4[0],v4[1],v4[2],
                                v1[0],v1[1],v1[2])

                    # quads.append(mesh_v[face[1]][1:]) 
                    # quads.append(mesh_v[face[2]][1:])
                    # quads.append(mesh_v[face[3]][1:]) 
                    # quads.append(mesh_v[face[4]][1:])
                    
                else:

                    v1 = [float(x) for x in mesh_v[len(mesh_v) + face[1]][1:]]
                    v2 = [float(x) for x in mesh_v[len(mesh_v) + face[2]][1:]]
                    v3 = [float(x) for x in mesh_v[len(mesh_v) + face[3]][1:]]
                    v4 = [float(x) for x in mesh_v[len(mesh_v) + face[4]][1:]]
                    # quads.append(mesh_v[len(mesh_v) + face[1]][1:]) 
                    # quads.append(mesh_v[len(mesh_v) + face[2]][1:])
                    # quads.append(mesh_v[len(mesh_v) + face[3]][1:]) 
                    # quads.append(mesh_v[len(mesh_v) + face[4]][1:])

            else:
                if float(face[1]) >= 0:
                    v1 = [float(x) for x in mesh_v[face[1]][1:]]
                    v2 = [float(x) for x in mesh_v[face[2]][1:]]
                    v3 = [float(x) for x in mesh_v[face[3]][1:]]

                    add_polygon(polygons,v1[0],v1[1],v1[2],
                                v2[0],v2[1],v2[2],
                                v3[0],v3[1],v3[2])
                    # triangles.append(mesh_v[face[1]][1:]) 
                    # triangles.append(mesh_v[face[2]][1:])
                    # triangles.append(mesh_v[face[3]][1:])
                    
                else:

                    v1 = [float(x) for x in mesh_v[len(mesh_v) + face[1]][1:]]
                    v2 = [float(x) for x in mesh_v[len(mesh_v) + face[2]][1:]]
                    v3 = [float(x) for x in mesh_v[len(mesh_v) + face[3]][1:]]

                    add_polygon(polygons,v1[0],v1[1],v1[2],
                                v2[0],v2[1],v2[2],
                                v3[0],v3[1],v3[2])

                    # triangles.append(mesh_v[len(mesh_v) + face[1]][1:]) 
                    # triangles.append(mesh_v[len(mesh_v) + face[2]][1:])
                    # triangles.append(mesh_v[len(mesh_v) + face[3]][1:])
                                   
            #count += 1

    return polygons

def draw_mesh(quads,triangles,screen,zbuffer,color):


    if quads:
        
        for index in range(int(len(quads)/4)):
            temp_index = index * 4
            draw_line(int(float(quads[temp_index][0])),int(float(quads[temp_index][1])),
                      int(float(quads[temp_index][2])),
                      int(float(quads[temp_index + 1][0])),int(float(quads[temp_index + 1][1])),
                      int(float(quads[temp_index + 1][2])),
                      screen, zbuffer,color)
            draw_line(int(float(quads[temp_index + 1][0])),int(float(quads[temp_index + 1][1])),
                      int(float(quads[temp_index + 1][2])),
                      int(float(quads[temp_index + 2][0])),int(float(quads[temp_index + 2][1])),
                      int(float(quads[temp_index + 2][2])),
                      screen, zbuffer,color)
            draw_line(int(float(quads[temp_index + 2][0])),int(float(quads[temp_index + 2][1])),
                      int(float(quads[temp_index + 2][2])),
                      int(float(quads[temp_index + 3][0])),int(float(quads[temp_index + 3][1])),
                      int(float(quads[temp_index + 3][2])),
                      screen, zbuffer,color)
            draw_line(int(float(quads[temp_index + 3][0])),int(float(quads[temp_index + 3][1])),
                      int(float(quads[temp_index + 3][2])),
                      int(float(quads[temp_index][0])),int(float(quads[temp_index][1])),
                      int(float(quads[temp_index][2])),
                      screen, zbuffer,color)
    if triangles:
        for index in range(int(len(triangles)/3)):
            temp_index = index * 3
            draw_line(int(float(quads[temp_index][0])),int(float(quads[temp_index][1])),
                      int(float(quads[temp_index][2])),
                      int(float(quads[temp_index + 1][0])),int(float(quads[temp_index + 1][1])),
                      int(float(quads[temp_index + 1][2])),
                      screen, zbuffer,color)
            draw_line(int(float(quads[temp_index + 1][0])),int(float(quads[temp_index + 1][1])),
                      int(float(quads[temp_index + 1][2])),
                      int(float(quads[temp_index + 2][0])),int(float(quads[temp_index + 2][1])),
                      int(float(quads[temp_index + 2][2])),
                      screen, zbuffer,color)
            draw_line(int(float(quads[temp_index + 2][0])),int(float(quads[temp_index + 2][1])),
                      int(float(quads[temp_index + 2][2])),
                      int(float(quads[temp_index][0])),int(float(quads[temp_index][1])),
                      int(float(quads[temp_index][2])),
                      screen, zbuffer,color)

