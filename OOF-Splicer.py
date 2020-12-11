import pickle

mb=8192000

class out:
    def __init__(self, name):
        self.name=name

def make(start, end, i, data):
    print('Generating OOF '+str(i+1)+'...')
    if end > len(data):
        end=len(data)
    f=open('S'+str(i+1)+'.OOF','wb')
    for i in range(start, end):
        f.write(bytes([data[i]]))
    f.close()
if __name__ == '__main__':
    valid=False
    while not valid:
        name=str(input('FILE NAME:'))
        try:
            index=out(name)
            file=open(name, 'rb')
            data=pickle.dumps(file.read())
            file.close()
            form=open('S0.OOF', 'wb')
            form.write(pickle.dumps(index))
            form.close()
            num=int(len(data)/mb)+1
            valid=True
            print('Generating '+str(num+1)+ ' OOF\'s...')
            print('Generating OOF 0...')
            for i in range(0,num):
                make(i*mb, i*mb+mb, i, data)
        except:
            print('INVALID FILE NAME!\n')
