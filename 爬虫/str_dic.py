def str_dic(stra):
    dic = {}
    tem_list = stra.split('\n')
    
    for i in tem_list: 
        if i:
            start_index = i.find(':')
            key = i[:start_index]
            value = i[start_index+1:]
            dic[key] = value
#     print dic
    return dic
    
    

s = """
q: 
viewFlag: A
sortType: default
searchStyle: 
searchRegion: city:
searchFansNum: 
currentPage: 1
pageSize: 100
"""
str_dic(s)
# print a