//First question

text=input("Как зовут создателя этой викторины? (4 буквы, англ)")
points=0
if text=="alex":
	points=1
	print("Правильно! На вашем счету 1 балл.")
elif text=="Alex":
	points=1
	print("Правильно! На вашем счету 1 балл.")	
else:
	points=0
	print("Неправильно. На вашем счету 0 баллов. Может удастся ответить на другие вопросы?")
	
//Second question

text=input("В каком году я родился?")
if text=="1989":
	if points==1:
		points=2
		print("Правильно! На вашем счету 2 балла.")
	elif points==0:
		points=1
		print("Правильно! На вашем счету 1 балл.")
elif points==1:
	print("Неправильно. На вашем счету 1 балл. Может удастся ответить на другие вопросы?")
elif points==0:
	print("Неправильно. На вашем счету 0 баллов. Может удастся ответить на другие вопросы?")

//Third question 

text=input("Сколько мне лет?")
if text=="30":
	if points==2:
		points=3
		print("Правильно! На вашем счету 3 балла.")
	elif points==0:
		points=1
		print("Правильно. Вот Ваш первый балл!")
	elif points==1:
		print("Правильно! На вашем счету 2 балла!")
elif points==0:
	print("Неправильно. На вашем счету 0 баллов. Может удастся ответить на другие вопросы?")
elif points==1:
	print("Неправильно. На вашем счету 1 балл. Может удастся ответить на другие вопросы?")
elif points==2:
	print("Неправильно. На вашем счету 2 балла.Может удастся ответить на другие вопросы?")
print("Продолжайте дальше, так держать!")

//Fourth question 

text=input("Что я люблю есть?")
if text=="rolton":
	points=4
	print("Правильно! На вашем счету 4 балла.")
elif text=="Rolton":
	points=4
	print("Правильно! На вашем счету 4 балла.")
	if points==2:
		points=3
		print("Правильно! На вашем счету 3 балла.")
	elif points==0:
		points=1
		print("Правильно. Вот Ваш первый балл!")
	elif points==1:
		points=2
		print("Правильно! На вашем счету 2 балла!")		
	elif points==2:
		points=3
		print("Правильно! На вашем счету 3 балла!")
elif points==0:
	print("Неправильно. На вашем счету 0 баллов. Может удастся ответить на другие вопросы?")
elif points==1:
	print("Неправильно. На вашем счету 1 балл. Может удастся ответить на другие вопросы?")
elif points==2:
	print("Неправильно. На вашем счету 2 балла.Может удастся ответить на другие вопросы?")
elif points==3:
	print("Неправильно. На вашем счету 3 балла.Может удастся ответить на другие вопросы?")
