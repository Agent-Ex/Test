def main(inp:str):

	inp = inp.split()
	
	try:

		if len(inp)==3 and inp[1] in '+-*/' and (11>int(inp[0])>0 and 11>int(inp[0])>0):

			match inp[1]:
				case '+':
					return int(inp[0]) + int(inp[-1])
				case '-':
					return int(inp[0]) - int(inp[-1])
				case '*':
					return int(inp[0]) * int(inp[-1])
				case '/':
					return int(inp[0]) // int(inp[-1])
		else:
			return Error

	except ZeroDivisionError:
		return'Деление на 0 недопустимо'

	except Exception:
		if len(inp)> 3 or len(inp)< 3:
			return 'Неправильный формат. Необходимо два операнда и один оператор(+, -, *, /)'
		elif inp[1] not in '+-*/' and len(inp)==3:
			return 'Данная cтрока не является математической операцией'
		else:
			return 'Допущена ошибка в запросе'

a = str(input())
print(main(a))

