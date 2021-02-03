from tkinter import *
from classes.my_data import MyData
from tkinter import messagebox

class ViewCard:

  def __init__(self, card_index, folderindex,  alldata):
    
    self.card_index = card_index
    self.folderindex = folderindex
    self.alldata = alldata
    self.num = card_index + 1
    self.main_window = Tk(className="Flashcard {}".format(self.num))
    self.main_window.geometry("600x850")
    self.build()

  def build(self):
    print("running...")
    btn_frame = Frame(self.main_window, pady=16)
    btn_frame.pack(expand=True, fill=BOTH)

    var = StringVar()
    label = Label(btn_frame, text="Flashcard {}".format(self.num), relief=FLAT)
    label.config(font=("Courier", 20))
    label.pack(fill=BOTH)

    self.folder_frame = Frame(btn_frame, pady=(60), padx=5, bg="gray") 
    self.folder_frame.pack(expand=True, fill=BOTH)

    # label.pack(side=LEFT)

    btn_back = Button(self.folder_frame, text="Back", command=self.back_folder, padx=20)
    btn_back.place(x=20, y=-55)

    self.text_desc = Text(self.folder_frame, width=40, height=25)
    self.text_desc.config(font=("Courier", 16))
    self.text_desc.place(x=20, y=30)

    txtdata = self.alldata[self.folderindex][self.card_index]

    self.set_text(txtdata)

    btn_save = Button(self.folder_frame, text="Save / Update", command=self.save_card, padx=20)
    btn_save.place(x=20, y=630)
    btn_save.config(font=(12, "bold"))

    # self.build_folder()
    self.main_window.mainloop()
  
  def goto_notes(self):
    return self

  def set_text(self, txt):
    self.text_desc.delete(1.0,"end")
    self.text_desc.insert(1.0, txt)

  def save_card(self):
    from classes.my_data import MyData
    txt = self.text_desc.get("1.0","end-1c")
    if txt == "":
      messagebox.showerror("Error", "Fields must not be empty!")
      return
    
    self.alldata[self.folderindex][self.card_index] = txt
    mydata = MyData()
    mydata.set_data(self.alldata)
    messagebox.showinfo("Success", "Saved Successfully!")
  
  def view_cards(self, dta):
    print(dta)
    return self
	
  def remove_child_frame_elem(self):
    i = 0
    for child in self.folder_frame.winfo_children():
      if i == 0 or i == 1:
        i += 1 
        continue
      child.destroy()
      i += 1

  def back_folder(self):
    from classes.pages import Pages
    self.main_window.destroy()
    page = Pages(self.folderindex, self.alldata)
    
    return self



