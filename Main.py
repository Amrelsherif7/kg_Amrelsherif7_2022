D={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
def conver(the_list):
    List = the_list
    L = len(List)
    new = []
    for i in range(L):
        empty = ''
        x = List.pop(0)
        str_conv = str(x)
        for y in str_conv:
            sentence = D[int(y)]
            empty += sentence
        new.append(empty)
        
    final=','.join(new)
    Output=(str(final))
    return(Output)
    
