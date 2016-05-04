
"""
 Author P. Arun Babu
 This software is released in ISC License

"""

import os
import random

random.seed(None)

Symbols = r"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()-_+={}[];:>\/?<>,."

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

n = random.randint(0,100)
captcha = "".join(random.sample(Symbols, n%3 + 4))

print "Captcha is ",captcha

convert_cmd  = "convert -size 400x85 plasma:grey50-grey50 -channel RGBA "

y = 40 + random.randint(0,10)

for c in captcha:

	color_1 = "#" + "".join(random.sample('01234567890ABCDEF',6))
	color_2 = "#" + "".join(random.sample('01234567890ABCDEF',6))

	font = random.choice(Fonts)

	convert_cmd += " -pointsize " + str(60 + random.randint(0,21)) 
	convert_cmd += " -tile gradient:" + color_1 + "-" + color_2 
	convert_cmd += " -font " +font+ " -draw \"text "+str(y)+",65 \'" +c+"\'\" "

	y += 55 + random.randint(0,6)
	x = 65 + random.randint(0,6) * ( (-1)**random.randint(0,1) )

rotate = random.randint(0,20) # Though rotating is good, it makes it difficult for user !

convert_cmd += " out.png"

# print "{"+convert_cmd+"}" 
convert_cmd = convert_cmd.replace('$','\$')
os.system(convert_cmd)
