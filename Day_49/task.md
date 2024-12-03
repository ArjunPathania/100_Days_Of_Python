
```markdown
# LinkedIn Job Application Bot Task

## Task Description
This script automates the process of applying to jobs on LinkedIn. It logs into a LinkedIn account, navigates to a job listings page, and applies to jobs with a phone number provided. It skips complex applications and those without an application button.

## Steps to Execute

1. **Load Environment Variables**:
   - Use the `dotenv` package to load `EMAIL`, `PASSWORD`, and `PHONE` from an `.env` file.

2. **Initialize WebDriver**:
   - A Chrome WebDriver is initialized with options to keep the browser open after the script finishes.

3. **Navigate to LinkedIn Job Listings**:
   - The script opens a LinkedIn job search page with predefined job criteria.

4. **Reject Cookies**:
   - The script automatically rejects cookies pop-up.

5. **Sign In to LinkedIn**:
   - It clicks the "Sign in" button and logs into LinkedIn with the credentials loaded from the `.env` file.

6. **Solve CAPTCHA Manually**:
   - The script pauses and asks the user to manually solve the CAPTCHA.

7. **Extract Job Listings**:
   - The script extracts all the job listings available on the page.

8. **Apply for Jobs**:
   - For each job listing:
     - Click the job to open the details.
     - Click the "Apply" button.
     - Insert the phone number into the form if it is empty.
     - If the application is complex (requires extra information), it skips the listing and moves to the next one.
     - If the application can be submitted directly, the script submits it and closes the modal.

9. **Close Browser**:
   - After applying to the jobs, the browser is closed.

## Requirements

- `selenium`: For automating the browser and interacting with LinkedIn.
- `time`: For managing sleep intervals between actions.
- `os` and `dotenv`: For loading sensitive account information like email, password, and phone number from environment variables.

## Example Output

- The script prints out messages like:
  ```
  Opening Listing
  Submitting job application
  Complex application, skipped.
  No application button, skipped.
  ```
  
## Notes

- The script requires manual CAPTCHA solving, so the user must interact with the browser during that part of the process.
- Ensure that the necessary environment variables (`EMAIL`, `PASSWORD`, `PHONE`) are set in a `.env` file for smooth operation.
- The script is currently set up to apply to jobs in the "Python" field in London. You can adjust the URL to fit different job searches.
- The browser is kept open in case of script crashes, providing time to debug or manually intervene.

## Improvements

- Add more sophisticated handling for different application types.
- Add error logging or email notifications to track script progress and issues.
```