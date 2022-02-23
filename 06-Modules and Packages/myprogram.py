from mymodule import myfunc
from TestMainPackage import main_script
from TestMainPackage.TestSubPackage import sub_script


def myprogram_func():
	print ('myprogram_func in myprogram.py')

print('top tier')


#myfunc()
#main_script.main_script_func()
sub_script.sub_script_func()

if __name__ == '__main__':
	print('myprogram_func is being ran directly')
else:
	print('myprogram_func is being imported into another script')