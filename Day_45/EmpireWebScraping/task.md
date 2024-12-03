```markdown
# Task: Scrape and Save Top 100 Movies

## Objective:
The objective of this task is to scrape a webpage listing the top 100 movies from the Empire website (archived version) and save the movie titles to a text file named `movies.txt`. The data is retrieved using web scraping techniques, and the movie titles are written in reverse order.

## Requirements:
1. **Python 3.x**: Ensure Python 3.x is installed.
2. **External Libraries**:
   - `requests`: For making HTTP requests to the URL.
   - `beautifulsoup4`: For parsing the HTML content of the webpage.
   - Install the necessary libraries using:
   ```bash
   pip install requests beautifulsoup4
   ```

## Process:

### 1. **URL and HTTP Request**:
   - The URL of the webpage containing the list of top 100 movies is set to an archived Empire page.
   - A GET request is made to fetch the webpage content using the `requests.get()` method.

### 2. **Parsing HTML with BeautifulSoup**:
   - The `response.text` is passed into BeautifulSoup to parse the HTML content of the webpage.
   - The `BeautifulSoup` object is used to extract data from the HTML.

### 3. **Extract Movie Titles**:
   - Using the `find_all()` method, the code locates all `<h3>` tags with the class `title`, which contain the movie titles.
   - The movie titles are retrieved using the `.get_text()` method and stored in a list.

### 4. **Write Movies to a File**:
   - Open the file `movies.txt` in append mode (`'a'`).
   - Loop through the list of movies in reverse order (from 100th to 1st) and write each movie title to the file.
   - A newline character (`\n`) is added after each movie title.

### 5. **File Output**:
   - The script will create or append to `movies.txt` in the same directory as the script. The movie titles are written in reverse order (from 100th to 1st).

## Steps to Set Up:

1. **Install Dependencies**:
   - Ensure that Python 3.x is installed on your system.
   - Install the required libraries by running:
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Run the Script**:
   - Execute the Python script in a Python environment.
   - The movie titles will be saved in the `movies.txt` file in the current working directory.

3. **Check the Output**:
   - Open the `movies.txt` file to view the movie titles listed in reverse order, from 100th to 1st.

## Expected Output:
- A file named `movies.txt` will be created (or appended to if it already exists) in the directory where the script is executed.
- The file will contain the top 100 movies from the Empire website, listed from the 100th movie to the 1st movie.

## Troubleshooting:
- **Library Installation**: If you encounter any issues installing the libraries, ensure that you are using the correct version of Python and that `pip` is up-to-date.
- **Network Issues**: If the webpage cannot be fetched due to network issues, check your internet connection or try accessing the URL in a browser to confirm it's available.
- **HTML Structure Changes**: If the structure of the webpage changes, the code may need to be updated to reflect changes in the tags or class names used to identify the movie titles.

## Notes:
- The script uses an archived version of the Empire website. If the URL becomes unavailable, the script will need to be updated with a valid URL.
- Ensure that web scraping is done ethically and follows the terms of service of the website being scraped.

```
