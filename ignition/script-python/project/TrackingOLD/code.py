def segExec(eqPath,location,opName,segName,segMatName,matName,qty):
	operRef = system.mes.loadMESObject(opName, 'OperationsDefinition')
	operResp = system.mes.createOperation(operRef)
	system.mes.beginOperation(eqPath,operResp)
	try:	
		oper = system.mes.getCurrentOperation(eqPath)
		seg = oper.createSegment(segName)
		seg.setMaterial(segMatName,matName,location,qty)
	
		return seg.execute()
	except java.lang.Exception, value:
		seg.abort()
		oper.end()
