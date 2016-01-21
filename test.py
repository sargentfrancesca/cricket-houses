import itertools
from PIL import Image
from os import listdir
from os.path import isfile, join
import sys, os.path
from time import strftime


def construct_names(options):
	all_names = []
	
	for x, part in enumerate(options):
		array = []
		for i in range(1,9):
			string = part + str(i)
			array.append(string)
		
		all_names.append(array)
	
	return all_names

def generate_image(combination):

	j_file = 'join.png'
	join = Image.open(j_file, 'r')
	join_w, join_h = join.size

	g_file = 'full/' + combination[0] + ".png"
	ground = Image.open(g_file, 'r')
	ground_w, ground_h = ground.size

	pixels = list(ground.getdata())
	width, height = ground.size
	pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

	print pixels

	m_file = 'full/' + combination[1] + ".png"
	middle = Image.open(m_file, 'r')
	middle_w, middle_h = middle.size

	r_file = 'full/' + combination[2] + ".png"
	roof = Image.open(r_file, 'r')
	roof_w, roof_h = roof.size	

	total_height = ground_h + roof_h + middle_h

	background = Image.new('RGBA', (1440, total_height), (255, 255, 255, 0))
	bg_w, bg_h = background.size

	ground_offset = ((bg_w - ground_w) / 2, total_height - ground_h)
	background.paste(ground, ground_offset, mask=ground)

	join_from_top = int(roof_h * 0.69)
	join_from_bottom = int(roof_h * 0.307)

	print join_from_top, join_from_bottom

	middle_offset = ((bg_w - ground_w) / 2, join_from_top)
	background.paste(middle, middle_offset, mask=middle)

	roof_offset = ((bg_w - ground_w) / 2, 0)
	background.paste(roof, roof_offset, mask=roof)


	background.paste(join, ground_offset, mask=join)
	background.paste(join, middle_offset, mask=join)
	background.paste(join, roof_offset, mask=join)

	filename = combination[0] + combination[1] + combination[2] + '.png'

	print filename

	# background.save('dev/' + filename)

def process_all_images():
	options = ["ground", "middle", "roof"]

	name_list = construct_names(options)

	all_options = list(itertools.product(*name_list))

	combination = list(all_options[1])

	generate_image(combination)

	# for a in all_options:
	# 	combination = list(a)	
	# 	generate_image(combination)

def process_image(ground, middle, roof):
	ground_img = 'ground'+str(ground)
	middle_img = 'middle'+str(middle)
	roof_img = 'roof'+str(roof)

	combination = [ground_img, middle_img, roof_img]

	generate_image(combination)


if __name__ == '__main__':
	ground_arg = sys.argv[1]
	middle_arg = sys.argv[2]
	roof_arg = sys.argv[3]

	process_image(ground_arg,middle_arg,roof_arg)







