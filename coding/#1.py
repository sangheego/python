def solution(babbling):
    answer=0
    ongal=['aya','ye','woo','ma']
    count=0
    for i in babbling:
        for j in ongal:
            if j in i:
                i=i.replace(j," ")
                print(i)
        i=i.replace(" ","")
        if len(i)==0:
            count+=1
        print(i)
    return count