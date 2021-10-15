pont = "!@#$%^&*()_-+<>?:.,;"
with open('livro.txt', 'r') as f1:
	f=f1.read()
	print(f)
	for c in f:
    		if c in pont:
        		f = f.replace(c, "")

with open('livro2.txt', 'w') as f1:
	write_data = f1.write(f)
	
	
