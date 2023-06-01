from tkinter import *

import requests
import json

#---------------API from API ninja website-------------------------------------#

def get_quote():
    pass
    #Write your code here.
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'D2nDhCeB7IidmGyKajhiM7RQTDEishDkFezrAZgc'})
    response.raise_for_status()
    data = response.json()
    print(data)
    print(type(data))
    json_data =json.dumps(data
                          )
    canvas.itemconfig(joke_text,text=json_data)


#-------------------------------UI setup------------------------------------------------#

window = Tk()
window.title("Dhoni Quotes...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
joke_text = canvas.create_text(150, 207, text="Click Mr.Bean for a Joke", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

joke_img = PhotoImage(file="funny_image.png")
joke_button = Button(image=joke_img, highlightthickness=0, command=get_quote)
joke_button.grid(row=1, column=0)



window.mainloop()
