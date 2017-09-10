
def CheckSignature(s):
	if(s=="#File_For_VKQuestBot\n"):
		print("Verify");
		return(True);

	else:
		print("Not Verify");
		return(False);

def ParseFile(name):
	#OPEN FILE
	f = open(name, "r", encoding="utf8");
	
	#CHECK SIGNATURE
	s = f.readline();
	bSig = CheckSignature(s)
	
	if bSig:
		#BEGIN PARSE		
		for line in f:
			if (line[0:3]=="!!!"):#ID PART
				story = { id : line[4:-1]};
				if(idPoint[-1] == "*"):



	
