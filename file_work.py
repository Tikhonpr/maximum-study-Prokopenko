
my_file = open("text.txt", "a")

my_file.write('Привет, Mir!')

my_file.close()

my_file = open("text.txt", "r")

string = my_file.read()
print(string)
my_file.close()