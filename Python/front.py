import tkinter as tk

root = tk.Tk()
root.title("Mon Application ")

label = tk.Label(root, text="Mon coffre-fort")
label.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Nouveau Mot de passe")
label.pack(side="left", padx=5) 

text_input = tk.Text(frame, height=2, width=30)
text_input.pack(side="left", padx=5) 

label = tk.Label(frame, text="Saisir le même mot de passe")
label.pack(side="left", padx=5) 

text_input = tk.Text(frame, height=2, width=30)
text_input.pack(side="left", padx=5) 




entry = tk.Entry(root, show="*")
entry.pack()

def access_my_safe():
    valeur = entry.get()  
    if valeur == "1234":  
        print("Coffre-fort ouvert")
    else:
        print("Mot de passe incorrect")

button = tk.Button(root, text="Accedez à mon coffre-fort", command=access_my_safe)
button.pack()
print(access_my_safe)
root.mainloop()


