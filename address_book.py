import pickle
#储存数据的文件
addressfile = 'address_book.data'
#创建字典
address_book = {}
#读取数据
f = open(addressfile,'rb')
address_book = pickle.load(f)
i = 1

while i != 6:
	print("请选择你要进行的操作：1.浏览 2.添加 3.删除 4.搜索 5.保存 6.退出")
	i = int(input())
	if i == 1:
		if len(address_book) > 0:
			for key in address_book:
				print(key,':', address_book[key])
		else:
			print("地址簿暂无信息")
		continue
	if i == 2:
		key = input("请输入要添加的名字：")
		address = input("请输入地址信息：")
		phone = input("请输入电话号码：")
		email = input("请输入邮件地址：")
		#将信息储存为一个list
		value = [address, phone, email]
		address_book[key] = value
		for key in address_book:
			print(key, ':', address_book[key])
		continue
	if i == 3:
		name = input("请输入要删除的联系人：")
		for key in address_book:
			if key == name:
				del address_book[key]
				break	
		continue
	if i == 4:
		name = input ("请输入要搜索的联系人：")
		for key in address_book:
			if key == name:
				print(key,':',address_book[key])
				break
	if i == 5:
		f = open(addressfile,'wb')
		pickle.dump(address_book,f)
		f.close()
		print("已保存。")


