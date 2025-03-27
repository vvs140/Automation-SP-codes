from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_playlist_video_titles(playlist_url):
    """Fetch and print video titles from the given YouTube playlist URL."""
    # Setup Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Load the playlist URL
        driver.get(playlist_url)
        time.sleep(5)  # Wait for the page to load (adjust if needed)
        
        # Extract video titles
        video_titles = driver.find_elements(By.CSS_SELECTOR, 'a#video-title')
        for video in video_titles:
            print(video.get_attribute('title'))
    
    finally:
        driver.quit()

if __name__ == "__main__":
    # Replace with your full playlist URL
    PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLR1gAGO6jQ_5QxjTd84pV9YF6e8MI5a-Q'
    
    # Fetch and print video titles
    get_playlist_video_titles(PLAYLIST_URL)
