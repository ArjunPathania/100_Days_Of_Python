
---

# Task.md

## Task Overview
The objective is to create a GUI-based Pomodoro Timer that helps users manage their work sessions and breaks effectively. The application will alternate between work and break sessions, providing visual indicators for the current session, countdown timer, and check marks to track completed sessions.

### Task Breakdown

1. **Set Up Constants and Initial Values**:
   - Define colors for each session state (work, break, and reset).
   - Set work, short break, and long break durations in minutes.
   - Initialize a variable `reps` to track the number of sessions and `timer` to store the reference for the countdown.

2. **Timer Reset Function**:
   - Create a function `reset_timer()` to reset all UI components and session data.
   - Reset the `reps` count and cancel any active timer using `after_cancel`.
   - Reset the timer display, set the indicator text back to "Timer," and clear check marks for completed sessions.
   - Re-enable the start button to allow restarting the timer.

3. **Start Timer Function**:
   - Create a function `start_timer()` to initiate and alternate between work and break sessions.
   - Increment the `reps` counter to keep track of the current session.
   - Display the appropriate session type (work or break) and adjust the timer duration based on the session.
   - Display check marks for completed work sessions.

4. **Countdown Mechanism**:
   - Implement a `countdown()` function to update the timer display with remaining minutes and seconds.
   - Continue the countdown if time remains, or call `start_timer()` to initiate the next session once the timer reaches zero.

5. **User Interface Setup**:
   - Configure the main application window with padding, a title, and a background color.
   - Add labels for the timer indicator, check marks, and other session text elements.
   - Create a canvas with an image (e.g., a tomato) and overlay the timer text on the image.
   - Add start and reset buttons to initiate or reset the timer.

---
