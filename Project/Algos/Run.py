import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk  # Updated import for Pillow 10.0.0+

# Import each algorithm from its respective file
from Algos.algo_create_directed_graph import create_directed_graph
from Algos.algo_welsh_powell import algo_welsh_powell
from Algos.algo_kruskal import algo_kruskal
from Algos.algo_dijkstra import algo_dijkstra
from Algos.algo_bellman_ford import algo_bellman_ford
from Algos.algo_nord_ouest import algo_nord_ouest
from Algos.algo_moindre_cout import algo_moindre_cout
from Algos.algo_stepping_stone import algo_stepping_stone
from Algos.algo_ford_fulkerson import algo_ford_fulkerson
from Algos.algo_potentiel_metra import algo_potentiel_metra
from Algos.algo_transport_optimal import algo_transport_optimal

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EMSI School GUI")
        self.root.geometry("500x400")  # Set a fixed window size
        self.root.configure(bg="#f0f0f0")  # Light gray background

        # Create a main frame to hold all content
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Load the image
        try:
            emsi_logo = Image.open("media//emsi_logo.png")
            emsi_logo = emsi_logo.resize((400, 70))  # Resize the image
            self.emsi_logo_photo = ImageTk.PhotoImage(emsi_logo)  # Store as an instance variable
        except Exception as e:
            print(f"Error loading image: {e}")
            self.emsi_logo_photo = None

        # Create a label and store a reference to the image
        if self.emsi_logo_photo:
            self.logo_label = tk.Label(self.main_frame, image=self.emsi_logo_photo, bg="#f0f0f0")
            self.logo_label.pack(pady=10)

        # School name label
        self.school_label = tk.Label(
            self.main_frame, 
            text="EMSI Les Orangers", 
            font=("Helvetica", 18, "bold"), 
            fg="#33a543",  # Dark blue-gray color
            bg="#f0f0f0"
        )
        self.school_label.pack(pady=25)

        # Creator name label
        self.creator_label = tk.Label(
            self.main_frame, 
            text="Created by: MESTOUR Hamza", 
            font=("Helvetica", 12), 
            fg="#4C566A",  # Dark gray color
            bg="#f0f0f0"
        )
        self.creator_label.pack(pady=5)

        # Constructor name label
        self.constructor_label = tk.Label(
            self.main_frame, 
            text="Supervised by: Mme Mouna elmkhalet", 
            font=("Helvetica", 12), 
            fg="#4C566A",  # Dark gray color
            bg="#f0f0f0"
        )
        self.constructor_label.pack(pady=5)

        # Button that triggers another script or function
        self.start_button = ttk.Button(
            self.main_frame, 
            text="Start", 
            command=self.on_start_click, 
            style="Custom.TButton"  # Custom style for the button
        )
        self.start_button.pack(pady=30)

        # Custom style for the button
        self.style = ttk.Style()
        self.style.configure("Custom.TButton", 
                     font=("Helvetica", 12, "bold"), 
                     foreground="#33a543",  # White text
                     background="#4CAF50",  # Green background
                     padding=10,
                     borderwidth=0,
                     focuscolor="#4CAF50",
                     focusthickness=10,
                     relief="flat",
                     bordercolor="#3c6342",  # Border color
                     lightcolor="#66BB6A",   # Light green for gradient
                     darkcolor="#388E3C",    # Dark green for gradient
                     )

        # Add hover and active effects
        self.style.map("Custom.TButton",
                     background=[("active", "#a9dab0")],  # Darker green on hover
                     foreground=[("active", "#2bb83e")],  # Keep text white on hover
                     lightcolor=[("active", "#388E3C")],  # Darker gradient on hover
                     darkcolor=[("active", "#2E7D32")],   # Even darker gradient on hover
                     )

    def on_start_click(self):
        #print("Start button clicked!")
        # Destroy the main window
        self.root.destroy()
        # Launch the AlgorithmApp
        root = tk.Tk()
        AlgorithmApp(root)
        root.mainloop()


class AlgorithmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Graphique - Algorithmes")
        self.root.geometry("1000x800")

        # Theme variables
        self.theme_mode = "dark"  # Default theme is dark
        self.light_colors = {
            "bg": "#FFFFFF",  # White background
            "text": "#333333",  # Dark gray text
            "button_bg": "#0078D7",  # Professional blue buttons
            "button_fg": "#FFFFFF",  # White text
            "text_bg": "#F5F5F5",  # Light gray background for text area
            "text_fg": "#333333"  # Dark gray text for text area
        }
        self.dark_colors = {
            "bg": "#2E3440",  # Dark blue-gray background
            "text": "#D8DEE9",  # Light gray text
            "button_bg": "#4C566A",  # Dark gray buttons
            "button_fg": "#ECEFF4",  # Light gray text
            "text_bg": "#3B4252",  # Darker gray background for text area
            "text_fg": "#E5E9F0"  # Light gray text for text area
        }

        # Title label
        self.label_titre = tk.Label(root, text="Sélectionnez un algorithme à exécuter",
                                   font=("Arial", 16), bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.label_titre.pack(pady=10)

        # Theme switcher button
        self.theme_button = tk.Button(root, text="🌙 Dark Mode", command=self.toggle_theme,
                                     bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                                     font=("Arial", 10), relief=tk.FLAT)
        self.theme_button.pack(pady=1)

        # Frame for algorithm buttons
        self.frame_buttons = tk.Frame(root, bg=self.dark_colors["bg"])
        self.frame_buttons.pack(pady=1)

        # Scrolled text area for displaying results
        self.text_area = scrolledtext.ScrolledText(root, width=100, height=7, wrap=tk.WORD,
                                                  bg=self.dark_colors["text_bg"], fg=self.dark_colors["text_fg"],
                                                  font=("Consolas", 12))
        self.text_area.pack(pady=1, padx=20, fill=tk.BOTH, expand=True)  # Allow expansion

        # Frame to hold the Matplotlib canvas
        self.canvas_frame = tk.Frame(root, bg=self.dark_colors["bg"])
        self.canvas_frame.pack(pady=1, fill=tk.BOTH, expand=True)  # Expand canvas frame

        # Frame for input (hidden by default)
        self.input_frame = tk.Frame(root, bg=self.dark_colors["bg"])
        self.input_label = tk.Label(self.input_frame, text="Enter number of vertices (≥ 2):", 
                                   bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.num_vertices_entry = tk.Entry(self.input_frame)
        self.num_vertices_entry.pack(side=tk.LEFT, padx=5)

        self.submit_button = tk.Button(self.input_frame, text="Submit", 
                                      bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                                      font=("Arial", 10), relief=tk.FLAT)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        # Frame for Transport Optimal input (hidden by default)
        self.algo_with_tow_inputs_frame = tk.Frame(root, bg=self.dark_colors["bg"])

        # Labels and entries for nb_usines and nb_magasins
        self.usines_label = tk.Label(self.algo_with_tow_inputs_frame, text="Number of factories (≥ 1):", 
                                    bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.usines_label.pack(side=tk.LEFT, padx=10)

        self.usines_entry = tk.Entry(self.algo_with_tow_inputs_frame)
        self.usines_entry.pack(side=tk.LEFT, padx=10)

        self.magasins_label = tk.Label(self.algo_with_tow_inputs_frame, text="Number of stores (≥ 1):", 
                                      bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.magasins_label.pack(side=tk.LEFT, padx=10)

        self.magasins_entry = tk.Entry(self.algo_with_tow_inputs_frame)
        self.magasins_entry.pack(side=tk.LEFT, padx=10)

        self.algo_with_tow_inputs_submit_button = tk.Button(self.algo_with_tow_inputs_frame, text="Submit", 
                                                           bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                                                           font=("Arial", 10), relief=tk.FLAT)
        self.algo_with_tow_inputs_submit_button.pack(side=tk.LEFT, padx=10)

        # List of (label, function) pairs for the algorithms
        self.algorithms = [
            ("Théorie des Graphes", create_directed_graph),
            ("Welsh Powell", algo_welsh_powell),
            ("Kruskal", algo_kruskal),
            ("Dijkstra", algo_dijkstra),
            ("Bellman-Ford", algo_bellman_ford),
            ("Nord-Ouest", algo_nord_ouest),
            ("Moindre Coût", algo_moindre_cout),
            ("Stepping Stone", algo_stepping_stone),
            ("Ford-Fulkerson", algo_ford_fulkerson),
            ("Potentiel Metra", algo_potentiel_metra),
            ("Transport Optimal", algo_transport_optimal)
        ]

        # Dynamically create a button for each algorithm
        for index, (label, func) in enumerate(self.algorithms):
            btn = tk.Button(self.frame_buttons, text=label,
                            command=lambda f=func: self.show_input_frame(f),
                            bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                            font=("Arial", 10), padx=5, pady=5, relief=tk.FLAT, width=20)  # Uniform width
            if label == "Transport Optimal":
                btn.grid(row=2, column=2, padx=5, pady=5)
            else:
                btn.grid(row=index // 5, column=index % 5, padx=5, pady=5)

        # Apply default theme after defining all UI elements
        self.apply_theme(self.dark_colors)

    def toggle_theme(self):
        if self.theme_mode == "light":
            self.theme_mode = "dark"
            self.apply_theme(self.dark_colors)
            self.theme_button.config(text="🌙 Dark Mode", bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"])  # Update theme button
        else:
            self.theme_mode = "light"
            self.apply_theme(self.light_colors)
            self.theme_button.config(text="☀️ Light Mode", bg=self.light_colors["button_bg"], fg=self.light_colors["button_fg"])  # Update theme button

    def apply_theme(self, colors):
        self.root.configure(bg=colors["bg"])
        self.label_titre.config(bg=colors["bg"], fg=colors["text"])
        self.frame_buttons.config(bg=colors["bg"])
        self.text_area.config(bg=colors["text_bg"], fg=colors["text_fg"])
        self.canvas_frame.config(bg=colors["bg"])
        for btn in self.frame_buttons.winfo_children():
            btn.config(bg=colors["button_bg"], fg=colors["button_fg"])

    def show_input_frame(self, algo_func):
        # Reset the height of the text area to its default
        self.text_area.config(height=7)  # Default height is 7 lines

        # Clear results when any algorithm button is clicked
        self.text_area.delete("1.0", "end")
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        # Show Transport Optimal input frame
        if algo_func in [algo_transport_optimal, algo_nord_ouest, algo_moindre_cout, algo_stepping_stone]:
            self.algo_with_tow_inputs_frame.pack(pady=10)
            self.input_frame.pack_forget()
            self.algo_with_tow_inputs_submit_button.config(command=lambda: self.executer_algo_with_tow_inputs(algo_func))
        elif algo_func in [create_directed_graph, algo_welsh_powell, algo_kruskal, algo_dijkstra, algo_bellman_ford, algo_ford_fulkerson]:
            self.input_frame.pack(pady=10)  # Show input frame
            self.algo_with_tow_inputs_frame.pack_forget()  # Hide Transport Optimal input frame
            self.submit_button.config(command=lambda: self.executer_algo_with_input(algo_func))
        else:
            self.input_frame.pack_forget()  # Hide input frame
            self.algo_with_tow_inputs_frame.pack_forget()  # Hide Transport Optimal input frame
            self.executer_algo(algo_func)

    def executer_algo_with_tow_inputs(self, algo_func):
        try:
            nb_usines = int(self.usines_entry.get())
            nb_magasins = int(self.magasins_entry.get())
            if nb_usines < 1 or nb_magasins < 1:
                raise ValueError("Number of factories and stores must be at least 1.")
            # Execute the algorithm with the specified number of factories and stores
            algo_func(self.canvas_frame, self.text_area, nb_usines, nb_magasins)
        except ValueError as e:
            self.text_area.delete("1.0", "end")
            self.text_area.insert("end", f"Invalid input! {str(e)}\n")

    def executer_algo_with_input(self, algo_func):
        num_vertices = self.num_vertices_entry.get()
        try:
            num_vertices = int(num_vertices)
            if num_vertices < 2:
                raise ValueError("Number of vertices must be at least 2.")
            # Execute the algorithm with the specified number of vertices
            algo_func(self.canvas_frame, self.text_area, num_vertices)
        except ValueError:
            self.text_area.delete("1.0", "end")
            self.text_area.insert("end", "Invalid input! Please enter a valid number of vertices (≥ 2).")

    def executer_algo(self, algo_func):
        # Execute the chosen algorithm
        algo_func(self.canvas_frame, self.text_area)

if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApp(root)
    root.mainloop()