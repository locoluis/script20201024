import sys
if len(sys.argv) < 3:
	sys.stderr.write("Use: %s transcriptionfile htmloutputfile\n" % (sys.argv[0],))
	sys.exit(-1)
f = open(sys.argv[1], "rt")
text = f.read()
f.close()
chrs = set(text)

narrow = "BCFISXYdl"
f = open(sys.argv[2], "wt")
f.write("""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Render</title>
<style type="text/css">
.spc { width: 16px; height: 32px; display: inline-block; }
""")
for c in sorted(chrs):
	if c in " \n":
		continue
	w = 32
	if c in narrow:
		w = 16
	f.write(".%(c)s { width: %(w)dpx; height: 32px; background-size: cover; background-image: url(glyphs/%(c)s.png); display: inline-block; }\n" % {"c": c, "w": w})
f.write("""</style>
</head>
<body>
<p>
""")
state = 0
for c in text:
	if c == "\n":
		if state == 1:
			f.write("</p>\n<p>")
			state = 0
		else:
			state = 1
		continue
	if state == 1:
		f.write("<br>\n")
		state = 0
	if c == " ":
		f.write('<i class="spc"></i>')
	else:
		f.write('<i class="%s"></i>' % (c,))
f.write("""
</p>
</body>
</html>
""")
f.close()
