# coding: utf8
import json;
def CheckSignature(s, sign):
        if(s.find(sign) == 0):
                return(True);
        else:
                return(False);

def FindBlock(s):
        beg = s.find("!!!");
        end = s.find("$$$");
        
        resp = [beg, end];
        #print(resp);
        
        if ( beg == -1 ) or ( end == -1 ):
                return False;
        else:
                return resp;

def Convert(A):
        result = [];
        for i in range(len(A)):
                ##FORMAT OF DICT
                temp = {'id':'', 'message':'', 'next': '', 'choice':[], 'media':''};
                
                ##CHECK ID
                bCheck = CheckSignature(A[i][0],"!!!");
                if bCheck != True:
                        print("Can't find !!!");
                        return;
                
                if len(A[i][0][4:])>20:
                        print("Very big size for id");
                        return;
                
                temp['id'] = A[i][0][4:];
                
                ##CHECK MESSAGE AND ANSWER
                j=1;
                
                bCheck = CheckSignature(A[i][j],"@@@");                
                while bCheck!=True:
                        j += 1;
                        bCheck = CheckSignature(A[i][j],"@@@");

                #WRITE MESSAGE        
                for line in range(j-1):
                        temp['message'] += A[i][line+1] + "\n";

                #WRITE MEDIA
                temp['media'] = A[i][j][4:];
                j = j+1;

                #WRITE NEXT
                temp['next'] = A[i][j][4:];

                #WRITE CHOICE
                if CheckSignature(A[i][len(A[i])-1], "$$$") != True:
                        print("Invalid Footer $$$");
                        return;

                j += 1;                
                while (len(A[i])-1 > j):     
                        temp['choice'].append(A[i][j]);
                        j += 1;

                temp['choice'] = json.dumps(temp['choice']);

                result.append(temp);

        return result;
                        

def ParseFile(name):
    #OPEN FILE
    f = open(name, "r", encoding="utf8");

    s = "";

    for line in f:
        s += line;

    bSig = CheckSignature(s, "#File_For_VKQuestBot\n");
	
    if bSig:
        A=[];
        s = s[len("#File_For_VKQuestBot\n"):];#DELETE SIGNATURE

        tryBlock = FindBlock(s);#A = LIST OF BLOCKS
        while ( tryBlock != False ) :
            A.append(s[tryBlock[0]:tryBlock[1]+3]);
            s = s[tryBlock[1]+4:]
            #print(s)
            tryBlock = FindBlock(s);

        for i in range(len(A)):#A = LIST OF LINES IN BLOCKS
                A[i] = A[i].split('\n');

        return Convert(A);
    else:
        print("File not Valid!!");
