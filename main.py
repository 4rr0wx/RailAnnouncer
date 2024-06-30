import os
import tkinter as tk
from tkinter import ttk, messagebox
from gtts import gTTS
import pygame


class TrainSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Simulator Announcements")

        self.current_station_index = 0
        self.stations = []

        # Strecke Dropdown
        self.strecke_var = tk.StringVar()
        self.strecke_dropdown = ttk.Combobox(root, textvariable=self.strecke_var)
        self.strecke_dropdown.bind("<<ComboboxSelected>>", self.load_zugdienste)
        self.strecke_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # Zugdienst Dropdown
        self.zugdienst_var = tk.StringVar()
        self.zugdienst_dropdown = ttk.Combobox(root, textvariable=self.zugdienst_var)
        self.zugdienst_dropdown.bind("<<ComboboxSelected>>", self.load_stations)
        self.zugdienst_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Buttons
        self.next_button = tk.Button(root, text="Nächste Station", command=self.next_station)
        self.next_button.grid(row=1, column=0, padx=10, pady=10)

        self.prev_button = tk.Button(root, text="Vorherige Station", command=self.prev_station)
        self.prev_button.grid(row=1, column=1, padx=10, pady=10)

        # Labels
        self.current_station_label = tk.Label(root, text="Aktuelle Station: ")
        self.current_station_label.grid(row=2, column=0, padx=10, pady=10)

        self.next_station_label = tk.Label(root, text="Nächste Station: ")
        self.next_station_label.grid(row=2, column=1, padx=10, pady=10)

        self.load_strecken()

    def load_strecken(self):
        strecken = [d for d in os.listdir() if os.path.isdir(d)]
        self.strecke_dropdown['values'] = strecken

    def load_zugdienste(self, event=None):
        strecke = self.strecke_var.get()
        if strecke:
            zugdienste = [f for f in os.listdir(strecke) if f.endswith('.txt')]
            self.zugdienst_dropdown['values'] = zugdienste

    def load_stations(self, event=None):
        self.current_station_index = 0
        strecke = self.strecke_var.get()
        zugdienst = self.zugdienst_var.get()
        if strecke and zugdienst:
            with open(os.path.join(strecke, zugdienst), 'r', encoding='utf-8') as file:
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
            announcement = f"Nächster Halt Next Stop: {station_name}"
            tts = gTTS(text=announcement, lang='de')
            tts.save("announcement.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("announcement.mp3")
            pygame.mixer.music.play()


if __name__ == "__main__":
    root = tk.Tk()
    app = TrainSimulator(root)
    root.mainloop()
