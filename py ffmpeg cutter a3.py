


import os

MINSIZE=1024*500

ffpath=''
ffexe = 'ffmpeg.exe'   

source = input('source file =')
oriSize=   os.path.getsize(source)

fname=source[:-4]
appendix=source[-4:]


secleng=0
while secleng<=0:
    secleng = input ('section length (in min, enter for 10min):')
    if secleng=='':
        secleng=600
    else:
        secleng=60*eval(secleng)    

print('sec=',secleng)            

section=0
while section<=0 or section>=1000:
    section = input ('section number:')
    if section =='':
        section=20
    else:
        section=eval(section)

if section<100:
    command= ffpath+ffexe+' -i %s -ss %s -t %s -vcodec copy -acodec copy ' +fname+'_sec%02d'+appendix
else:     #section in [100,999]
    command= ffpath+ffexe+' -i %s -ss %s -t %s -vcodec copy -acodec copy ' +fname+'_sec%03d'+appendix

strikes=3
totalSize=0
for i in range(section):
    ss=i * secleng
    c=command % (source, ss, secleng, i+1)
    print(c)
    os.system(c)
    #x=input('enter to go on')

        
    filename = (fname+'_sec%02d'+appendix)%(i+1)
    filesize = os.path.getsize(filename)
    totalSize+=filesize
    if filesize < MINSIZE:
        os.system('del '+filename)
        strikes-=1
        if strikes==0:            
            break
print("original size:", oriSize)       
print("total secs size:", totalSize, "  ~ %.2f" % (totalSize/oriSize*100)  )       


    
    
    
    


    


