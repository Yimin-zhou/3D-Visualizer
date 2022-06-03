"""
User inputs to control the cam or object
"""
import pygame as pg
import matrix


def camera_control(cam, moving_speed, rotation_speed):
    key = pg.key.get_pressed()

    if key[pg.K_a]:
        cam.position = cam.position - cam.right * moving_speed
    if key[pg.K_d]:
        cam.position = cam.position + cam.right * moving_speed
    if key[pg.K_w]:
        cam.position = cam.position + cam.forward * moving_speed
    if key[pg.K_s]:
        cam.position = cam.position - cam.forward * moving_speed
    if key[pg.K_e]:
        cam.position = cam.position + cam.up * moving_speed
    if key[pg.K_q]:
        cam.position = cam.position - cam.up * moving_speed

    if key[pg.K_LEFT]:
        cam.forward, cam.right, cam.up = camera_yaw(cam, -rotation_speed)
    if key[pg.K_RIGHT]:
        cam.forward, cam.right, cam.up = camera_yaw(cam, rotation_speed)
    if key[pg.K_UP]:
        cam.forward, cam.right, cam.up = camera_pitch(cam, -rotation_speed)
    if key[pg.K_DOWN]:
        cam.forward, cam.right, cam.up = camera_pitch(cam, rotation_speed)


def camera_yaw(cam, angle):
    rotate = matrix.rotate_y_matrix(angle)
    return cam.forward @ rotate, cam.right @ rotate, cam.up @ rotate


def camera_pitch(cam, angle):
    rotate = matrix.rotate_x_matrix(angle)
    return cam.forward @ rotate, cam.right @ rotate, cam.up @ rotate
