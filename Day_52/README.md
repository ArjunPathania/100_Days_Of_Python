---

# Instagram Follower Bot

This Instagram Follower Bot automates the process of logging into Instagram, finding followers from a similar account, and following them, while mimicking human-like behavior to avoid detection.

---

## **Project Setup**

### **1. Prerequisites**
Before running the bot, ensure you have the following installed:
- Python 3.6 or higher
- Google Chrome browser
- ChromeDriver (compatible with your version of Chrome)
- Virtual environment (optional but recommended)

### **2. Install Dependencies**
Clone the repository and install the required Python dependencies:

```bash
git clone https://github.com/yourusername/insta-follower-bot.git
cd insta-follower-bot
pip install -r requirements.txt
```

Or, install individual dependencies with:

```bash
pip install selenium python-dotenv
```

### **3. Set Up `.env` File**
Create a `.env` file in the root of the project directory with the following content:

```env
USERNAME=your_instagram_username
PASSWORD=your_instagram_password
SIMILAR_ACCOUNT=target_account_name
```

Replace `your_instagram_username`, `your_instagram_password`, and `target_account_name` with your Instagram credentials and the account whose followers you want to target.

---

## **How It Works**

The bot automates the following steps:

1. **Login**: Logs into Instagram using the credentials provided in the `.env` file.
2. **Find Followers**: Searches for the target account, navigates to its followers list, and scrolls through the list to load more users.
3. **Follow Users**: Clicks the "Follow" button on users in the followers list, mimicking human behavior by introducing random delays between actions.
4. **Handle Interceptions**: If the "Follow" button is intercepted (e.g., by a pop-up), the bot automatically clicks the "OK" button to dismiss it and retry the action.

---

## **Running the Bot**

### **1. Start the Bot**
To run the bot, execute the following command in your terminal:

```bash
python instaFollowerBot.py
```

The bot will:
- Log into Instagram
- Navigate to the target account's followers list
- Follow users by clicking the "Follow" button
- Scroll through the followers list and repeat the process

### **2. Stop the Bot**
You can stop the bot at any time by interrupting the process in your terminal (usually with `Ctrl + C`).

---

## **Error Handling**

- **Pop-up Interception**: If the "Follow" button click is blocked by an overlay or pop-up, the bot will automatically click the "OK" button to dismiss the pop-up and continue.
- **Timeout or Missing Elements**: The bot includes handling for timeouts and missing elements, and will print helpful error messages if something goes wrong.

---

## **Project Structure**

```
/project-directory
│
├── .env                   # Environment variables (username, password, target account)
├── instaFollowerBot.py     # Main bot script
├── requirements.txt       # List of Python dependencies
├── README.md              # Project documentation
└── task.md                # Task overview and project details
```

---

## **Known Issues**

- **Instagram Restrictions**: Instagram may temporarily block actions (e.g., following too many accounts in a short time). This is normal behavior, and the bot should pause before attempting further actions.
- **Pop-up Issues**: Occasionally, the bot may encounter unexpected pop-ups. The bot tries to handle these by clicking the "OK" button.

---

## **Future Enhancements**

- **Proxy Support**: Implement proxy rotation to avoid IP bans and reduce the risk of Instagram detecting the bot.
- **Captcha Handling**: Add functionality to handle CAPTCHA challenges that may appear when Instagram suspects bot activity.
- **Scheduler**: Schedule the bot to run at specific times or intervals.
- **GUI**: Develop a graphical user interface for easier management of bot settings and controls.

---

## **Acknowledgments**

- **Selenium**: For automating web browsers.
- **Python-dotenv**: For securely managing environment variables.

---
