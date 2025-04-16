
---

```markdown
# 📡 Text to Morse Code Converter

This is a simple Python project that takes input text and converts it into **Morse code**, with the added feature of **playing audio beeps** for each dot and dash.

---

## 🔍 Features

- 🔤 Converts alphabets, digits, and a few special characters into Morse code
- 🔊 Plays beep sounds corresponding to Morse symbols
- 🧼 Ignores unsupported characters gracefully
- 💬 Command-line interface for easy interaction

---

## 🖥️ How to Use

1. Clone or download this repo to your local machine.
2. Open a terminal and navigate to the project folder:
   ```bash
   cd ~/Python100/Day_82/
   ```
3. Run the script:
   ```bash
   python3 textToMorseCode.py
   ```
4. Enter the text you want to convert when prompted. The Morse code will be printed and played as audio.

---

## 📁 File Structure

```
📂 Day_82/
├── textToMorseCode.py   # Main script
├── long.mp3             # Sound file used for long Morse beeps
├── short.mp3             # Sound file used for short Morse beeps
└── README.md            # This file
```

---

## 📦 Dependencies

### Required Python Package:

- `playsound`
  ```bash
  pip install playsound
  ```

> If you get warnings like:
> ```
> playsound is relying on another python subprocess.
> Please use `pip install pygobject`...
> ```
> You can safely ignore them, or install the suggested dependencies.

### Optional Troubleshooting:
If you face errors while installing or using audio libraries:

- Try using the `simpleaudio` or `pygame` library.
- Ensure you have development libraries:
  ```bash
  sudo apt install libasound2-dev
  ```

---

## ⚙️ Customization

- Replace the default `long.mp3` with any short beep sound of your choice.
- Adjust the timing between dots and dashes by modifying `time.sleep()` durations in the code.

---

## 💡 Learnings

- Dictionary mapping & character translation
- Audio playback in Python
- Terminal-based interaction
- Error handling and clean user input

---

## 👤 Author

**Arjun Pathania**  
🧠 Passionate about Python, problem solving, and building cool stuff.

---

## 📬 Contributions & Feedback

Feel free to fork, improve, or open an issue if you'd like to contribute or suggest improvements!

---

## 🧭 License

This project is open-source and free to use for learning and personal development.

```
---