import os
import winreg

class Directories:
    def get_downloads_path(self):
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                source_dir = winreg.QueryValueEx(key, downloads_guid)[0]
            return source_dir
        else:
            return os.path.join(os.path.expanduser('~'), 'downloads')
    
    def get_musics_path(self):
        """Returns the default music path for linux or windows"""
        if os.name == 'nt':
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            music_guid = 'My Music'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                dest_dir_music = winreg.QueryValueEx(key, music_guid)[0]
                return dest_dir_music
        else:
            return os.path.join(os.path.expanduser('~'), 'Music')
            
    def get_images_path(self):
        """Returns the default images path for linux or windows"""
        if os.name == 'nt':
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            image_guid = 'My Pictures'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                dest_dir_image = winreg.QueryValueEx(key, image_guid)[0]
                return dest_dir_image
        else:
            return os.path.join(os.path.expanduser('~'), 'Pictures')

    def get_videos_path(self):
        """Returns the default video path for linux or windows"""
        if os.name == 'nt':
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            video_guid = 'My Video'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                dest_dir_video = winreg.QueryValueEx(key, video_guid)[0]
                return dest_dir_video
        else:
            return os.path.join(os.path.expanduser('~'), 'Videos')
        
    def get_contacts_path(self):
        """Returns the default contacts path for linux or windows"""
        if os.name == 'nt':
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            contacts_guid = '{56784854-C6CB-462B-8169-88E350ACB882}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                dest_dir_contacts = winreg.QueryValueEx(key, contacts_guid)[0]
                return dest_dir_contacts
        else:
            return os.path.join(os.path.expanduser('~'), 'Contacts')
        
    def get_documents_path(self):
        """Returns the default documents path for linux or windows"""
        if os.name == 'nt':
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            documents_guid = 'Personal'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                dest_dir_documents = winreg.QueryValueEx(key, documents_guid)[0]
                return dest_dir_documents
        else:
            return os.path.join(os.path.expanduser('~'), 'Documents')
        
    def get_programs_path(self):
        """Returns the default programs path for linux or windows"""
        if os.name == 'nt':
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            programs_guid = 'Programs'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                dest_dir_programs = winreg.QueryValueEx(key, programs_guid)[0]
                return dest_dir_programs
        else:
            return os.path.join(os.path.expanduser('~'), '.config', 'autostart')