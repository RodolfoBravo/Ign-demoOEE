def getUserFirstName():
	userName = system.security.getUsername()
	user = system.user.getUser("", userName)
	return user.get('firstname')
	
def getUserLastName():
	userName = system.security.getUsername()
	user = system.user.getUser("", userName)
	return user.get('lastname')
def verifiedRole(role):
		if role in system.security.getRoles():
			return True
		else:
			return False
			
			
def blankHeaderReport():
	header = [u'Operación',u'Número de Lote',u'Número de Parte',u'Descripción',u'Fecha de Operación']
	dataset=[]
	dat= system.dataset.toDataSet(header,dataset)
	pydat= system.dataset.toPyDataSet(dat)
	return dat