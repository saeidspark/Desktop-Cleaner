from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
import logging
from configparser import ConfigParser
from watchdog.events import FileSystemEventHandler
from win10toast import ToastNotifier
from source.directories import Directories
import os
from time import sleep

dir_path = [os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))]
dir_path_str = str(dir_path[0])
os.chdir(dir_path_str)

class MoverHandler(FileSystemEventHandler, Directories):
    config = ConfigParser()
    config.read('config\\config.ini')
    def __init__(self):
        self.source_dir = self.get_downloads_path()
        self.dest_dir_music = self.get_musics_path()
        self.dest_dir_video = self.get_videos_path()
        self.dest_dir_image = self.get_images_path()
        self.dest_dir_documents = self.get_documents_path()
        self.dest_dir_programs = self.get_programs_path()
        self.dest_dir_contacts = self.get_contacts_path()
        
        self.image_extensions = self.config.get("Extensions", "image_extensions").split(" , ")
        self.video_extensions = self.config.get("Extensions", "video_extensions").split(" , ")
        self.audio_extensions = self.config.get("Extensions", "audio_extensions").split(" , ")
        self.document_extensions = self.config.get("Extensions", "document_extensions").split(" , ")
        self.program_extensions = self.config.get("Extensions", "program_extensions").split(" , ")
        self.contact_extensions = self.config.get("Extensions", "contact_extensions").split(" , ")
        
    def make_unique(self, dest, name):
        filename, extension = splitext(name)
        counter = 1
        # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
        while exists(f"{dest}/{name}"):
            name = f"{filename}({str(counter)}){extension}"
            counter += 1
        return name

    def move_file(self, dest, entry, name):
        if exists(f"{dest}/{name}"):
            unique_name = self.make_unique(dest, name)
            oldName = join(dest, name)
            newName = join(dest, unique_name)
            rename(oldName, newName)
        move(entry, dest)
        sleep(1)

    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        sleep(1)
        with scandir(self.source_dir) as entries:
            for entry in entries:
                namek = entry.name
                self.check_audio_files(entry, namek)
                self.check_video_files(entry, namek)
                self.check_image_files(entry, namek)
                self.check_document_files(entry, namek)
                self.check_program_files(entry, namek)
                self.check_contact_files(entry, namek)
    
    def start(self):
        self.on_modified(None)
        
    def check_audio_files(self, entry, name):  # * Checks all Audio Files
        for audio_extension in self.audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                self.move_file(self.dest_dir_music, entry, name)
                logging.info(f"Moved audio file: {name}")
                
    def check_video_files(self, entry, name):  # * Checks all Video Files
        for video_extension in self.video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                self.move_file(self.dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for image_extension in self.image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                self.move_file(self.dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for document_extension in self.document_extensions:
            if name.endswith(document_extension) or name.endswith(document_extension.upper()):
                self.move_file(self.dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_program_files(self, entry, name):  # * Checks all Program Files
        for program_extension in self.program_extensions:
            if name.endswith(program_extension) or name.endswith(program_extension.upper()):
                self.move_file(self.dest_dir_programs, entry, name)
                logging.info(f"Moved program file: {name}")

    def check_contact_files(self, entry, name):  # * Checks all Contact Files
        for contact_extension in self.contact_extensions:
            if name.endswith(contact_extension) or name.endswith(contact_extension.upper()):
                self.move_file(self.dest_dir_contacts, entry, name)
                logging.info(f"Moved contact file: {name}")