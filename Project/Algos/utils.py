# utils.py

def clear_canvas(canvas_frame):
    """
    Clear all widgets inside the given canvas_frame.
    """
    for widget in canvas_frame.winfo_children():
        widget.destroy()
