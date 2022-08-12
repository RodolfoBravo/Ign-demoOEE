def roles():
	rol = system.security.getRoles()
	data = []
	for i in rol:
		data.append(i)
	return data
