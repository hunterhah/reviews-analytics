data = []
count = 0
with open('reviews.txt', 'r') as file:
	for review in file:
		data.append(review)
		count += len(review)
average = count / len(data)
print('讀取完成，共有', len(data), '筆資料')
print('每則留言的平均長度為', average, '字')