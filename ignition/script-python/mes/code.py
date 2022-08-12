def getOEEPath(eqPath):
	tagPath = eqPath
	if tagPath is not None:
		tagPath = tagPath.replace('\\', '/')
		if '[global]/' in (tagPath):
			tagPath = tagPath[len('[global]/'):]    #Remove [global]\
		tagPath = '[default]' + tagPath + '/OEE'
	return tagPath
	
def createOEEUDTTag(tagPath):
	import java
	baseTagPath = tagPath.replace('OEE','')
	try:
		tag = {
			'name':'OEE',
			'tagType':'UdtInstance',
			'typeId': 'eqOEE',
			#'parameters': {'Line':Line}
			}
		collisionPolicy = 'a'
		return system.tag.configure(baseTagPath,[tag],collisionPolicy)
	except java.lang.Exception, value:
		return str(value.getMessage()) 
	
