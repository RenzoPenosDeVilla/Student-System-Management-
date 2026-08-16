from tkinter import *
from tkinter import messagebox

# STACK LIST
papers = []

# FUNCTIONS
def submit_paper():
    student = student_entry.get()
    title = title_entry.get()

    if student == "" or title == "":
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    paper = f"{student} - {title}"
    papers.append(paper)

    messagebox.showinfo("Success", "Paper submitted successfully!")

    student_entry.delete(0, END)
    title_entry.delete(0, END)

    view_papers()


def view_papers():
    display.delete(0, END)

    if len(papers) == 0:
        display.insert(END, "No submitted papers.")
    else:
        for paper in reversed(papers):
            display.insert(END, paper)


def remove_paper():
    if len(papers) == 0:
        messagebox.showwarning("Warning", "No papers to remove.")
    else:
        removed = papers.pop()
        messagebox.showinfo("Removed", f"{removed} removed successfully.")
        view_papers()


def update_paper():
    try:
        selected = display.curselection()[0]

        # reverse index adjustment
        actual_index = len(papers) - 1 - selected

        new_student = student_entry.get()
        new_title = title_entry.get()

        if new_student == "" or new_title == "":
            messagebox.showwarning("Warning", "Please enter new details.")
            return

        papers[actual_index] = f"{new_student} - {new_title}"

        messagebox.showinfo("Updated", "Paper updated successfully.")

        student_entry.delete(0, END)
        title_entry.delete(0, END)

        view_papers()

    except:
        messagebox.showwarning("Warning", "Please select a paper.")


def search_paper():
    keyword = student_entry.get().lower()

    display.delete(0, END)

    found = False

    for paper in reversed(papers):
        if keyword in paper.lower():
            display.insert(END, paper)
            found = True

    if not found:
        display.insert(END, "Paper not found.")


# GUI WINDOW
root = Tk()
root.title("School Paper Submission System")
root.geometry("500x500")
root.config(bg="#dbeafe")

# TITLE
title_label = Label(
    root,
    text="School Paper Submission System",
    font=("Arial", 12, "bold"),
    bg="#dbeafe"
)
title_label.pack(pady=10)

# STUDENT NAME
Label(root, text="Student Name:", bg="#dbeafe", font=("Arial", 11)).pack()

student_entry = Entry(root, width=40)
student_entry.pack(pady=5)

# PAPER TITLE
Label(root, text="Paper Title:", bg="#dbeafe", font=("Arial", 11)).pack()

title_entry = Entry(root, width=40)
title_entry.pack(pady=5)

# BUTTON FRAME
button_frame = Frame(root, bg="#dbeafe")
button_frame.pack(pady=10)

Button(
    button_frame,
    text="Submit Paper",
    width=15,
    command=submit_paper
).grid(row=0, column=0, padx=5, pady=5)

Button(
    button_frame,
    text="View Papers",
    width=15,
    command=view_papers
).grid(row=0, column=1, padx=5, pady=5)

Button(
    button_frame,
    text="Update Paper",
    width=15,
    command=update_paper
).grid(row=1, column=0, padx=5, pady=5)

Button(
    button_frame,
    text="Remove Latest",
    width=15,
    command=remove_paper
).grid(row=1, column=1, padx=5, pady=5)

Button(
    button_frame,
    text="Search Paper",
    width=15,
    command=search_paper
).grid(row=2, column=0, padx=5, pady=5)

Button(
    button_frame,
    text="Exit",
    width=15,
    command=root.quit
).grid(row=2, column=1, padx=5, pady=5)

# DISPLAY LISTBOX
display = Listbox(root, width=55, height=12, font=("Arial", 10))
display.pack(pady=10)

root.mainloop()
  
