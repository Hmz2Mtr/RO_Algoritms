***Installation and Setup***
**Prerequisites**
Python 3.8 or higher: Make sure Python is installed on your system. You can download it from python.org.

Git: Install Git to clone the repository. Download it from git-scm.com.

**Step 1: Clone the Repository**
Clone this repository to your local machine using the following command:

Copy
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
**Step 2: Install Dependencies**
Install the required Python packages using pip. Run the following command:

Copy
pip install -r requirements.txt
If you don't have a requirements.txt file, install the dependencies manually:

Copy
pip install tkinter networkx matplotlib pillow
**Step 3: Run the Application**
To run the application, execute the following command:

Copy
python Run.py
Compiling the Project to an Executable
To compile the project into a standalone executable, use PyInstaller. Run the following command:

Copy
pyinstaller --onefile --windowed --hidden-import networkx --hidden-import PIL --hidden-import matplotlib --hidden-import matplotlib.backends.backend_tkagg Run.py
What This Command Does
--onefile: Bundles the application into a single executable file.

--windowed: Prevents a console window from appearing (for GUI applications).

--hidden-import: Ensures that specific modules (networkx, PIL, matplotlib, etc.) are included in the build.

The executable will be located in the dist folder.
