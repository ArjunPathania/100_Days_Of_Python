# Task.md

## Project: Quiz Application

### **Objective**
Build a Python-based quiz application that retrieves questions from an external source, presents them to the user in a graphical user interface (GUI), and tracks their progress.

---

### **Modules and Components**

1. **`question_model.py`**  
   - Defines the `Question` class.
   - Attributes:
     - `text`: Stores the question text.
     - `answer`: Stores the correct answer.

2. **`data.py`**  
   - Contains the `QuestionBank` class.
   - Retrieves question data, either from a local file or an API.
   - Converts raw question data into a format suitable for the `Question` class.

3. **`quiz_brain.py`**  
   - Manages the quiz logic.
   - Functions:
     - `next_question`: Fetches the next question.
     - `check_answer`: Verifies the user's answer.
     - `still_has_questions`: Checks if there are more questions to ask.

4. **`ui.py`**  
   - Manages the user interface using a GUI framework (e.g., Tkinter).
   - Displays questions, tracks user responses, and updates the score.

---

### **Implementation Workflow**

1. **Fetch Question Data**
   - Use the `QuestionBank` class to retrieve and parse question data.
   - Convert the data into `Question` objects and store them in `question_bank`.

2. **Initialize Quiz Logic**
   - Create an instance of `QuizBrain` with `question_bank`.

3. **Build the GUI**
   - Use `QuizInterface` to handle user interactions:
     - Display questions.
     - Process user input.
     - Show results at the end of the quiz.

4. **Run the Application**
   - Integrate all components to provide a seamless quiz experience.

---

### **Task Breakdown**

#### **`question_model.py`**
- [ ] Create a `Question` class.
- [ ] Implement attributes for `text` and `answer`.

#### **`data.py`**
- [ ] Create a `QuestionBank` class.
- [ ] Add functionality to fetch question data from an API or file.
- [ ] Format the data for the quiz.

#### **`quiz_brain.py`**
- [ ] Implement quiz logic to manage question flow and scoring.
- [ ] Add methods to check user answers and track progress.

#### **`ui.py`**
- [ ] Design the GUI for displaying questions and options.
- [ ] Add buttons for user interactions.
- [ ] Update the GUI based on quiz progress.

#### **Main Script**
- [ ] Combine all modules.
- [ ] Ensure smooth data flow between components.

---

### **Future Enhancements**
- Add a timer for each question.
- Include different difficulty levels.
- Save user progress and high scores.
- Provide feedback on incorrect answers.