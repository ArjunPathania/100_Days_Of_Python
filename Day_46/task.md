```markdown
# Task: Create a Spotify Playlist from Billboard's Top 100 Songs

## Objective:
This task is designed to create a private Spotify playlist using the top 100 songs from the Billboard Hot 100 chart for a specific date. The date will be input by the user, and the program will scrape the song names from the Billboard website and search for those songs on Spotify. It will then create a playlist and add those songs to it.

## Requirements:
1. **Python 3.x**: Ensure Python 3.x is installed.
2. **External Libraries**:
   - `requests`: For making HTTP requests to the Billboard Hot 100 chart page.
   - `beautifulsoup4`: For parsing the HTML content of the Billboard page.
   - `spotipy`: For interacting with the Spotify API.
   - `python-dotenv`: For loading environment variables from a `.env` file.

   Install the necessary libraries using:
   ```bash
   pip install requests beautifulsoup4 spotipy python-dotenv
   ```

3. **Spotify Developer Account**:
   - Create a Spotify Developer account and set up an application in the Spotify Developer Dashboard.
   - Obtain your **Client ID** and **Client Secret**, and add them to your `.env` file.

4. **.env File**:
   - Store your **Spotify Client ID**, **Client Secret**, and **Spotify Username** in a `.env` file in the same directory as the script:
     ```
     SPOTIPY_CLIENT_ID=<Your_Spotify_Client_ID>
     SPOTIPY_CLIENT_SECRET=<Your_Spotify_Client_Secret>
     SPOTIPY_USERNAME=<Your_Spotify_Username>
     ```

## Process:

### 1. **User Input for Year**:
   - The program asks the user to input a date (in the format `YYYY-MM-DD`) for the specific year they want to get the Billboard Hot 100 for. This will be used to search for songs released in that year on Spotify.

### 2. **Scraping Billboard's Hot 100**:
   - Using `requests` and `BeautifulSoup`, the program makes an HTTP request to the Billboard Hot 100 chart page for the specified date.
   - The program extracts the song names from the HTML structure using the `select()` method to target the appropriate `<h3>` tags containing the song titles.

### 3. **Search Songs on Spotify**:
   - For each song title scraped from Billboard, the program searches for the song in the specified year using the `spotipy.Spotify().search()` method.
   - The program appends the URI of each track to the `song_uris` list for later use in creating the playlist.

### 4. **Create Playlist on Spotify**:
   - Using the Spotify API, the program creates a private playlist with the name formatted as `YYYY-MM-DD Billboard 100`.
   - The playlist is created using `sp.user_playlist_create()`, which takes the user's ID, playlist name, and description.

### 5. **Add Songs to Playlist**:
   - The program adds the songs from the `song_uris` list to the newly created playlist using the `sp.playlist_add_items()` method.

### 6. **Error Handling**:
   - If a song cannot be found on Spotify (e.g., due to licensing issues), it will be skipped and a message will be printed indicating that the song doesn’t exist on Spotify.

## Steps to Set Up:

1. **Install Dependencies**:
   - Ensure that Python 3.x is installed on your system.
   - Install the required libraries by running:
   ```bash
   pip install requests beautifulsoup4 spotipy python-dotenv
   ```

2. **Set Up .env File**:
   - Create a `.env` file in the same directory as your script and add your **Spotify Client ID**, **Client Secret**, and **Username** as shown:
     ```
     SPOTIPY_CLIENT_ID=<Your_Spotify_Client_ID>
     SPOTIPY_CLIENT_SECRET=<Your_Spotify_Client_Secret>
     SPOTIPY_USERNAME=<Your_Spotify_Username>
     ```

3. **Run the Script**:
   - Execute the Python script in your terminal or IDE. When prompted, enter the year in `YYYY-MM-DD` format.
   - The script will scrape the Billboard Hot 100 for that date, search for the songs on Spotify, and create a playlist containing those songs.

4. **Check Your Playlist**:
   - After running the script, check your Spotify account for a new private playlist named `YYYY-MM-DD Billboard 100`.
   - This playlist will contain the top 100 songs from the Billboard chart for the specified date.

## Expected Output:
- A private Spotify playlist with the top 100 songs from the Billboard Hot 100 chart on the specified date will be created in your Spotify account.
- If any song is missing from Spotify, it will be skipped with a message printed to the console.

## Troubleshooting:
- **Missing Songs**: If a song is not found on Spotify, ensure that the song exists in Spotify's catalog and that the correct year was provided.
- **Invalid Date Format**: If the date is not in the correct format (`YYYY-MM-DD`), the program may fail to find the correct chart or playlist.
- **Spotify Authentication**: If there are issues with authentication, ensure that your `client_id`, `client_secret`, and `username` are correctly set in the `.env` file, and that you have authorized the app.

## Notes:
- The playlist created is **private** and not accessible to others unless shared.
- This script uses the Spotify API, so an active Spotify account is required to use the playlist features.
- The Billboard page scraped in this script is archived. If the page format changes, the scraping logic may need to be updated.
```