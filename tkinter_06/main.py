import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text="label 1") # "Label" = huruf depannya kapital itu adalah class
label2 = tkinter.Label(main_window, text="label 2")

tombol1 = tkinter.Button(main_window, text="tombol1")
tombol2 = tkinter.Button(main_window, text="tombol2")

# method positioning
label1.pack() # "pack" = huruf didepannya kecil artinya itu method
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()

# import tkinter as tk

# root = tk.Tk()

# label1 = tk.Label(text="label 1")
# label2 = tk.Label(text="label 2")

# tombol1 = tk.Button(text="tombol1")
# tombol2 = tk.Button(text="tombol2")

# # method positioning
# label1.pack()
# label2.pack()
# tombol1.pack()
# tombol2.pack()

# root.mainloop()
