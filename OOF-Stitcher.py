import pickle

class out:
    def __init__(self, name):
        self.name=name

if __name__ == '__main__':
    index=1
    data=b''
    while True:
        try:
            f=open('S'+str(index)+'.OOF', 'rb')
            data+=f.read()
            f.close()
            index+=1
        except:
            break
    try:
        form=open('S0.OOF', 'rb')
        final=pickle.loads(form.read())
        form.close()
        out=open(str(final.name), 'wb')
        out.write(pickle.loads(data))
        out.close()
    except:
        pass
