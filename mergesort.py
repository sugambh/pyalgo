def mergesort(l):
    if(len(l)<=1):
        return l
    else:
        mid=len(l)/2
        a=mergesort(l[:mid])
        b=mergesort(l[mid:])
        return merge(a,b)

def merge(a,b):
    result=[]
    i=0
    j=0
    while(i<len(a) or j<len(b)):
        if(i<len(a) and j<len(b)):   
            if(a[i]<=b[j]):
                result.append(a[i])
                i=i+1
            else:
                result.append(b[j])
                j=j+1
        elif(i==len(a)):
            result=result+b[j:]
            break
        else:
            result=result+a[i:]
            break
    print a,"->", b," ->",result
    return result

inputlist=raw_input("enter the number to be sorted\n")
inp=[ int(x)  for x in inputlist.split(" ")]
out=mergesort(inp)
