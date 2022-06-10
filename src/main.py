import render
import camera
import object
import math


def create_camera(re):
    return camera.Camera(re, [0.5, 1, -4], [0 * math.pi / 180, 0, 0])


def create_3dobject(re):
    return object.Cube(re, [0.8, 0.4, 0.2], [0, 30 * math.pi / 180, 0], 1)


def main():
    # init render
    visualizer_render = render.VisualizerRender()

    # init a camera
    cam = create_camera(visualizer_render)

    # create 3d objects
    object3d = create_3dobject(visualizer_render)

    # continuing render the frames
    visualizer_render.run(cam, object3d)


if __name__ == '__main__':
    main()
