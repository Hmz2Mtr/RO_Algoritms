***Installation and Setup***/n
**Prerequisites**/n
Python 3.8 or higher: Make sure Python is installed on your system. You can download it from python.org./n
/n
Git: Install Git to clone the repository. Download it from git-scm.com./n
/n
**Step 1: Clone the Repository**/n
Clone this repository to your local machine using the following command:/n
/n
Copy/n
git clone https://github.com/your-username/your-repo-name.git/n
cd your-repo-name/n
**Step 2: Install Dependencies**/n
Install the required Python packages using pip. Run the following command:/n
/n
Copy/n
pip install -r requirements.txt/n
If you don't have a requirements.txt file, install the dependencies manually:/n
/n
Copy/n
pip install tkinter networkx matplotlib pillow/n
**Step 3: Run the Application**/n
To run the application, execute the following command:/n
/n
Copy/n
python Run.py/n
Compiling the Project to an Executable/n
To compile the project into a standalone executable, use PyInstaller. Run the following command:/n
/n
Copy/n
pyinstaller --onefile --windowed --hidden-import networkx --hidden-import PIL --hidden-import matplotlib --hidden-import matplotlib.backends.backend_tkagg Run.py/n
What This Command Does/n
--onefile: Bundles the application into a single executable file./n
/n
--windowed: Prevents a console window from appearing (for GUI applications)./n
/n
--hidden-import: Ensures that specific modules (networkx, PIL, matplotlib, etc.) are included in the build./n
/n
The executable will be located in the dist folder./n
