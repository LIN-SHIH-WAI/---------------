#__author:"LIN SHIH-WAI"
#date:  2017/10/12
# --------------------函数定义:清空文档-------------------------
def clean(目标文件名):
    while True:
        判断是否清空=input('是否要清空文档%s    y/n:'%目标文件名)
        if 判断是否清空=='y':
            open('%s'%目标文件名,'w+',encoding='utf-8')
            break
        if 判断是否清空=='n':
            break
# ---------------------------函数定义:筛选汉字------------------------
def check_chinese(ch):
    if 0x4e00 <= ord(ch) < 0x9fa6:
        return ch
    return ''
#---------------------提取所有的文字,并且形成字典---------------------
读取人民日报=open('读取文档.txt','r+',encoding='utf-8')
第一次提取=读取人民日报.read()
clean('汉字收集.txt')
汉字收集=open('汉字收集.txt','a+',encoding='utf-8')
for i in 第一次提取:
    汉字=check_chinese(i)
    汉字收集.write(汉字)
汉字收集.close()
汉字收集=open('汉字收集.txt','r',encoding='utf-8')
读取所有的字符串=汉字收集.read()
读取所有的字符串=读取所有的字符串.replace('\n','')
读取所有的字符串=读取所有的字符串.strip()
hzf={}
clean('所有字体提取.txt')
所有字体提取=open('所有字体提取.txt','a+',encoding='utf-8')
for i in 读取所有的字符串:
    hzf.setdefault(i)
    所有字体提取.write(i)
#---------------------形成每个子字典------------------------------
for i in hzf.keys():
    hzf[i]={}
# ----------------------给每个子字典添加新的值--------------------
for i in range(0,len(读取所有的字符串)-1):
    a=读取所有的字符串[i]
    b=读取所有的字符串[i+1]
    hzf[a].setdefault(b)
    hzf[a][b]=0               #给每一个赋值 否则不能进行+1 的操作
for i in range(0,len(读取所有的字符串)-1):
    a=读取所有的字符串[i]
    b=读取所有的字符串[i+1]
    if b in hzf[a]:
        hzf[a][b]+=1
clean('记录')
记录=open('记录','a+',encoding='utf-8')
记录.write(str(hzf))

#--------------------把每个字典列表转换成List------------------------------
hzFlist={}#深度拷贝不能用等号
clean('list转换写入日志.txt')
List写入=open('list转换写入日志.txt','a+',encoding='utf-8')
for i in hzf:
    hzFlist.setdefault(i)
    hzFlist[i]=[]
for i in hzf:
    for v in hzf[i].items():
        hzFlist[i].append(v)

List写入.write(str(hzFlist))
#---------------------对hzFlist进行排序---------------------------------------
for i in hzFlist:
    hzFlist[i].sort(key=lambda x:x[1],reverse=True)
clean('排序记录.txt')
排序写入=open('排序记录.txt','a+',encoding='utf-8')
排序写入.write(str(hzFlist))
#---------------------对跟随字数加工------------------------------------
hzFTab={}
clean('字数统计记录.txt')
f=open('字数统计记录.txt','a+',encoding='utf-8')
for i in hzFlist:
    sum=0
    hzFTab.setdefault(i)
    for v in hzFlist[i]:
        sum=sum+v[1]
    hzFTab[i]=sum
f.write(str(hzFTab))
#--------------------对hzFlist再加工----------------------------
clean('hzTab.txt')
f=open('hzTab.txt','a+',encoding='utf-8')
hzFstr={}
for i in hzFlist:
    hzFstr.setdefault(i)
    文字列表 = []
    计数 = 1
    for v in hzFlist[i]:
        文字=v[0]

        if 计数<=20:
            文字列表.append(文字)
        计数+=1
    文字=''.join(文字列表)
    hzFstr[i]=文字
    f.write('%s %s\n'%(i,str(hzFstr[i])))

def 打印(x):
    for i,v in enumerate(x):
        print("%s.%s"%(i,v),end=' ')


while True:
    打字=input('\n请输入你的汉字:')
    if 打字 in hzFstr:
        打印(hzFstr[打字])
    if 打印 == '退出':
        break











