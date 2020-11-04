#!usr/bin/env python3
#coding=utf-8
#HaoCold
#2020-11-04 09:47:51

"""
把 OC 的头文件里面的方法，转成字符串。
然后通过字符串转 SEL
"""

def file():

    # 指定路径
    path = ''
    f = open(path, 'r')
    for line in f.readlines():
        if line.startswith('-') or line.startswith('+'):
            list = line.split(':(')
            
            # - (id)propertyList;
            if len(list) == 1:
                li = list[0]
                li = li.split(')')[1]
                li = li.split(';')[0]
                li = '@"' + li + '",'
                print(li)
            # - (unichar)characterAtIndex:(NSUInteger)index;
            elif len(list) == 2:
                li = list[0]
                li = '@"' + li.split(')')[1] + ':",'
                print(li)
                
            # - (void)getCharacters:(unichar *)buffer range:(NSRange)range;
            elif len(list) > 2:
                li = list[0]
                li = '@"' + li.split(')')[1] + ':'
                
                for i in range(1, len(list)):
                    sub_list = list[i].split(' ')
                    if len(sub_list) > 1:
                        last = sub_list[len(sub_list)-1]
                        if not last.endswith('\n'):
                            li = li + last + ':'
                li = li + '",'
                print(li)

    f.close()
    
if __name__ == "__main__":
    file()
