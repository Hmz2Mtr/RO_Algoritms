## **Prerequisites**
Before you begin, ensure you have the following installed on your system:

1. **Python 3.8 or higher**:  
   Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Git**:  
   Install Git to clone the repository. Download it from [git-scm.com](https://git-scm.com/).

---

## **Step 1: Clone the Repository**
To get started, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
## **Step 2: Install Dependencies**
1. **Install the required Python packages using pip. Run the following command:**

```bash
pip install -r requirements.txt
If you don't have a requirements.txt file, install the dependencies manually:
pip install tkinter networkx matplotlib pillow
```

## **Step 3: Run the Application**
1. **To run the application, execute the following command:**

```bash
python Run.py
```

Compiling the Project to an Executable
To compile the project into a standalone executable, use PyInstaller. Run the following command:

```bash
pyinstaller --onefile --windowed --hidden-import networkx --hidden-import PIL --hidden-import matplotlib --hidden-import matplotlib.backends.backend_tkagg Run.py
```
**What This Command Does**
1. --onefile: Bundles the application into a single executable file.

2. --windowed: Prevents a console window from appearing (for GUI applications).

3. --hidden-import: Ensures that specific modules (networkx, PIL, matplotlib, etc.) are included in the build.

**The executable will be located in the dist folder.**
