# -*- coding: utf-8 -*-
import colorsys
from colorvariation import Color

def complementaryColor(ColorInput):
	# Convert RGB (base 256) to HLS (between 0 and 1 )
	ColorInput.HLS = list(colorsys.rgb_to_hls(ColorInput.RGB[0] / 255, ColorInput.RGB[1] / 255, ColorInput.RGB[2] / 255))

	# Change the Hue value to the Hue opposite
	HueValue = ColorInput.HLS[0] * 360
	ColorInput.HLS[0] = ((HueValue + 180) % 360)/360

	# Convert HLS (between 0 and 1) to RGB (base 256)
	return list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorInput.HLS[0],ColorInput.HLS[1],ColorInput.HLS[2])))

def triadicColor(ColorInput):
	
	# Convert RGB (base 256) to HLS (between 0 and 1 )
	ColorInput.HLS = list(colorsys.rgb_to_hls(ColorInput.RGB[0] / 255, ColorInput.RGB[1] / 255, ColorInput.RGB[2] / 255))
	
	# Find the first triadic Hue
	FirstTriadicHue = ((ColorInput.HLS[0] * 360 + 120) % 360) / 360

	# Find the second triadic Hue
	SecondTriadicHue = ((ColorInput.HLS[0] * 360 + 240) % 360) / 360

	ColorOutput1 = Color("",[FirstTriadicHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")
	ColorOutput2 = Color("",[SecondTriadicHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")

	ColorOutput1.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput1.HLS[0],ColorOutput1.HLS[1],ColorOutput1.HLS[2])))
	ColorOutput2.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput2.HLS[0],ColorOutput2.HLS[1],ColorOutput2.HLS[2])))

	return [ColorOutput1.RGB,ColorOutput2.RGB]

def splitComplementaryColor(ColorInput):
	# Convert RGB (base 256) to HLS (between 0 and 1 )
	ColorInput.HLS = list(colorsys.rgb_to_hls(ColorInput.RGB[0] / 255, ColorInput.RGB[1] / 255, ColorInput.RGB[2] / 255))

	# Find the first triadic Hue
	FirstSplitComplementaryHue = ((ColorInput.HLS[0] * 360 + 150) % 360) / 360

	# Find the second triadic Hue
	SecondSplitComplementaryHue = ((ColorInput.HLS[0] * 360 + 210) % 360) / 360

	ColorOutput1 = Color("",[FirstSplitComplementaryHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")
	ColorOutput2 = Color("",[SecondSplitComplementaryHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")

	ColorOutput1.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput1.HLS[0],ColorOutput1.HLS[1],ColorOutput1.HLS[2])))
	ColorOutput2.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput2.HLS[0],ColorOutput2.HLS[1],ColorOutput2.HLS[2])))

	return [ColorOutput1.RGB,ColorOutput2.RGB]

def tetradicColor(ColorInput):

	# Convert RGB (base 256) to HLS (between 0 and 1 )
	ColorInput.HLS = list(colorsys.rgb_to_hls(ColorInput.RGB[0] / 255, ColorInput.RGB[1] / 255, ColorInput.RGB[2] / 255))

	# Find the first tetradic Hue
	FirstTetradicHue = ((ColorInput.HLS[0] * 360 + 60) % 360) / 360

	# Find the second tetradic Hue
	SecondTetradicHue = ((ColorInput.HLS[0] * 360 + 180) % 360) / 360

	# Find the third tetradic Hue
	ThirdTetradicHue = ((ColorInput.HLS[0] * 360 + 240) % 360) / 360


	ColorOutput1 = Color("",[FirstTetradicHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")
	ColorOutput2 = Color("",[SecondTetradicHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")
	ColorOutput3 = Color("",[ThirdTetradicHue,ColorInput.HLS[1],ColorInput.HLS[2]],"")

	ColorOutput1.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput1.HLS[0],ColorOutput1.HLS[1],ColorOutput1.HLS[2])))
	ColorOutput2.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput2.HLS[0],ColorOutput2.HLS[1],ColorOutput2.HLS[2])))
	ColorOutput3.RGB = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(ColorOutput3.HLS[0],ColorOutput3.HLS[1],ColorOutput3.HLS[2])))

	return [ColorOutput1.RGB,ColorOutput2.RGB,ColorOutput3.RGB]