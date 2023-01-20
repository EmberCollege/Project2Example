import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Shop")
root.geometry("1280x720")

tabControl = ttk.Notebook(root)

tabCase = ttk.Frame(tabControl)
tabMoBo = ttk.Frame(tabControl)
tabCPU = ttk.Frame(tabControl)
tabGPU = ttk.Frame(tabControl)
tabCooler = ttk.Frame(tabControl)
tabPSU = ttk.Frame(tabControl)
tabRAM = ttk.Frame(tabControl)

tabControl.add(tabCase, text="Case")
tabControl.add(tabMoBo, text="MoBo")
tabControl.add(tabCPU, text="CPU")
tabControl.add(tabGPU, text="GPU")
tabControl.add(tabCooler, text="Cooler")
tabControl.add(tabPSU, text="PSU")
tabControl.add(tabRAM, text="RAM")

tabControl.place(x=10,y=0)

#Dropdown menus

caseLabel = ttk.Label(tabCase, text="Pick a Case")

caseLabel.grid(column=0,row=0,padx=10,pady=10)
caseOption = ["ATX", "mATX", "ITX", "Cardboard Box"]

def caseChanged(*args):
    print(caseSelect.get())

caseSelect = tk.StringVar()
caseSelect.set("ATX")
caseSelect.trace('w', caseChanged)
caseDrop = tk.OptionMenu(tabCase, caseSelect, *caseOption)
caseDrop.grid(column=1,row=0,padx=10,pady=10)

MoBoLabel = ttk.Label(tabMoBo, text="Pick a Motherboard")

MoBoLabel.grid(column=0,row=0,padx=10,pady=10)
MoBoOption = ["Intel", "AMD"]

def MoBoChanged(*args):
    print(MoBoSelect.get())

MoBoSelect = tk.StringVar()
MoBoSelect.set("Intel")
MoBoSelect.trace('w', MoBoChanged)
MoBoDrop = tk.OptionMenu(tabMoBo, MoBoSelect, *MoBoOption)
MoBoDrop.grid(column=1,row=0,padx=10,pady=10)

CPULabel = ttk.Label(tabCase, text="Pick a CPU")
GPULabel = ttk.Label(tabCase, text="Pick a GPU")
CoolerLabel = ttk.Label(tabCase, text="Pick a Cooler")
PSULabel = ttk.Label(tabCase, text="Pick a PSU")
RAMLabel = ttk.Label(tabCase, text="Pick a RAM")

root.mainloop()