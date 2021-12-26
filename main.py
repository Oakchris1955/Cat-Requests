import tkinter as tk
import requests

# pip install pillow
from PIL import Image, ImageTk

#set the window
window = tk.Tk()

#render the image
def render(status):
	load = Image.open(requests.post(f'http://http.cat/{status}', stream=True).raw)
	render = ImageTk.PhotoImage(load)
	img['image'] = render
	img.image = render
	img.pack(side='top', fill='both', expand='yes')
	print('Rendered!!!')

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
debug_output = tk.Text(width=100, height=20, state=tk.DISABLED)

#pack the variables
img.pack()
greeting.pack()
entry.pack()
request_button.pack()
debug_response.pack()
debug_output.pack()

#show the window
window.mainloop()
