import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk

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
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")  # Light gray background

        # Main frame to hold all content
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Load and display the EMSI logo
        self.load_logo()

        # School name label
        self.school_label = tk.Label(
            self.main_frame,
            text="EMSI Les Orangers",
            font=("Helvetica", 18, "bold"),
            fg="#33a543",  # Green color
            bg="#f0f0f0"
        )
        self.school_label.pack(pady=25)

        # Creator and supervisor labels
        self.create_labels()

        # Start button with custom style
        self.create_start_button()

    def load_logo(self):
        """Load and display the EMSI logo."""
        try:
            emsi_logo = Image.open("media//emsi_logo.png")
            emsi_logo = emsi_logo.resize((400, 70))
            self.emsi_logo_photo = ImageTk.PhotoImage(emsi_logo)
            self.logo_label = tk.Label(self.main_frame, image=self.emsi_logo_photo, bg="#f0f0f0")
            self.logo_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.emsi_logo_photo = None

    def create_labels(self):
        """Create labels for creator and supervisor."""
        self.creator_label = tk.Label(
            self.main_frame,
            text="Created by: MESTOUR Hamza",
            font=("Helvetica", 12),
            fg="#4C566A",
            bg="#f0f0f0"
        )
        self.creator_label.pack(pady=5)

        self.constructor_label = tk.Label(
            self.main_frame,
            text="Supervised by: Mme Mouna elmkhalet",
            font=("Helvetica", 12),
            fg="#4C566A",
            bg="#f0f0f0"
        )
        self.constructor_label.pack(pady=5)

    def create_start_button(self):
        """Create the Start button with custom styling."""
        self.start_button = ttk.Button(
            self.main_frame,
            text="Start",
            command=self.on_start_click,
            style="Custom.TButton"
        )
        self.start_button.pack(pady=30)

        # Custom style for the button
        self.style = ttk.Style()
        self.style.configure("Custom.TButton",
                             font=("Helvetica", 12, "bold"),
                             foreground="#FFFFFF",  # White text
                             background="#4CAF50",  # Green background
                             padding=10,
                             borderwidth=0,
                             focuscolor="#4CAF50",
                             focusthickness=10,
                             relief="flat",
                             bordercolor="#3c6342",
                             lightcolor="#66BB6A",
                             darkcolor="#388E3C",
                             )

        # Add hover and active effects
        self.style.map("Custom.TButton",
                       background=[("active", "#a9dab0")],
                       foreground=[("active", "#FFFFFF")],
                       lightcolor=[("active", "#388E3C")],
                       darkcolor=[("active", "#2E7D32")],
                       )

    def on_start_click(self):
        """Handle Start button click event."""
        self.root.destroy()
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
            "button_bg": "#4CAF50",  # Green buttons for light mode
            "button_fg": "#FFFFFF",  # White text
            "text_bg": "#F5F5F5",  # Light gray background for text area
            "text_fg": "#333333",  # Dark gray text for text area
            "entry_bg": "#FFFFFF",  # White background for entry widgets
            "entry_fg": "#000000"  # Black text for entry widgets
        }
        self.dark_colors = {
            "bg": "#2E3440",  # Dark blue-gray background
            "text": "#D8DEE9",  # Light gray text
            "button_bg": "#4C566A",  # Dark gray buttons
            "button_fg": "#ECEFF4",  # Light gray text
            "text_bg": "#3B4252",  # Darker gray background for text area
            "text_fg": "#E5E9F0",  # Light gray text for text area
            "entry_bg": "#4C566A",  # Dark gray background for entry widgets
            "entry_fg": "#ECEFF4"  # Light gray text for entry widgets
        }

        # Initialize UI components
        self.create_ui()

    def create_ui(self):
        """Create all UI components."""
        # Title label
        self.label_titre = tk.Label(self.root, text="Sélectionnez un algorithme à exécuter",
                                    font=("Arial", 16), bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.label_titre.pack(pady=10)

        # Theme switcher button
        self.theme_button = tk.Button(self.root, text="🌙 Dark Mode", command=self.toggle_theme,
                                      bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                                      font=("Arial", 10), relief=tk.FLAT)
        self.theme_button.pack(pady=1)

        # Frame for algorithm buttons
        self.frame_buttons = tk.Frame(self.root, bg=self.dark_colors["bg"])
        self.frame_buttons.pack(pady=1)

        # Scrolled text area for displaying results
        self.text_area = scrolledtext.ScrolledText(self.root, width=100, height=7, wrap=tk.WORD,
                                                   bg=self.dark_colors["text_bg"], fg=self.dark_colors["text_fg"],
                                                   font=("Consolas", 12))
        self.text_area.pack(pady=1, padx=20, fill=tk.BOTH, expand=True)

        # Frame to hold the Matplotlib canvas
        self.canvas_frame = tk.Frame(self.root, bg=self.dark_colors["bg"])
        self.canvas_frame.pack(pady=1, fill=tk.BOTH, expand=True)

        # Input frames for algorithms
        self.create_input_frames()

        # List of algorithms
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

        # Dynamically create buttons for each algorithm
        self.create_algorithm_buttons()

        # Apply default theme
        self.apply_theme(self.dark_colors)

    def create_input_frames(self):
        """Create input frames for algorithms."""
        # Frame for single input (e.g., number of vertices)
        self.input_frame = tk.Frame(self.root, bg=self.dark_colors["bg"])
        self.input_label = tk.Label(self.input_frame, text="Enter number of vertices (≥ 2):",
                                    bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.num_vertices_entry = tk.Entry(self.input_frame, bg=self.dark_colors["entry_bg"], fg=self.dark_colors["entry_fg"])
        self.num_vertices_entry.pack(side=tk.LEFT, padx=5)

        self.submit_button = tk.Button(self.input_frame, text="Submit",
                                       bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                                       font=("Arial", 10), relief=tk.FLAT)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        # Frame for Transport Optimal input (two inputs)
        self.algo_with_tow_inputs_frame = tk.Frame(self.root, bg=self.dark_colors["bg"])

        self.usines_label = tk.Label(self.algo_with_tow_inputs_frame, text="Number of factories (≥ 1):",
                                     bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.usines_label.pack(side=tk.LEFT, padx=10)

        self.usines_entry = tk.Entry(self.algo_with_tow_inputs_frame, bg=self.dark_colors["entry_bg"], fg=self.dark_colors["entry_fg"])
        self.usines_entry.pack(side=tk.LEFT, padx=10)

        self.magasins_label = tk.Label(self.algo_with_tow_inputs_frame, text="Number of stores (≥ 1):",
                                       bg=self.dark_colors["bg"], fg=self.dark_colors["text"])
        self.magasins_label.pack(side=tk.LEFT, padx=10)

        self.magasins_entry = tk.Entry(self.algo_with_tow_inputs_frame, bg=self.dark_colors["entry_bg"], fg=self.dark_colors["entry_fg"])
        self.magasins_entry.pack(side=tk.LEFT, padx=10)

        self.algo_with_tow_inputs_submit_button = tk.Button(self.algo_with_tow_inputs_frame, text="Submit",
                                                            bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                                                            font=("Arial", 10), relief=tk.FLAT)
        self.algo_with_tow_inputs_submit_button.pack(side=tk.LEFT, padx=10)

    def create_algorithm_buttons(self):
        """Create buttons for each algorithm."""
        for index, (label, func) in enumerate(self.algorithms):
            btn = tk.Button(self.frame_buttons, text=label,
                            command=lambda f=func: self.show_input_frame(f),
                            bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"],
                            font=("Arial", 10), padx=5, pady=5, relief=tk.FLAT, width=20)
            if label == "Transport Optimal":
                btn.grid(row=2, column=2, padx=5, pady=5)
            else:
                btn.grid(row=index // 5, column=index % 5, padx=5, pady=5)

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        if self.theme_mode == "light":
            self.theme_mode = "dark"
            self.apply_theme(self.dark_colors)
            self.theme_button.config(text="🌙 Dark Mode", bg=self.dark_colors["button_bg"], fg=self.dark_colors["button_fg"])
        else:
            self.theme_mode = "light"
            self.apply_theme(self.light_colors)
            self.theme_button.config(text="☀️ Light Mode", bg=self.light_colors["button_bg"], fg=self.light_colors["button_fg"])

    def apply_theme(self, colors):
        """Apply the selected theme colors to the UI."""
        self.root.configure(bg=colors["bg"])
        self.label_titre.config(bg=colors["bg"], fg=colors["text"])
        self.frame_buttons.config(bg=colors["bg"])
        self.text_area.config(bg=colors["text_bg"], fg=colors["text_fg"])
        self.canvas_frame.config(bg=colors["bg"])
        for btn in self.frame_buttons.winfo_children():
            btn.config(bg=colors["button_bg"], fg=colors["button_fg"])

        # Update input frame components
        self.input_frame.config(bg=colors["bg"])
        self.input_label.config(bg=colors["bg"], fg=colors["text"])
        self.num_vertices_entry.config(bg=colors["entry_bg"], fg=colors["entry_fg"])
        self.submit_button.config(bg=colors["button_bg"], fg=colors["button_fg"])

        # Update Transport Optimal input frame components
        self.algo_with_tow_inputs_frame.config(bg=colors["bg"])
        self.usines_label.config(bg=colors["bg"], fg=colors["text"])
        self.usines_entry.config(bg=colors["entry_bg"], fg=colors["entry_fg"])
        self.magasins_label.config(bg=colors["bg"], fg=colors["text"])
        self.magasins_entry.config(bg=colors["entry_bg"], fg=colors["entry_fg"])
        self.algo_with_tow_inputs_submit_button.config(bg=colors["button_bg"], fg=colors["button_fg"])

    def show_input_frame(self, algo_func):
        """Show the appropriate input frame based on the selected algorithm."""
        self.text_area.config(height=7)
        self.text_area.delete("1.0", "end")
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        if algo_func in [algo_transport_optimal, algo_nord_ouest, algo_moindre_cout, algo_stepping_stone]:
            self.algo_with_tow_inputs_frame.pack(pady=10)
            self.input_frame.pack_forget()
            self.algo_with_tow_inputs_submit_button.config(command=lambda: self.executer_algo_with_tow_inputs(algo_func))
        elif algo_func in [create_directed_graph, algo_welsh_powell, algo_kruskal, algo_dijkstra, algo_bellman_ford, algo_ford_fulkerson]:
            self.input_frame.pack(pady=10)
            self.algo_with_tow_inputs_frame.pack_forget()
            self.submit_button.config(command=lambda: self.executer_algo_with_input(algo_func))
        else:
            self.input_frame.pack_forget()
            self.algo_with_tow_inputs_frame.pack_forget()
            self.executer_algo(algo_func)

    def executer_algo_with_tow_inputs(self, algo_func):
        """Execute an algorithm that requires two inputs."""
        try:
            nb_usines = int(self.usines_entry.get())
            nb_magasins = int(self.magasins_entry.get())
            if nb_usines < 1 or nb_magasins < 1:
                raise ValueError("Number of factories and stores must be at least 1.")
            algo_func(self.canvas_frame, self.text_area, nb_usines, nb_magasins)
        except ValueError as e:
            self.text_area.delete("1.0", "end")
            self.text_area.insert("end", f"Invalid input! {str(e)}\n")

    def executer_algo_with_input(self, algo_func):
        """Execute an algorithm that requires one input."""
        num_vertices = self.num_vertices_entry.get()
        try:
            num_vertices = int(num_vertices)
            if num_vertices < 2:
                raise ValueError("Number of vertices must be at least 2.")
            algo_func(self.canvas_frame, self.text_area, num_vertices)
        except ValueError:
            self.text_area.delete("1.0", "end")
            self.text_area.insert("end", "Invalid input! Please enter a valid number of vertices (≥ 2).")

    def executer_algo(self, algo_func):
        """Execute an algorithm that requires no input."""
        algo_func(self.canvas_frame, self.text_area)


if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApp(root)
    root.mainloop()