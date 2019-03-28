#encoding=utf8
try:
    f=open('金正恩.jpg','rb')
    print(2333333)
    f1=open('2333333.jpg','ab+')  
    print(66666666) 
    while True: 
        s=''
        s=f.readline()
        #print(s)
        if s=='':
            break    
        s1=f1.write(s)
        #print(s1)

    f.close()
    print(23333)
    f1.close()    
except OSError:
    print('打开失败')   


#ubuntu比较奥两个图片一样的方法就不要我说了吧，图片随意
