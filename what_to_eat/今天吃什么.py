import random
import pickle

foodfile = 'food.data'
f = open(foodfile,'rb')
list1 = []
list1 = pickle.load(f)
#list1 = ['米线', '香锅','排骨汤','火锅','烤鱼']
'''f = open(foodfile,'wb')
pickle.dump(list1,f)
f.close()'''
i = 6
while i != 0:
	i = int(input ('\n请输入要执行的操作：0.退出 1.随机点餐 2.查看 3.添加 4.删除 \n'))
	while i == 1:
		#确保两个结果不一样
		slice = random.sample(list1,2)
		print ('中午吃：',slice[0])
		print ('晚上吃：',slice[1])
		#循环
		i = int(input('0.就吃这个！1.再选一次 2.查看 3.添加 4.删除\n'))
	if i == 2:
		k = 0
		for food in list1:
			print (food ,end = ' ')
			k = k + 1
	if i == 3:
		food = str(input('请添加食物名称(输入“返回”返回上一级）：'))
		if food == '返回':
			i == 6
		else:
			list1.append(food)
			f = open(foodfile,'wb')
			pickle.dump(list1,f)
			f.close()
	if i == 4:
		print('现在的食物有：')
		k = 0
		for food in list1:
			print(k ,'.',food, end = '')
			k = k + 1
		confirm = str(input('\n确认要删除食物？\nY.是 N.否\n'))
		if confirm == 'Y':
			number = int(input('\n请输入要删除食物的序号：'))
			del list1[number]
			k = 0
			print('现在的食物有：')
			for food in list1:
				print(k ,'.',food, end = '')
				k = k + 1
			f = open(foodfile,'wb')
			pickle.dump(list1,f)
			f.close()
		else:
			i == 6

		
