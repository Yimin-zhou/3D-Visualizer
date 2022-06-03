"""
Draw the frames
"""
import numpy as np
import pygame as pg
import control


# def object_movement(object3d):
#


# TODO explain which spaces
def object_to_screen(cam, object3d):
    screen_vertices = cam.camera_to_ndc(object3d.vertices)
    screen_vertices = cam.ndc_to_screen_matrix(screen_vertices)
    return screen_vertices[:, :2]  # only take x,y


class VisualizerRender:
    def __init__(self):
        # initialize program window
        pg.init()
        self.resolution = self.width, self.height = 1600, 900
        self.h_width, self.h_height = self.width // 2, self.height // 2  # surface for drawing
        self.fps = 60
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()

    def draw(self, cam, ob):
        """
        Draw the frame
        """
        # draw background
        self.screen.fill(pg.Color('darkslategray'))
        # draw objects
        # TODO decide render order for each vertex
        for face in ob.faces:
            polygon = object_to_screen(cam, ob)[face]
            if not np.any((polygon == self.h_width) | (polygon == self.h_height)):
                pg.draw.polygon(self.screen, pg.Color('gray'), polygon)
                pg.draw.polygon(self.screen, pg.Color('orange'), polygon, 3)

    def run(self, cam, ob):
        """
        Calls other functions to actually run the program
        """
        while True:
            # camera control
            control.camera_control(cam, 0.02, 0.002)

            # move object
            ob.pivot = -ob.object_x_axis * 0.01 + ob.pivot
            ob.set_vertices(ob.pivot)

            self.draw(cam, ob)

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)
