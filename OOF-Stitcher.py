import pickle

index=0
data=b''

if __name__ == '__main__':
    while True:
        try:
            f=open('S'+str(index)+'.OOF', 'rb')
            data+=f.read()
            f.close()
            index+=1
        except:
            break
    try:
        data=pickle.loads(data)
        out=open(data[0], 'wb')
        out.write(data[1])
        out.close()
    except:
        pass
