def sub_script_func():
	print('I am sub_script_func from TestSubPackage')


if __name__ == '__main__':
	print('sub_script_func is being ran directly')
else:
	print('sub_script.py is being imported to another module')