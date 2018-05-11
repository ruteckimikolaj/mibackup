"""Lightweight cross-platform graphic interface for folder compare program."""

import getpass
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from mibackupapp import compare_copy
#from .mibackupapp import cc_message


class FolderComparisonGUI(tk.Frame):
    """The graphic interface for the application."""

    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.root = root

        # tkinter app variables -- .get() returns False until .set() otherwise
        self.dir1 = tk.StringVar()
        self.dir2 = tk.StringVar()
        self.folder_output = tk.StringVar()
        self.filename = tk.StringVar()
        self.output_as_txt = tk.BooleanVar()
        self.output_as_txt.set(1)
        self.output_as_csv = tk.BooleanVar()
        self.output_as_csv.set(1)

        self.set_design_options()
        self.create_widgets()
        self.set_action_options()

    def set_design_options(self):
        """Configure widget design options before placing them in GUI."""

        self.root.title("Ignalski Custom Backup Tool")
        self.root.minsize(300, 200)
        self.button_options = {
            'fill': tk.constants.BOTH,
            'padx': 5,
            'pady': 5,
        }

    def create_widgets(self):
        """Create widgets on GUI launch."""

        tk.Label(
            self, text='Folder Backup Tool', font=16,
            ).pack()

        tk.Button(
            self, text='Select Source Folder',
            command=lambda: self.set_directory(self.dir1),
            ).pack(**self.button_options)

        tk.Label(
            self, textvariable=self.dir1, fg="blue",
            ).pack()

        tk.Button(
            self, text='Select Destination Folder',
            command=lambda: self.set_directory(self.dir2),
            ).pack(**self.button_options)

        tk.Label(
            self, textvariable=self.dir2, fg="blue",
            ).pack()
        tk.Button(
            self, text='Run', command=self.validate_and_run).pack(**self.button_options)


    def set_action_options(self):
        """Configure widget action options after placing them in GUI."""

        self.directory_options = {
            'initialdir': r'C:\Users\{}\Desktop'.format(getpass.getuser()),
            'mustexist': False,
            'parent': self.root,
            'title': 'Choose a directory',
        }

        self.start_program = {
            'title': 'Start a program'
        }

    def set_directory(self, variable):
        """Return a selected directory name.

        ARGS:
            variable (tk.Variable): The tkinter variable to save selection as.
        """

        selection = filedialog.askdirectory(**self.directory_options)
        variable.set(selection)

    def validate_and_run(self):
        """Run the folder comparison program with user selected data."""

        # Validate user inputs savid in tkinter variables
        folder1_is_valid = os.path.exists(self.dir1.get())
        folder2_is_valid = os.path.exists(self.dir2.get())
        folder_output_is_valid = os.path.exists(self.folder_output.get())
        output_name_valid = self.filename.get()

        # Show error if validation failed
        if not folder1_is_valid:
            messagebox.showerror("Error", "Must select Folder 1")
        elif not folder2_is_valid:
            messagebox.showerror("Error", "Must select Folder 2")
        else:
            #if cc_message != True
                

            # Run the folder compare program
            compare_copy(self.dir1.get(), self.dir2.get())


if __name__ == '__main__':
    # Start the app in dev mode
    ROOT = tk.Tk()
    FolderComparisonGUI(ROOT).pack()
    ROOT.mainloop()
