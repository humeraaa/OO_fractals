##Open README.md
#Press Ctrl + Shift + V (or right-click → "Open Preview").
#You can also split the editor: Ctrl + K V to see side-by-side Markdown + Preview.

#Please open the terminal manually inside VS Code by:
#Going to Menu → Terminal → New Terminal or using shortcut: `Ctrl + `` (backtick)
# Activate virtual environment by typing: venv\Scripts\activate

#Just make sure your VS Code is using the correct interpreter:
#Press Ctrl+Shift+P → "Python: Select Interpreter"
#Choose the one that looks like:.\venv\Scripts\python.exe

# This make ease running the script via the "Run" button or python -u command in VS Code's 
# internal runner, not from an activated terminal session or cmd.

#Run power shell command to set execution policy if you encounter an error:
#PS D:\week03_OOPs_Point_Pen\OO_fractals> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
#Activate venv: PS D:\week03_OOPs_Point_Pen\OO_fractals> .\venv\Scripts\Activate.ps1

# This confirms where python in VSCode points to:
#python -c "import sys; print(sys.executable)"
# It must say D:\week03_OOPs_Point_Pen\OO_fractals\venv\Scripts\python.exe

# To check and verify the installed packages in the virtual environment:
# PS D:\week03_OOPs_Point_Pen\OO_fractals> dir .\venv\Scripts\pyreverse*



#Generate UML diagrams using Pyreverse
# Make sure you have Graphviz installed and added to your PATH.
# (venv) PS D:\week03_OOPs_Point_Pen\OO_fractals> cd D:\week03_OOPs_Point_Pen\OO_fractals\python
# (venv) PS D:\week03_OOPs_Point_Pen\OO_fractals\python> ..\venv\Scripts\pyreverse.exe -o png -p OO_fractals -my geometry drawing app
# Format png is not supported natively. Pyreverse will try to generate it using Graphviz...
# Analysed 6 modules with a total of 4 imports


from app.app import App

if __name__ == "__main__":
    app = App()
    app.run()