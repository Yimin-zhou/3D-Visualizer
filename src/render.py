"""
Draw the frames
"""
import math

from camera import *
from object import *


class VisualizerRender:
    def __init__(self):
        # initialize program window
        pg.init()
        self.resolution = self.width, self.height = 1600, 900
        self.h_width, self.h_height = self.width // 2, self.height // 2  # surface for drawing
        self.fps = 60
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()

        # create camera
        self.camera = Camera(self, [0.5, 1, -4])

        # create 3d objects
        self.object = Cube(self, [0.2, 0.4, 0.2], [0, math.pi / 6, 0], 1)

    def object_to_screen(self):
        screen_vertices = self.camera.camera_to_ndc(self.object.vertices)
        screen_vertices = self.camera.ndc_to_screen_matrix(screen_vertices)
        return screen_vertices[:, :2]  # only take x,y

    def draw(self):
        """
        Draw the frame
        """
        # draw background
        self.screen.fill(pg.Color('darkslategray'))
        # draw objects
        # TODO decide render order for each vertex
        for face in self.object.faces:
            polygon = self.object_to_screen()[face]
            if not np.any((polygon == self.h_width) | (polygon == self.h_height)):
                pg.draw.polygon(self.screen, pg.Color('gray'), polygon)
                pg.draw.polygon(self.screen, pg.Color('orange'), polygon, 3)

    def run(self):
        """
        Calls other functions to actually run the program
        """
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)
