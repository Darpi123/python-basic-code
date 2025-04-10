#　字典 dictionary : 可以幫我們儲存很多鍵(key)跟值(value)的配對 

dic = {"蘋果":"apple" , "香蕉":"banana" , "貓":"cat" , "狗":"dog"}  #字典要用大括號，key為中文，value為英文
print(dic["蘋果"]) #用中括號打key，就可以查value

dic = {"0":"apple" , "1":"banana" , "2":"cat" , "3":"dog"}  #字典要用大括號，key為中文，value為英文
print(dic["1"]) #用中括號打key，就可以查value





dic ={"蘋123果":"apple" , "香蕉":"banana" , "貓咪":"cat" }
print(dic["蘋123果"])



#　添加和刪除字典～～
dic3 = {"蘋果":"apple" , "香蕉":"banana" , "貓":"cat" , "狗":"dog"} 

dic3["鳥"] = "Bird"     # 添加字典裡的data
del dic3["蘋果"]    #刪除字典裡的data
print(dic3)