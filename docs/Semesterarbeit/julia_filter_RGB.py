from PIL import Image, ImageDraw
from multiprocessing.dummy import Pool as ThreadPool
import math
import random
import tqdm
import os

MAX_ITERATIONS = 255

def converge(z, zi, c, ci):
    start_z = z
    start_zi = zi
    iterations = 0
    while (iterations <= MAX_ITERATIONS and (z*z + zi*zi) < 16):
        zz = z*z
        zizi = zi*zi
        mixed = 2*z*zi
        zi = 2*z*zi + ci
        z = zz - zizi + c
        iterations += 1

    if (iterations > MAX_ITERATIONS):
        return True, iterations
    else:
        return False, iterations + math.log2(math.log2(z*z + zi*zi))

def unit_circle(r, angle, deg=True):
    if deg:
        angle = angle*math.pi/180
    return (math.cos(angle) * r, math.sin(angle) * r)

def julia_filter(source, w, c, sens=0.2, angle_offset=0, pos=(0,0), loading=False):

    im = source.convert('RGB')
    px = im.load()

    width, height = im.size
    draw = ImageDraw.Draw(im)

    pos_x = pos[0]
    pos_y = pos[1]

    scale = w/width
    pwidth, pheight = width*scale, height*scale

    width_range = tqdm.tqdm(range(width)) if loading else range(width)

    for x in width_range:    # for every col:
        for y in range(height):    # For every row
            image_pixel = px[x,y]
            light = sum(image_pixel)/3
            if light > 30 and light < 200:
                zx = (x+(0.75-image_pixel[0]/255-image_pixel[1]/255/2)*sens*width/2)/(width/pwidth)-pwidth/2 + pos_x
                zy = (y+(0.75-image_pixel[2]/255-image_pixel[1]/255/2)*sens*height/2)/(height/pheight)-pheight/2 + pos_y
                convergence_red, iterations_red = converge(zx+unit_circle(0.2, angle_offset)[0], zy+unit_circle(0.1, angle_offset)[1], c[0], c[1])
                convergence_blue, iterations_blue = converge(zx+unit_circle(0.2, angle_offset+120)[0], zy+unit_circle(0.1, angle_offset+120)[1], c[0], c[1])
                convergence_green, iterations_green = converge(zx+unit_circle(0.2, angle_offset+240)[0], zy+unit_circle(0.1, angle_offset+240)[1], c[0], c[1])
                red = int((iterations_red)/(MAX_ITERATIONS)*255)
                blue = int((iterations_blue)/(MAX_ITERATIONS)*255)
                green = int((iterations_green)/(MAX_ITERATIONS)*255)
            else:
                red = 255
                blue = 255
                green = 255
            draw.point((x,y), (red, blue, green))
            
    return im


j = 0

def rot_filter(angle):
    im = Image.open('start_images/ducks.jpg')
    print(f'starting {angle}')
    x, y = unit_circle(0.781, angle)
    gen_im = julia_filter(im, 1, (x, y), angle, pos=(0,0), loading=False)
    gen_im.convert('RGB').save(f'ducks_turn4/{angle}.{x}.{y}.png')
    global j
    j += 1
    print(f'done {angle} ({j}/360)')

def rot_filter_init():
    rots = [i for i in range(360)]
    pool = ThreadPool(2)

    results = pool.map(rot_filter, rots)

def single_picture():
    im = Image.open('start_images/ducks.jpg')
    im = julia_filter(im, 1, (-0.7269, -0.1889), sensitivty=0.2, pos=(0,0), loading=True)
    im.convert('RGB').save(f'gen_images/ducks21.png')

def interpolate(angle_points):
    end = []
    last_point = angle_points[0]

    for angle, first in angle_points[1:]:
        distance = first - last_point[1]
        step_size = (angle - last_point[0])/distance
        for i in range(distance):
            end.append((last_point[0]+step_size*i, last_point[1]+i))
        last_point = (angle, first)

    return end

def animation(angle_points):
    path = 'ducktale/'
    angle_points = interpolate(angle_points)
    start = angle_points[0][1]
    end = angle_points[-1][1]
    for i in range(end-start+1):
        frame = start + i
        angle = angle_points[i][0]
        x, y = unit_circle(0.781, angle)
        im_name = 'd' + ''.join(['0' for k in range(4-len(str(start+i)))]) + str(start+i) + '.png'
        print(im_name)
        im = Image.open(path + im_name)
        im = im.resize((960, 540))
        im = julia_filter(im, 1, (x, y), sens=1, pos=(0,0), loading=True)
        im.convert('RGB').save(f'gen_ducktale3/d{frame}.jpg')

def ducktales_keyframed_animation():
    points = [(167, 0),
    (168, 90),
    (92, 98),
    (92, 99),
    (92, 100),
    (92.1, 137),
    (93, 174),
    (108, 190),
    (107.5, 250),
    (107.5, 251),
    (107.5, 255),
    (108, 277),
    (129, 281),
    (128.5, 300),
    (135, 303),
    (134.5, 380),
    (134.5, 381),
    (129, 384),
    (129.5, 393),
    (135, 423),
    (138, 500),
    (144, 506),
    (145, 545),
    (146, 587),
    (147, 646),
    (171, 649),
    (172, 694),
    (189, 699),
    (190, 743),
    (213, 778),
    (212, 781),
    (214, 870),
    (215, 874),
    (214, 912),
    (215, 915),
    (214, 951),
    (216, 953),
    (225, 995),
    (226, 998),
    (225.5, 1044),
    (226, 1075),
    (231, 1080),
    (233, 1117),
    (234, 1158),
    (252, 1165),
    (253, 1195),
    (253.5, 1202),
    (254, 1213),
    (253.5, 1239),
    (268, 1247),
    (267, 1314),
    (267, 1315),
    (271, 1348),
    (360, 1482),
    (0, 1483),
    (90, 1516),
    (93, 1520),
    (107, 1541),
    (108, 1571),
    (128, 1590),
    (135, 1595),
    (170, 1620),
    (165, 1690),
    (171, 1724),
    (188, 1802)]

    animation(points)