
"""

 Author P. Arun Babu
 This software is released in ISC License

"""

import os
import random

random.seed(None)

Symbols =  r"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Symbols += r"~!@#$%^&*()-_+={}[];:>/?<>,." # Make captcha difficult

Fonts = [
	"AvantGarde-Book",
	"AvantGarde-BookOblique",
	"AvantGarde-Demi",
	"AvantGarde-DemiOblique",
	"Bookman-Demi",
	"Bookman-DemiItalic",
	"Bookman-Light",
	"Bookman-LightItalic",
	"Courier",
	"Courier-Bold",
	"Courier-Oblique",
	"Courier-BoldOblique",
	"fixed",
	"Helvetica",
	"Helvetica-Bold",
	"Helvetica-Oblique",
	"Helvetica-BoldOblique",
	"Helvetica-Narrow",
	"Helvetica-Narrow-Oblique",
	"Helvetica-Narrow-Bold",
	"Helvetica-Narrow-BoldOblique",
	"NewCenturySchlbk-Roman",
	"NewCenturySchlbk-Italic",
	"NewCenturySchlbk-Bold",
	"NewCenturySchlbk-BoldItalic",
	"Palatino-Roman",
	"Palatino-Italic",
	"Palatino-Bold",
	"Palatino-BoldItalic",
	"Times-Roman",
	"Times-Bold",
	"Times-Italic",
	"Times-BoldItalic",
	# "Symbol", # lets not use symbol font !
]

def random_xy ():
	return str(random.randint(0,400)) +"," + str(random.randint(0,85)) + " " 

def random_color ():
	return "#" + "".join(random.sample('01234567890ABCDEF',6))

def gen_captcha (save_as = "out.png"):
#
	n 	= 4 + random.randint(0,100)%3 		# generate 4-6 chars 
	captcha = "".join(random.sample(Symbols, n)) 

	implode = str(random.uniform(0.1,0.16))
	implode = implode[:4]

	convert_cmd  = "convert -implode " +implode+  " -size 400x85 plasma:grey50-grey50 -channel RGBA "

	for i in xrange(0,random.randint(6,25)):	
		line_color = random.choice(['gray', 'black', 'yellow'])
		convert_cmd += " -fill none -stroke " + line_color +  " -draw 'bezier " + random_xy() + random_xy() + random_xy() + random_xy() +"' -stroke none " 

	# x,y where captcha chars will be drawn 
	y = 40 + random.randint(0,10)

	captcha = captcha.replace("\\","\\\\")

	for c in captcha:
	#
		color_1 = random_color () 
		color_2 = random_color () 

		font = random.choice(Fonts)

		convert_cmd += " -pointsize " + str(60 + random.randint(0,21)) 
		convert_cmd += " -tile gradient:" + color_1 + "-" + color_2 

		x = 65 + random.randint(0,6) * ( (-1)**random.randint(0,1) )
		convert_cmd += " -font " +font+ " -draw \"text "+str(y)+"," + str(x) + "\'" +c+"\'\" "
		y += 55 + random.randint(0,6)
	#


	convert_cmd += " " + save_as

	# print "{"+convert_cmd+"}" # debug 
	convert_cmd = convert_cmd.replace('$','\$')
	os.system(convert_cmd)

	return captcha
#

if __name__ == "__main__":
	print "Generating captcha : "+gen_captcha ("my.png")
