"""
User inputs to control the cam or object
"""
import pygame as pg
import matrix


def camera_control(cam, moving_speed, rotation_speed):
    key = pg.key.get_pressed()
    cam_position = cam.position
    new_position = cam_position
    right_vector = cam.right
    forward_vector = cam.forward
    up_vector = cam.up

    if key[pg.K_a]:
        new_position = cam_position - right_vector * moving_speed
    if key[pg.K_d]:
        new_position = cam_position + right_vector * moving_speed
    if key[pg.K_w]:
        new_position = cam_position + forward_vector * moving_speed
    if key[pg.K_s]:
        new_position = cam_position - forward_vector * moving_speed
    if key[pg.K_e]:
        new_position = cam_position + up_vector * moving_speed
    if key[pg.K_q]:
        new_position = cam_position - up_vector * moving_speed

    if key[pg.K_LEFT]:
        cam.forward, cam.right, cam.up = camera_yaw(cam, -rotation_speed)
    if key[pg.K_RIGHT]:
        cam.forward, cam.right, cam.up = camera_yaw(cam, rotation_speed)
    if key[pg.K_UP]:
        cam.forward, cam.right, cam.up = camera_pitch(cam, -rotation_speed)
    if key[pg.K_DOWN]:
        cam.forward, cam.right, cam.up = camera_pitch(cam, rotation_speed)

    return new_position


def camera_yaw(cam, angle):
    rotate = matrix.rotate_y_matrix(angle)
    return cam.forward @ rotate, cam.right @ rotate, cam.up @ rotate


def camera_pitch(cam, angle):
    rotate = matrix.rotate_x_matrix(angle)
    return cam.forward @ rotate, cam.right @ rotate, cam.up @ rotate
