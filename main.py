import os
import tkinter as tk
from tkinter import ttk, messagebox
from gtts import gTTS
import pygame
import subprocess
import platform


class TrainSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("RailAnnouncer")

        self.current_station_index = 0
        self.stations = []

        # Ensure 'Routen' directory exists
        self.routes_dir = 'Routen'
        if not os.path.exists(self.routes_dir):
            os.makedirs(self.routes_dir)

        # Labels for Dropdowns
        self.strecke_label = tk.Label(root, text="Wähle eine Strecke:")
        self.strecke_label.grid(row=0, column=0, padx=10, pady=10)

        self.zugdienst_label = tk.Label(root, text="Wähle einen Zugdienst:")
        self.zugdienst_label.grid(row=0, column=1, padx=10, pady=10)

        # Strecke Dropdown
        self.strecke_var = tk.StringVar()
        self.strecke_dropdown = ttk.Combobox(root, textvariable=self.strecke_var)
        self.strecke_dropdown.bind("<<ComboboxSelected>>", self.load_zugdienste)
        self.strecke_dropdown.grid(row=1, column=0, padx=10, pady=10)

        # Zugdienst Dropdown
        self.zugdienst_var = tk.StringVar()
        self.zugdienst_dropdown = ttk.Combobox(root, textvariable=self.zugdienst_var)
        self.zugdienst_dropdown.bind("<<ComboboxSelected>>", self.load_stations)
        self.zugdienst_dropdown.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.next_button = tk.Button(root, text="Nächste Station", command=self.next_station)
        self.next_button.grid(row=2, column=0, padx=10, pady=10)

        self.prev_button = tk.Button(root, text="Vorherige Station", command=self.prev_station)
        self.prev_button.grid(row=2, column=1, padx=10, pady=10)

        self.open_folder_button = tk.Button(root, text="Ordner öffnen", command=self.open_folder)
        self.open_folder_button.grid(row=2, column=2, padx=10, pady=10)

        # Labels
        self.current_station_label = tk.Label(root, text="Aktuelle Station: ")
        self.current_station_label.grid(row=3, column=0, padx=10, pady=10)

        self.next_station_label = tk.Label(root, text="Nächste Station: ")
        self.next_station_label.grid(row=3, column=1, padx=10, pady=10)

        self.load_strecken()

    def load_strecken(self):
        strecken = [d for d in os.listdir(self.routes_dir) if os.path.isdir(os.path.join(self.routes_dir, d))]
        self.strecke_dropdown['values'] = strecken

    def load_zugdienste(self, event=None):
        strecke = self.strecke_var.get()
        if strecke:
            zugdienste = [f for f in os.listdir(os.path.join(self.routes_dir, strecke)) if f.endswith('.txt')]
            self.zugdienst_dropdown['values'] = zugdienste

    def load_stations(self, event=None):
        self.current_station_index = 0
        strecke = self.strecke_var.get()
        zugdienst = self.zugdienst_var.get()
        if strecke and zugdienst:
            self.current_path = os.path.join(self.routes_dir, strecke, zugdienst)
            with open(self.current_path, 'r', encoding='utf-8') as file:
                self.stations = [line.strip() for line in file.readlines()]
            self.update_station_labels()

    def update_station_labels(self):
        if self.stations:
            current_station = self.stations[self.current_station_index]
            next_station = self.stations[self.current_station_index + 1] if self.current_station_index + 1 < len(
                self.stations) else "Endstation"
            self.current_station_label.config(text=f"Aktuelle Station: {current_station}")
            self.next_station_label.config(text=f"Nächste Station: {next_station}")

    def next_station(self):
        if self.current_station_index < len(self.stations) - 1:
            self.current_station_index += 1
            self.announce_station()
            self.update_station_labels()

    def prev_station(self):
        if self.current_station_index > 0:
            self.current_station_index -= 1
            self.announce_station()
            self.update_station_labels()

    def announce_station(self):
        if self.stations:
            station_name = self.stations[self.current_station_index]
            announcement = f"Nächster Halt: {station_name}"
            tts = gTTS(text=announcement, lang='de')
            tts.save("announcement.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("announcement.mp3")
            pygame.mixer.music.play()

    def open_folder(self):
        folder_path = self.routes_dir
        if platform.system() == "Windows":
            os.startfile(folder_path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", folder_path])
        else:
            subprocess.Popen(["xdg-open", folder_path])


if __name__ == "__main__":
    root = tk.Tk()
    app = TrainSimulator(root)
    root.mainloop()
