import pickle

mb=8192000
data=[]

def make(start, end, i):
    global data
    print('Generating OOF '+str(i)+'...')
    if end > len(data):
        end=len(data)
    f=open('S'+str(i)+'.OOF','wb')
    for i in range(start, end):
        f.write(bytes([data[i]]))
    f.close()

if __name__ == '__main__':
    valid=False
    while not valid:
        name=str(input('FILE NAME:'))
        try:
            data.append(name)
            file=open(name, 'rb')
            data.append(file.read())
            file.close()
            num=int(len(data[1])/mb)+1
            data=pickle.dumps(data)
            valid=True
            print('Generating '+str(num)+ ' OOF\'s...')
            for i in range(0,num):
                make(i*mb, i*mb+mb, i)
        except:
            print('INVALID FILE NAME!\n')
