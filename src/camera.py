"""
camera and space transform
"""
from matrix import *


class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0])

        # object space
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.height / render.width)
        self.near_plane = 0.1
        self.far_plane = 100

    def camera_translate_matrix(self):
        """
        M
        """
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def camera_rotate_matrix(self):
        """
        V
        """
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_mv_matrix(self):
        """
        MV
        """
        return self.camera_translate_matrix() @ self.camera_rotate_matrix()

    def camera_p_matrix(self):
        """
        P
        """
        near = self.near_plane
        far = self.far_plane
        right = math.tan(self.h_fov / 2)
        left = -right
        top = math.tan(self.v_fov / 2)
        bottom = -top

        m00 = 2 / (right - left)
        m11 = 2 / (top - bottom)
        m22 = (far + near) / (far - near)
        m32 = -2 * near * far / (far - near)
        return np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

    def camera_projection(self, vertices):
        """
        MVP
        """
        transformed_vertices = vertices @ self.camera_mv_matrix()
        transformed_vertices = transformed_vertices @ self.camera_p_matrix()
        return transformed_vertices

    def camera_to_ndc(self, vertices):
        """
        to NDC space, and cutoff the vertices
        """
        transformed_vertices = self.camera_projection(vertices)
        transformed_vertices /= transformed_vertices[:, -1].reshape(-1, 1)  # use w to normalize
        transformed_vertices[(transformed_vertices > 1) | (transformed_vertices < -1)] = 0
        return transformed_vertices

    def ndc_to_screen_matrix(self, vertices):
        """
        from NDC to screen space
        """
        hw, hh = self.render.h_width, self.render.h_height
        return vertices @ np.array([
            [hw, 0, 0, 0],
            [0, -hh, 0, 0],
            [0, 0, 1, 0],
            [hw, hh, 0, 1]
        ])
