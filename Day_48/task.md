
```markdown
# Selenium Cookie Clicker Bot Task

## Task Description
This script automates playing the Cookie Clicker game using Selenium WebDriver. It clicks the cookie to generate cookies and purchases the most expensive affordable upgrade every 5 seconds, stopping after 5 minutes to check the cookies per second (CPS) count.

## Steps to Execute

1. **Initialize WebDriver**:
   - A Chrome WebDriver is initialized with options to keep the browser open after the script finishes.

2. **Navigate to Cookie Clicker Game**:
   - The script opens the Cookie Clicker game page (`https://orteil.dashnet.org/experiments/cookie/`).

3. **Click the Cookie**:
   - The script clicks the cookie to accumulate cookies.

4. **Every 5 Seconds**:
   - The script checks the prices of available upgrades.
   - Extracts the prices and identifies the most expensive affordable upgrade.
   - Purchases the most expensive upgrade that the player can afford.

5. **After 5 Minutes**:
   - After 5 minutes of gameplay, the script stops and prints the cookies per second (CPS) rate.

## Requirements

- `selenium`: For automating the browser and interacting with the game.
- `time`: For managing time-based actions in the game.

## Example Output

- Every 5 seconds, the script will print the most expensive affordable upgrade's price.
- After 5 minutes, it will print the cookies per second (CPS) count.

Example:
```
4500
12500
20000
CPS: 2500
```

## Notes

- Make sure the Selenium WebDriver is installed and configured properly on your machine.
- The game URL is hardcoded as `https://orteil.dashnet.org/experiments/cookie/`, but you can change it if necessary.
- The bot automatically purchases upgrades as long as the player has enough cookies.

## Improvements

- You can modify the script to continue playing indefinitely or for a different duration.
- Add a feature to track and log the player's progress over time (e.g., total cookies, upgrades purchased).
```