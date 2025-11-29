from tkinter import *

#function to calculate points

def calculate_points():
    try:
        books = int(entry_books.get())
        if books<0:
            points = "invalid input"
        elif books == 0:
            points = 0
        elif books == 2:
            points = 5
        elif books == 4:
            points = 15
        elif books == 6:
            points = 30
        elif books >= 8:
            points = 60
        else:
            points = 0

        #store the result
        global last_result
        last_result = f"points awarded: {points}"
        result_var.set(f"points calculated! Click 'Show Result' to view.")
    except ValueError:
        result_var.set("please enter a valid number")

# function to display stored result
def show_result():
    try:
        result_var.set(last_result)
    except NameError:
        result_var.set("please calculate points first!")



#GUI setup
root = Tk()
root.title("Serendipity Booksellers")
root.geometry("400x200")
root.resizable(0,0)

#input widget
label_instruction= Label(root,text="Enter number of books purchased this month:")
label_instruction.pack(pady=10)
entry_books = Entry(root,width=20)
entry_books.pack()

#output widget
result_var = StringVar()
label_result = Label(root,textvariable=result_var, fg="blue", font=("arial",12))
label_result.pack(pady=20)

#buttons
button_calculate = Button(root, text="compute points", command = calculate_points, bg="light green")
button_calculate.pack(pady=5)
button_show = Button(root, text="show result", command= show_result, bg="light yellow")
button_show.pack(pady=5)

root.mainloop()

