def getSegmentInfo(segment):
	import java.lang
	try:
		ps = system.mes.loadMESObject(segment, 'ProcessSegment')
		dicSegment = {'Name': ps.getName(), 'Materials': {}}
		propList = ps.getComplexPropertyTypeNames()
		for i in range(propList.size()):
			complexPropType = propList.get(i)
			cnt = ps.getComplexPropertyCount(complexPropType)
			if complexPropType == 'Material':
				for j in range(cnt):
					complexProp = ps.getComplexProperty(complexPropType, j)
					nameComplexProperty = complexProp.getName()
					UUIDEquipment = complexProp.getValue('MaterialEquipmentRefUUID')
					LotSource = complexProp.getValue('MaterialLotNoSource')
					Use = complexProp.getValue('MaterialUse')
					Matref = complexProp.getValue('MaterialRef')
					Matref = (Matref.split(', '))[1]
					if Use == 'Out':
						matEqPath = system.mes.loadMESObject(UUIDEquipment).getEquipmentPath()
					else:  # In
						matEqPath = system.mes.loadMESObject(UUIDEquipment).getEquipmentPath()
					MaterialProperties = dict(matEqPath=matEqPath,
											  LotSource=LotSource,
											  Use=Use,
											  Matref=Matref)
					dicSegment['Materials'][nameComplexProperty] = MaterialProperties
			if complexPropType == 'Equipment':
				for j in range(cnt):
					complexProp = ps.getComplexProperty(complexPropType, j)
					UUIDEquipment = complexProp.getValue('EquipmentRefUUID')
					segEqPath = system.mes.loadMESObject(UUIDEquipment).getEquipmentPath()
					dicSegment['Equipment'] = segEqPath
		return {'Status':True,'Value':dicSegment}
	except java.lang.Exception, value:
		print "Error = %s", str(value.getMessage())
		return {'Status':False,'Value':str(value.getMessage())}

def executeSegment(segment,lotNumbers):
					import java.lang
					result = shared.Tracking.getSegmentInfo(segment)
					dicSegment=result['Value']
					try:
						seg = system.mes.createSegment(dicSegment['Name'], dicSegment['Equipment'], False, True)
						#seg = system.mes.getActiveSegment( dicSegment['Equipment'],dicSegment['Name'])		
						for materialPropertyName in dicSegment['Materials']:
							currentMatProperties = dicSegment['Materials'][materialPropertyName]
							if currentMatProperties['Use'] == 'In':
								print str(materialPropertyName) + ' Found'
								seg.setMaterial(materialPropertyName, lotNumbers[materialPropertyName],-1,1)
								print str(materialPropertyName) + ' Done'
						for materialPropertyName in dicSegment['Materials']:
								currentMatProperties = dicSegment['Materials'][materialPropertyName]
								if currentMatProperties['Use'] == 'Out' and currentMatProperties['LotSource'] == 'Manual':  # Execute Segment Mat out for Transition
									# seg.setMaterial('Out Material','3666499','Enterprise\Site\Area\Line 1', '0000537000000000001', quantity)
									print str(materialPropertyName) + ' Found'
									seg.setMaterial(materialPropertyName, currentMatProperties['Matref'], currentMatProperties['matEqPath'], lotNumbers[materialPropertyName], 1)
									print str(materialPropertyName) + ' Done'
								#print 'mat done'
						#seg.setPersonnel("Quality Inspector",'Inspector')
						#seg.executeImmediately()
						#seg.update()
						seg.execute()
						return {'Status':True,'Value':dicSegment['Name']}
					except java.lang.Exception, value:
						return {'Status':False,'Value':str(value.getMessage())}


def executeSegmentLot(segment,lotNumbers):
											import java.lang
											result = shared.Tracking.getSegmentInfo(segment)
											dicSegment=result['Value']
											try:
												seg = system.mes.createSegment(dicSegment['Name'], dicSegment['Equipment'], False, True)
												#seg = system.mes.getActiveSegment( dicSegment['Equipment'],dicSegment['Name'])		
												for materialPropertyName in dicSegment['Materials']:
													currentMatProperties = dicSegment['Materials'][materialPropertyName]
													if currentMatProperties['Use'] == 'In':
														print str(materialPropertyName) + ' Found'
														#seg.setMaterial(materialPropertyName, lotNumbers[materialPropertyName],1,1)
														seg.setMaterialBypassChecks(materialPropertyName, lotNumbers[materialPropertyName],1,1)
														print str(materialPropertyName) + ' Done'
												for materialPropertyName in dicSegment['Materials']:
														currentMatProperties = dicSegment['Materials'][materialPropertyName]
														if currentMatProperties['Use'] == 'Out' and currentMatProperties['LotSource'] == 'Manual':  # Execute Segment Mat out for Transition
															# seg.setMaterial('Out Material','3666499','Enterprise\Site\Area\Line 1', '0000537000000000001', quantity)
															print str(materialPropertyName) + ' Found'
															seg.setMaterial(materialPropertyName, currentMatProperties['Matref'], currentMatProperties['matEqPath'], lotNumbers[materialPropertyName], 1)
															print str(materialPropertyName) + ' Done'
														#print 'mat done'
												#seg.setPersonnel("Quality Inspector",'Inspector')
												#seg.executeImmediately()
												#seg.update()
												seg.execute()
												return {'Status':True,'Value':dicSegment['Name']}
											except java.lang.Exception, value:
												return {'Status':False,'Value':str(value.getMessage())}



