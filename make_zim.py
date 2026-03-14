import os
from libzim.writer import Creator, Item, FileProvider

# 1. We MUST define this class to satisfy the library's new requirements
class MyItem(Item):
    def __init__(self, path, title, fpath):
        super().__init__()
        self.path = path
        self.title = title
        self.fpath = fpath

    def get_path(self):
        return self.path

    def get_title(self):
        return self.title

    def get_mimetype(self):
        return "audio/mpeg"

    def get_contentprovider(self):
        # This tells libzim WHERE the file is on your hard drive
        return FileProvider(self.fpath)

    def get_hints(self):
        return {}

def create_podcast_zim():
    print("--- Starting ZIM Creation ---")
    
    with Creator("my_podcast.zim").config_indexing(True, "en") as creator:
        # Add Metadata
        creator.add_metadata("Title", "My Offline Podcast")
        creator.add_metadata("Language", "eng")

        download_path = "downloads"
        if not os.path.exists(download_path):
            print("Error: Run scraper.py first!")
            return

        # Add files using our new Class
        for filename in os.listdir(download_path):
            if filename.endswith(".mp3"):
                full_path = os.path.abspath(os.path.join(download_path, filename))
                
                # Create the item object
                # path_in_zim, title, path_on_disk
                item = MyItem(filename, filename, full_path)
                
                creator.add_item(item)
                print(f"Successfully added: {filename}")

        # Set main page
        all_files = [f for f in os.listdir(download_path) if f.endswith(".mp3")]
        if all_files:
            creator.set_mainpath(all_files[0])

    print("--- SUCCESS! Your .zim file is ready ---")

if __name__ == "__main__":
    create_podcast_zim()