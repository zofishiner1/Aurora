# ONLY WINDOWS
# Aurora

### The program only supports Russian language

**Installing**
To install all dependencies you need to open the console, write "python -m venv venv" (WIndows).
After creating the virtual environment, you need to activate it with the command “venv\Scripts\activate” and then enter “pip install -r requirements.txt”

Then go to the data/LocWIKI/ directory and follow the instructions (Creating a single file from a multi-volume RAR archive) for unpacking a multi-volume .rar archive to unpack the file "ruwiki-latest-pages-articles-multistream.xml", and then after completing the instructions in the data/LocWIKI/ directory, go to the data/configs directory /model.rec and do the same for "large_rec"

__Creating a single file from a multi-volume RAR archive__:
	Open an archiving program that supports RAR format, such as WinRAR.
	Locate the first volume of the multi-volume archive (file with .part01.rar or .rar extension).
	Right-click on this file and select "Extract to specified folder".
	The program will automatically merge all volumes into one file.

**After installing**
To start Aurora after creating the Python virtual environment and installing all dependencies, simply enter "python main.py"

## Note
This file will be supplemented with information as necessary.

And also for cross-platform lovers - this code WILL be adopted for Linux