def executeSegmentIn(segment,lotNumbers):
	import java.lang
	result = shared.Tracking.getSegmentInfo(segment)
	dicSegment=result['Value']
	try:
		seg = system.mes.createSegment(dicSegment['Name'], dicSegment['Equipment'], False, True)
		#seg = system.mes.getActiveSegment( dicSegment['Equipment'],dicSegment['Name'])		
		for materialPropertyName in dicSegment['Materials']:
			currentMatProperties = dicSegment['Materials'][materialPropertyName]
			if currentMatProperties['Use'] == 'In':
				print str(materialPropertyName) + ' Found'
				seg.setMaterial(materialPropertyName, lotNumbers[materialPropertyName],1)
				print str(materialPropertyName) + ' Done'
		for materialPropertyName in dicSegment['Materials']:
				currentMatProperties = dicSegment['Materials'][materialPropertyName]
				if currentMatProperties['Use'] == 'Out' and currentMatProperties['LotSource'] == 'Manual':  # Execute Segment Mat out for Transition
					# seg.setMaterial('Out Material','3666499','Enterprise\Site\Area\Line 1', '0000537000000000001', quantity)
					print str(materialPropertyName) + ' Found'
					seg.setMaterial(materialPropertyName, currentMatProperties['Matref'], currentMatProperties['matEqPath'], lotNumbers[materialPropertyName], 5)
					print str(materialPropertyName) + ' Done'
		#seg.executeImmediately()
		seg.execute()
		return {'Status':True,'Value':dicSegment['Name']}
	except java.lang.Exception, value:
		return {'Status':False,'Value':str(value.getMessage())}

def printSegmentInfo(segment):
	result = getSegmentInfo(segment)
	if result['Status']==True:
		dicSegment=result['Value']
		for item in dicSegment:
			if item == 'Materials':
				print item
				for mat in dicSegment[item]:	
					Materials=dicSegment[item][mat]
					print Materials['Use']  + ': "'+  mat +'" "'+ Materials['Matref'] +'" '+ Materials['matEqPath']
				print ''
			else:
				print item
				print dicSegment[item]
				print ''
	else:
		print result['Value']


def genlotNumberHFTube(markerPath):
			import datetime
			counterPath=markerPath+'/Counter'
			if system.tag.exists(counterPath):
					counterValue = system.tag.read(counterPath).value 			
			else:
				return 'Counter Error'
				print 'counter error'
				
			newCounterValue = counterValue + 1			
			
			if newCounterValue > 99999:
					newCounterValue = 1
			system.tag.write(counterPath,newCounterValue)		
			
			
			Counter= str(newCounterValue).zfill(5)			
			genPoint= system.tag.read(markerPath+'/GenerationPoint').value	
			PlantCode = 'GSL' #Codigo planta
			FordMotorCompany= 'FoMoCo'
			VendorID= 'HCTTA'
			Shift = 'A'
			now = datetime.date.today().isocalendar()
			yearL, weekL, dayL = now[0]% 100 ,now[1],now[2]
			weekL=str(weekL).zfill(2)
			lotNoutRH = str(genPoint) + str(Shift) + str(dayL) + str(weekL) + str(yearL) +str(Counter) + 'RH'#################pkYoke##############
			lotNoutLH = str(genPoint) + str(Shift) + str(dayL) + str(weekL) + str(yearL) +str(Counter) + 'LH'
			dic= {'LH':lotNoutLH,'RH': lotNoutRH}
			return dic
			
def adjustQty(segment,lotNumber,Seq, QtyIn, QtyOut, Personnel):
			import java.lang
			result = shared.Tracking.getSegmentInfo(segment)
			dicSegment=result['Value']
			try:
				seg = system.mes.createSegment(dicSegment['Name'], dicSegment['Equipment'], False, True)
				#seg = system.mes.getActiveSegment( dicSegment['Equipment'],dicSegment['Name'])		
				for materialPropertyName in dicSegment['Materials']:
					currentMatProperties = dicSegment['Materials'][materialPropertyName]
					if currentMatProperties['Use'] == 'In':
						print str(materialPropertyName) + ' Found'
						seg.setMaterial(materialPropertyName, lotNumber,Seq,QtyIn)
						print str(materialPropertyName) + ' Done'
				for materialPropertyName in dicSegment['Materials']:
						currentMatProperties = dicSegment['Materials'][materialPropertyName]
						if currentMatProperties['Use'] == 'Out' and currentMatProperties['LotSource'] == 'Manual':  # Execute Segment Mat out for Transition
							# seg.setMaterial('Out Material','3666499','Enterprise\Site\Area\Line 1', '0000537000000000001', quantity)
							print str(materialPropertyName) + ' Found'
							seg.setMaterial(materialPropertyName, currentMatProperties['Matref'], currentMatProperties['matEqPath'], lotNumber, QtyOut)
							print str(materialPropertyName) + ' Done'
				seg.setPersonnel("Personnel",Personnel)
				seg.execute()
				return {'Status':True,'Value':dicSegment['Name']}
			except java.lang.Exception, value:
				return {'Status':False,'Value':str(value.getMessage())}

def getFinalPartName(LotN):
	if LotN.find('RH')>=0:
		return 'LX6B-S16123-D'
	elif LotN.find('LH')>=0:#IZQUIERDO
		return 'LX6B-S16D154-D'
	else:
		return 'No Definido'