from wakeonlan import send_magic_packet
from tkinter import *
import systems

systems = systems.return_systems()

root = Tk()
root.title("Wake On Lan")
title_row = Label(root, width=40, text="Wake On Lan Tool")
title_row.grid(row=0, column=0, columnspan=2)

console = Label(root, width=40, text='Select a system to wake')
console.grid(row=2, column=1)


def wake_up(system):
    send_magic_packet(system['mac_address'])
    display_console = Label(root, width=40, text=f"Wakeing up {system['name']} - {system['mac_address']}")
    display_console.grid(row=2, column=1, rowspan=2)


for system in systems:
    button = Button(root, text=system['name'], padx=60, pady=20, border=10, command=lambda: wake_up(system))
    button.grid(row=systems.index(system) + 2, column=0)

root.mainloop()
