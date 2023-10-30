class apilog:
	def __init__(self):
		None
	def put(self, value, type="none"):
		if type == "none":
			rend = open("renderity_console.temp","r").read()
			open("renderity_console.temp","w").write(rend+str(value)+"<br>")
		elif type == "danger":
			rend = open("renderity_console.temp","r").read()
			open("renderity_console.temp","w").write(rend+"<span style='color:red;'>[]</span> "+str(value)+" <span style='color:red;'>[]</span>"+"<br>")
		elif type == "warning":
			rend = open("renderity_console.temp","r").read()
			open("renderity_console.temp","w").write(rend+"<span style='color:yellow;'>[]</span> "+str(value)+" <span style='color:yellow;'>[]</span>"+"<br>")
		elif type == "success":
			rend = open("renderity_console.temp","r").read()
			open("renderity_console.temp","w").write(rend+"<span style='color:green;'>[]</span> "+str(value)+" <span style='color:green;'>[]</span>"+"<br>")
		elif type == "primary":
			rend = open("renderity_console.temp","r").read()
			open("renderity_console.temp","w").write(rend+"<span style='color:#0098FF;'>[]</span> "+str(value)+" <span style='color:#0098FF;'>[]</span>"+"<br>")
		return True
	def clear(self):
		open("renderity_console.temp","w").write("")
		return True