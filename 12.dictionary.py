#　字典 dictionary : 可以幫我們儲存很多鍵(key)跟值(value)的配對 

dic = {"蘋果":"apple" , "香蕉":"banana" , "貓":"cat" , "狗":"dog"}  #字典要用大括號，key為中文，value為英文
print(dic["蘋果"]) #用中括號打key，就可以查value

dic = {"0":"apple" , "1":"banana" , "2":"cat" , "3":"dog"}  #字典要用大括號，key為中文，value為英文
print(dic["1"]) #用中括號打key，就可以查value





dic ={"蘋123果":"apple" , "香蕉":"banana" , "貓咪":"cat" }
dic["蘋123果"] = "789789" # 取代原先的字典
print(dic["蘋123果"])



#　添加和刪除字典～～
dic3 = {"蘋果":"apple" , "香蕉":"banana" , "貓":"cat" , "狗":"dog"} 

dic3["鳥"] = "Bird"     # 添加字典裡的data
del dic3["蘋果"]        # 刪除字典裡的data
print(dic3)


print(dic3)





# 嵌入式字典

test = { "apple":{"taste":"good","look":"red"},
        "banana":{"teste":"very good" , "look":"yellow"}
}
print(test)




# A dictionary to handle airport codes
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
}

# Output the contents of the dictionary
print(airport_codes)
print(airport_codes["JFK"]["city"]) # 印出JYK裡面city的對應value，就是 New York



airport_codes["JFK"]["city"] = "Hello"  #變更JYK裡面的city，將New York變成 Hello 

print(airport_codes)