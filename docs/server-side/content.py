

class Scene:
	def __init__(self, name, image):
		self.name = name
		self.image = image
		self.parts = []

class Actor:
	def __init__(self, name, image):
		self.name = name
		self.image = image

class Object:
	def __init__(self, name, image):
		self.name = name
		self.image = image


scenes = []

s = Scene('football', 'football.png')
s.text = '{0} wollte mit {1} Fussball spielen'
s.alt_text = 'wollte {0} mit {1} Fussball spielen'
s.parts.append(['actor', 42, 108])
s.parts.append(['object', 98, 194])
scenes.append(s)

s = Scene('brücke', 'brücke.png')
s.text = '{0} ging über die brücke wo {1} ist, um zu {2} kommen'
s.alt_text = 'ging {0} über die brücke wo {1} ist, um zu {2} kommen'
s.parts.append(['actor', 25, 113])
s.parts.append(['object', 111, 204])
s.parts.append(['actor', 235, 107])
scenes.append(s)

s = Scene('kampf', 'kampf.png')
s.text = '{0} schlägt {1} mit {2} und {3} sagt "{4}"'
s.alt_text = 'schlägt {0} {1} mit {2} und {3} sagt "{4}"'
s.parts.append(['actor', 48, 130])
s.parts.append(['actor', 114, 154])
s.parts.append(['object', 93, 137])
s.parts.append(['actor', 203, 140])
s.parts.append(['object', 154, 61])
scenes.append(s)


actors = []

a = Actor('er', 'er.png')
actors.append(a)
a = Actor('der teufel', 'teufel.png')
actors.append(a)
a = Actor('Pi', 'pi.png')
actors.append(a)


objects = []

o = Object('apfel', 'apfel.png')
objects.append(o)
o = Object('ball', 'ball.png')
objects.append(o)
o = Object('pi', 'pi.png')
objects.append(o)