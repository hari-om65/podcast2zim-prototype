import feedparser
import requests
import os

# Using a very reliable NASA podcast feed for this test
PODCAST_RSS_URL = "https://podcasts.files.bbci.co.uk/p02pc9ny.rss"
def start_scraping():
    print("--- Starting Podcast Scraper ---")
    
    # 1. Parse the feed
    feed = feedparser.parse(PODCAST_RSS_URL)
    
    # 2. Check if the feed loaded correctly
    if not feed.entries:
        print("Error: Could not find any episodes. Check your internet or the URL.")
        return

    # Try to get title safely
    podcast_title = feed.feed.get('title', 'Unknown Podcast')
    print(f"Scraping Podcast: {podcast_title}")
    
    # 3. Create a folder to save files
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # 4. Get the first 2 episodes only
    for entry in feed.entries[:2]:
        # Get title and clean it for Windows filenames
        original_title = entry.get('title', 'untitled_episode')
        clean_title = "".join(x for x in original_title if x.isalnum() or x in "._- ")
        
        # Look for the audio link (enclosure)
        if 'enclosures' in entry and entry.enclosures:
            audio_url = entry.enclosures[0].href
            print(f"Downloading: {clean_title}...")
            
            # 5. Download the file
            try:
                response = requests.get(audio_url, timeout=10)
                filename = f"downloads/{clean_title[:30]}.mp3"
                with open(filename, 'wb') as f:
                    f.write(response.content)
            except Exception as e:
                print(f"Failed to download {clean_title}: {e}")
        else:
            print(f"Skipping {clean_title} (No audio link found)")
            
    print("--- Done! Check your 'downloads' folder. ---")

if __name__ == "__main__":
    start_scraping()