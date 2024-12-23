# Name Card Project

## Overview
This project involves creating a professional and visually appealing portfolio webpage using **HTML**, **CSS**, and **Bootstrap**. The name card serves as a digital introduction, showcasing skills, expertise, and contact information in an interactive format.

---

## Objectives
1. Create a structured HTML page to display portfolio information.
2. Style the page with **CSS** for a modern and professional look.
3. Use external fonts and icons for better aesthetics.
4. Add interactivity and responsiveness for enhanced user experience.

---

## Requirements
- Basic knowledge of **HTML** and **CSS**.
- Understanding of linking static files such as images, stylesheets, and icons.
- A working Python/Flask setup (optional for serving static files).

---

## Steps to Complete the Project

### 1. **Setup the Environment**
   - Create a folder structure:
     ```
     /static
         /css
             styles.css
         /images
             favicon.ico
             cloud.png
             mountain.png
             ProfilePhoto.jpg
             graph.gif
     /templates
         index.html
     ```
   - Place the `index.html` inside the `/templates` folder and all static files in their respective directories.

### 2. **Create the HTML Structure**
   - Use semantic tags for better accessibility and readability.
   - Include sections for:
     - Header with a **welcome message**.
     - Profile and introduction.
     - Skills section with descriptions and visuals.
     - Contact section with a **call-to-action button**.

### 3. **Add Styles with CSS**
   - Use **Google Fonts** for typography:
     - `Merriweather`, `Montserrat`, and `Sacramento`.
   - Customize the page's colors, layout, and font sizes.
   - Add background images and align content using **CSS flexbox**.

### 4. **Use External Resources**
   - Link **favicon.ico** for the page icon.
   - Include external libraries:
     - **Bootstrap** for responsive design.
     - **Font Awesome** or other resources for icons.

### 5. **Add Animations**
   - Use `.gif` files or animated SVGs for dynamic visuals.
   - Examples:
     - A coding GIF in the skills section.
     - Animated graphs for data visualization.

### 6. **Contact Section**
   - Provide a **call-to-action** button linking to an email address.
   - Include links to professional profiles:
     - LinkedIn
     - GitHub
     - Twitter (or X)

### 7. **Footer**
   - Add footer links for external profiles.
   - Include a copyright notice.

---

## Bonus Features
- Make the site responsive using **media queries** in CSS.
- Host the page on a platform like GitHub Pages or Netlify.
- Use Flask to serve the page with dynamic routing.

---

## Expected Output
- A single-page portfolio site with a **modern layout**, **clean typography**, and **easy navigation**.
- A visually appealing contact button and professional footer.

---

## Challenges
- Ensuring responsiveness for different screen sizes.
- Optimizing images and GIFs for faster loading times.
- Handling font or file loading issues.

---

## Next Steps
- Add JavaScript for interactivity.
- Build a back-end to process form submissions or dynamically load data.
