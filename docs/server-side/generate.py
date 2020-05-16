import random
from PIL import Image
import os


import content

def path_ext(path):
	return 'images/' + path

def clear_folder():
	for image in os.listdir('static/generated'):
		os.remove(f'static/generated/{image}')

clear_folder()

def generate_image(scene, parts):
	im = Image.open(path_ext(scene.image)).convert('RGBA')
	im = im.resize((256, 256), resample=3)
	for i, p in enumerate(scene.parts):
		part = parts[i]
		part_image = Image.open(path_ext(part.image)).convert('RGBA')
		part_image = part_image.resize((48, 48), resample=3)
		x = p[1] - 24
		y = p[2] - 24
		im.paste(part_image, box=(x, y), mask=part_image)

	path = f'static/generated/{random.randint(10**8,10**9 -1 )}.png'
	im.save(path)
	return path


def generate_scene(actors=[], objects=[]):
	scene = random.choice(content.scenes)
	parts = []
	for t, x, y in scene.parts:
		if t == 'actor':
			if len(actors) < 1:
				parts.append(random.choice(content.actors))
			else:
				parts.append(actors[0])
				del actors[0]
		elif t == 'object':
			if len(objects) < 1:
				parts.append(random.choice(content.objects))
			else:
				parts.append(objects[0])
				del objects[0]
		else:
			raise Exception()

	text = scene.text.format(*[p.name.title() for p in parts])
	alt_text = scene.alt_text.format(*[p.name.title() for p in parts])
	path = generate_image(scene, parts)
	
	return [(text, alt_text), path]

def generate_story():
	actors = [random.choice(content.actors) for i in range(random.randint(1, 1))]
	objects = [random.choice(content.objects) for i in range(random.randint(1, 1))]

	scenes = [generate_scene(actors=actors.copy(), objects=objects.copy()) for i in range(3)]
	scenes[0][0] = scenes[0][0][0]
	scenes[1][0] = ', jedoch ' + scenes[1][0][1]
	scenes[2][0] = ', also ' + scenes[2][0][1] + '.'

	return scenes