def getLiveAnalysisTagPath(eqPath):
 
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
def suma(x,y):
	return x+y
def rest(x,y):
	return x-y
