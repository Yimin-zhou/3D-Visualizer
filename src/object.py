"""
3d objects in homogeneous coordinates, with transform functions, left hand
"""
import numpy as np
import matrix as matrix


class Obejct3D:
    def __init__(self, render, init_position, init_rotation, init_scale):
        self.render = render
        # world space
        self.world_z_axis = np.array([0, 0, 1])
        self.world_y_axis = np.array([0, 1, 0])
        self.world_x_axis = np.array([1, 0, 0])
        # object space
        self.object_z_axis = np.array([0, 0, 1])
        self.object_y_axis = np.array([0, 1, 0])
        self.object_x_axis = np.array([1, 0, 0])
        self.pivot = np.array([0, 0, 0])
        # set pivot and object axes
        self.set_initial_object_axis(init_position, init_scale, init_rotation)
        self.vertices = np.array([
            [*self.pivot, 1],
            [*(self.pivot + self.object_y_axis), 1],
            [*(self.pivot + self.object_y_axis + self.object_x_axis), 1],
            [*(self.pivot + self.object_x_axis), 1],
            [*(self.pivot + self.object_z_axis), 1],
            [*(self.pivot + self.object_y_axis + self.object_z_axis), 1],
            [*(self.pivot + self.object_y_axis + self.object_x_axis + self.object_z_axis), 1],
            [*(self.pivot + self.object_x_axis + self.object_z_axis), 1],
        ])
        self.faces = np.array([
            [4, 7, 6, 5],
            [5, 4, 0, 1],
            [4, 7, 3, 0],
            [1, 5, 6, 2],
            [3, 7, 6, 2],
            [1, 2, 3, 0],
        ])
        # set initial transform
        self.set_init_transform(init_position, init_rotation, init_scale)

    def set_vertices(self, pivot):
        self.vertices = np.array([
            [*pivot, 1],
            [*(pivot + self.object_y_axis), 1],
            [*(pivot + self.object_y_axis + self.object_x_axis), 1],
            [*(pivot + self.object_x_axis), 1],
            [*(pivot + self.object_z_axis), 1],
            [*(pivot + self.object_y_axis + self.object_z_axis), 1],
            [*(pivot + self.object_y_axis + self.object_x_axis + self.object_z_axis), 1],
            [*(pivot + self.object_x_axis + self.object_z_axis), 1],
        ])

    def set_initial_object_axis(self, pos, scal_mul, init_rotation):
        self.pivot = ((np.array([*self.pivot, 1])) @ matrix.translate_matrix(pos))[:3]
        self.object_z_axis = ((np.array([*self.object_z_axis, 1])) @ matrix.rotate_x_matrix(init_rotation[0]))[:3]
        self.object_z_axis = ((np.array([*self.object_z_axis, 1])) @ matrix.rotate_y_matrix(init_rotation[1]))[:3]
        self.object_z_axis = ((np.array([*self.object_z_axis, 1])) @ matrix.rotate_z_matrix(init_rotation[2]))[:3]
        self.object_y_axis = ((np.array([*self.object_y_axis, 1])) @ matrix.rotate_x_matrix(init_rotation[0]))[:3]
        self.object_y_axis = ((np.array([*self.object_y_axis, 1])) @ matrix.rotate_y_matrix(init_rotation[1]))[:3]
        self.object_y_axis = ((np.array([*self.object_y_axis, 1])) @ matrix.rotate_z_matrix(init_rotation[2]))[:3]
        self.object_x_axis = ((np.array([*self.object_x_axis, 1])) @ matrix.rotate_x_matrix(init_rotation[0]))[:3]
        self.object_x_axis = ((np.array([*self.object_x_axis, 1])) @ matrix.rotate_y_matrix(init_rotation[1]))[:3]
        self.object_x_axis = ((np.array([*self.object_x_axis, 1])) @ matrix.rotate_z_matrix(init_rotation[2]))[:3]

    def translate_object(self, pos):
        self.vertices = self.vertices @ matrix.translate_matrix(pos)

    def scale_object(self, scal_mul):
        self.vertices = self.vertices @ matrix.scale_matrix(scal_mul)

    def rotate_x_object(self, angle):
        self.vertices = self.vertices @ matrix.rotate_x_matrix(angle)

    def rotate_y_object(self, angle):
        self.vertices = self.vertices @ matrix.rotate_y_matrix(angle)

    def rotate_z_object(self, angle):
        self.vertices = self.vertices @ matrix.rotate_z_matrix(angle)

    def set_init_position(self, init_position):
        self.translate_object(init_position)

    def set_init_scale(self, init_scale):
        self.scale_object(init_scale)

    def set_init_rotation(self, init_rotation):
        self.rotate_x_object(init_rotation[0])
        self.rotate_y_object(init_rotation[1])
        self.rotate_z_object(init_rotation[2])

    def set_init_transform(self, init_position, init_rotation, init_scale):
        self.set_init_position(init_position)
        self.set_init_rotation(init_rotation)
        self.set_init_scale(init_scale)


class Cube(Obejct3D):
    def __init__(self, render, init_position, init_rotation, init_scale):
        super().__init__(render, init_position, init_rotation, init_scale)
        # # world space
        # self.world_z_axis = np.array([0, 0, 1])
        # self.world_y_axis = np.array([0, 1, 0])
        # self.world_x_axis = np.array([1, 0, 0])
        # # object space
        # self.object_z_axis = np.array([0, 0, 1])
        # self.object_y_axis = np.array([0, 1, 0])
        # self.object_x_axis = np.array([1, 0, 0])
        # self.pivot = np.array([0, 0, 0])
        # self.set_initial_object_axis(init_position, init_scale, init_rotation)
        self.vertices = np.array([
            [*self.pivot, 1],
            [*(self.pivot + self.object_y_axis), 1],
            [*(self.pivot + self.object_y_axis + self.object_x_axis), 1],
            [*(self.pivot + self.object_x_axis), 1],
            [*(self.pivot + self.object_z_axis), 1],
            [*(self.pivot + self.object_y_axis + self.object_z_axis), 1],
            [*(self.pivot + self.object_y_axis + self.object_x_axis + self.object_z_axis), 1],
            [*(self.pivot + self.object_x_axis + self.object_z_axis), 1],
        ])
        self.faces = np.array([
            [4, 7, 6, 5],
            [5, 4, 0, 1],
            [4, 7, 3, 0],
            [1, 5, 6, 2],
            [3, 7, 6, 2],
            [1, 2, 3, 0],
        ])

        # set initial transform
        # self.set_init_transform(init_position, init_rotation, init_scale)

    def set_vertices(self, pivot):
        self.vertices = np.array([
            [*pivot, 1],
            [*(pivot + self.object_y_axis), 1],
            [*(pivot + self.object_y_axis + self.object_x_axis), 1],
            [*(pivot + self.object_x_axis), 1],
            [*(pivot + self.object_z_axis), 1],
            [*(pivot + self.object_y_axis + self.object_z_axis), 1],
            [*(pivot + self.object_y_axis + self.object_x_axis + self.object_z_axis), 1],
            [*(pivot + self.object_x_axis + self.object_z_axis), 1],
        ])



