def getInventoryByEquipmentPath(eqPath):
    #Given an equipment path, this function will return the
    #current available quantity
    qty = 0.0
    if eqPath != '':
     
        results = system.mes.getLotInventoryByEquipment(eqPath,'','*')
        qty = results.getNetQuantitySum()
    return qty
    
def getLiveAnalysisTagPath(eqPath):
         
	# Given an equipmentPath, this function will return the live analysis tag path
	# equipPath comes in the format of [global]\Enterprise\Site\Area\Line
	# which needs to be converted to [MES]Enterprise/Site/Area/Line/Live Analysis
	 
	#print "getEquipmentStatusTagPath called for ", equipPath
	 
	tagPath = eqPath
	if tagPath is not None:
		tagPath = tagPath.replace('\\', '/')
		if '[global]/' in (tagPath):
			tagPath = tagPath[len('[global]/'):]    #Remove [global]\
		tagPath = '[MES]' + tagPath + '/Live Analysis'
	return tagPath
	
def getLiveAnalysisTagPath1(eqPath):
 	tagPath = eqPath
	if tagPath is not None:
		tagPath = tagPath.replace('\\', '/')
		if '[global]/' in (tagPath):
			tagPath = tagPath[len('[global]/'):]    #Remove [global]\
		tagPath = '[MES]' + tagPath + '/Live Analysis/General/'
	return tagPath 
	
def getDefaultTagPath(eqPath): 
	tagPath = eqPath
	if tagPath is not None:
		tagPath = tagPath.replace('\\', '/')
		if '[global]/' in (tagPath):
			tagPath = tagPath[len('[global]/'):]    #Remove [global]\
		tagPath = tagPath + '/'
	return tagPath