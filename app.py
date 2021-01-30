from tkinter import *
from string import ascii_letters, digits, punctuation

all_chars = list(" " + ascii_letters + punctuation)

screen_width = "400"
screen_height = "150"

def crypt_words(li):
	try:
		result = []
		for x in li:
			result.append(str(all_chars.index(x)))

		return result
	except:
		pass

def decrypt_words(li):
	try:
		result = []
		for x in li:
			result.append(str(all_chars[x]))
		return result
	except:
		pass

def show_crypt():
	try:
		from_entry = crypt_entry.get()
		result = crypt_words(from_entry)
		decrypt_entry.insert(0, ",".join(result))
		crypt_entry.delete(0, END)
	except:
		pass		

def show_decrypt():
	try:
		from_entry = decrypt_entry.get()
		new = from_entry.split(",")
		newl = [int(x) for x in new]
		result = decrypt_words(newl)
		crypt_entry.insert(0, "".join(result))
		decrypt_entry.delete(0, END)
	except:
		pass

root = Tk()
root.title("Secretwords")
root.resizable(False, False)
root.geometry(f'{screen_width}x{screen_height}')

crypt_entry = Entry(root)
decrypt_entry = Entry(root)
crypt_btn = Button(root, text="Encrypt", command=show_crypt)
decrypt_btn = Button(root, text="Decrypt", command=show_decrypt)
header_2 = Label(root, text="Encrypted")
header_1 = Label(root, text="Decrypted")

#place things
crypt_entry.place(x=110, y=50, height=25)
decrypt_entry.place(x=110,y=80, height=25)
crypt_btn.place(x=300, y=50, height=25, width=80)
decrypt_btn.place(x=300, y=80, height=25, width=80)
header_1.place(x=20, y=50)
header_2.place(x=20, y=80)

root.mainloop()