import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
import threading

# Set your Gemini API key
API_KEY = "your_api_key"
genai.configure(api_key=API_KEY)

def generate_text():
    prompt = input_text.get("1.0", tk.END).strip()
    if not prompt:
        return
    
    generate_button.config(state=tk.DISABLED)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Generating...")
    output_text.config(state=tk.DISABLED)
    
    def fetch_response():
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            result = response.text.strip()
        except Exception as e:
            result = f"Error: {str(e)}"
        
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state=tk.DISABLED)
        generate_button.config(state=tk.NORMAL)
    
    thread = threading.Thread(target=fetch_response)
    thread.start()

# UI Setup
root = tk.Tk()
root.title("MyGPT")
root.geometry("500x400")
root.resizable(True, True)

input_label = tk.Label(root, text="Enter your prompt:")
input_label.pack(pady=5)

input_text = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD)
input_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

generate_button = tk.Button(root, text="Generate Text", command=generate_text)
generate_button.pack(pady=10)

output_label = tk.Label(root, text="Generated Text:")
output_label.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
