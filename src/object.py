"""
3d objects in homogeneous coordinates, with transform functions, left hand
"""
import pygame as pg
from matrix import *


class Obejct3D:
    def __init__(self, render, init_position, init_rotation, init_scale):
        self.render = render
        self.vertices = np.array([
            [0, 0, 0, 1],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1],
        ])
        self.faces = np.array([
            [0, 1, 2, 3],
        ])

        # set initial transform
        self.set_init_transform(init_position, init_rotation, init_scale)

    def translate_object(self, pos):
        self.vertices = self.vertices @ translate_matrix(pos)

    def scale_object(self, scal_mul):
        self.vertices = self.vertices @ scale_matrix(scal_mul)

    def rotate_x_object(self, angle):
        self.vertices = self.vertices @ rotate_x_matrix(angle)

    def rotate_y_object(self, angle):
        self.vertices = self.vertices @ rotate_y_matrix(angle)

    def rotate_z_object(self, angle):
        self.vertices = self.vertices @ rotate_z_matrix(angle)

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

        self.vertices = np.array([
            [0, 0, 0, 1],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 0, 1, 1],
        ])
        self.faces = np.array([
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [1, 2, 6, 5],
            [0, 3, 7, 4],
            [1, 5, 0, 4],
            [2, 6, 7, 3],
        ])

        # set initial transform
        self.set_init_transform(init_position, init_rotation, init_scale)


