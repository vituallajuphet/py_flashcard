from tkinter import *


class Pages:

  def __init__(self, mydata):
    
    self.alldata = mydata
    self.main_window = Tk(className="Folder {}".format(self.alldata[len(self.alldata)-1]))
    self.main_window.geometry("600x800")
    self.build()

  def build(self):

    btn_frame = Frame(self.main_window, pady=16)
    btn_frame.pack(expand=True, fill=BOTH)

    var = StringVar()
    label = Label(btn_frame, text=self.foldername, relief=FLAT)
    label.config(font=("Courier", 20))
    label.pack(fill=BOTH)

    self.folder_frame = Frame(btn_frame, pady=(60), padx=5, bg="gray") 
    self.folder_frame.pack(expand=True, fill=BOTH)

    # label.pack(side=LEFT)

    btn_add = Button(self.folder_frame, text="+ Add Flashcard", command=self.create_folder, padx=20)
    btn_add.place(x=460, y=-55)

    btn_back = Button(self.folder_frame, text="Back", command=self.back_home, padx=20)
    btn_back.place(x=20, y=-55)


    self.main_window.mainloop()
  
  def build_folder(self):

    col = 1
    row = 1
    btns = []
    i = 0;
    for dta in self.data:
      btns.append(Button(self.folder_frame, text="Folder {}".format(i+1), command= lambda dta = dta: self.view_cards(dta), padx=20))
      btns[i].grid(row=row, column=col, pady=(0, 5), padx=(0, 5))
      btns[i].config(width=10, font=17)
      i += 1
      col += 1
      if col == 5:
        col = 1
        row += 1


  def goto_notes(self):
    return self

  def create_folder (self):
    self.remove_child_frame_elem()
    dta.set_data(self.data.append([]))
    self.data = data.get_data()

    self.build_folder()

    return self
  
  def view_cards(self, dta):
    print(dta)
    return self
	
  def remove_child_frame_elem(self):
    i = 0
    for child in self.folder_frame.winfo_children():
      if i == 0:
        i += 1 
        continue
      child.destroy()
      i += 1



