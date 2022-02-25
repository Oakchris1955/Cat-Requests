#import tkinter
import tkinter as tk

#import other libs
import requests, keyboard

# pip install pillow
from PIL import Image, ImageTk

#set the window
window = tk.Tk()

#set the window name
window.title('Cat Requests - Made by Oakchris1955')

#set the window icon
window.iconphoto(False, tk.PhotoImage(file='icon.png'))

#render the image
def render(status):
	load = Image.open(requests.post(f'http://http.cat/{status}', stream=True).raw)
	render = ImageTk.PhotoImage(load)
	img['image'] = render
	img.image = render
	img.pack(side='top', fill='both', expand='yes')
	print('Succesfully rendered the image')

def get_status():
	try:
		status = requests.get(entry.get(), timeout=5).status_code
	except Exception as e:
		debug_output.configure(state=tk.NORMAL)
		debug_output.insert(tk.END, str(e)+'\n')
		debug_output.configure(state=tk.DISABLED)
		print('An exception rose')
	else:
		render(status)

#set the variables
img = tk.Label(text='Please submit a request')
greeting = tk.Label(text="Please enter the address you wanna ping here")
entry = tk.Entry(width=50)
request_button = tk.Button(text='Send request', command=get_status)
debug_response = tk.Label(text='Debug output:')
debug_output = tk.Text(width=100, height=15, state=tk.DISABLED)

#pack the variables
img.pack()
greeting.pack()
entry.pack()
request_button.pack()
debug_response.pack()
debug_output.pack()

#render the image when the "Enter" button is pressed
keyboard.on_press_key("Enter", lambda _:get_status())

#show the window
window.mainloop()
