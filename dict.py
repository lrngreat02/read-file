# dict

# 读取档案
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())  #line.strip() 去掉\n
		count += 1

#用dict统计word出现次数	
wc = {} # word_count
for d in data:
	words = d.spilt()  # 不写成d.split(' '), 默认为' ', 且会跳过连续空格'    '
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000:
		print(word, wc[word])
print(len(wc))


#查询
while True:
	word = input('search word: ')
	if word == 'q':
		print('thanks')
		break
	if word in wc:
		print(word, wc[word])
	else:
		print('not found')


# # 留言总长度
# sum_len = 0  # 橙色
# for d in data:
# 	sum_len += len(d)
# print('留言的平均长度为'， sum_len/len(data)

# # 筛选：留言长度小于100的
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有'， len(new), '笔留言长度小于100')
# print(new[0])

# # 筛选：留言中有'good' 
# # good = [d for d in data if 'good' in d]
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print(good[0])

# # 筛选：判断每一条留言中是否有‘bad'，输出是True or False
# bad = ['bad' in d for d in data]
# print(bad)