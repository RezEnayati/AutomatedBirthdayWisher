**Birthday Wisher Program **

**Introduction:**
The Birthday Wisher Program is a Python script designed to automate the process of sending birthday wishes via email. With this program, you can send personalized birthday messages to individuals based on their birthday data stored in a CSV file.

**Features:**
1. **Automated Email Sending:** The program automatically sends birthday wishes via email to individuals whose birthdays match the current date.

2. **Customizable Messages:** You can customize the birthday messages by creating letter templates in text files. The program selects a random template and replaces placeholders with the recipient's name.

3. **SMTP Email Sending:** The program uses the Simple Mail Transfer Protocol (SMTP) to send emails, ensuring reliable delivery of birthday wishes.

4. **Error Handling:** The program handles file not found errors and SMTP exceptions gracefully, providing informative error messages when issues occur.

**Installation:**
1. Clone or download the Birthday Wisher Program repository from Github.
   
2. Ensure you have Python installed on your system.
   
3. Install the required dependencies by running `pip install pandas`.

**Usage:**
1. Prepare a CSV file named `birthdays.csv` containing birthday data. Each row should represent an individual with columns for name, email, month, and day of birth.

2. Create letter templates in text files (e.g., `letter_1.txt`, `letter_2.txt`, etc.) in a directory named `letter_templates`. Use `[NAME]` as a placeholder for the recipient's name in the templates.

3. Configure the email settings by providing your email address (`EMAIL`) and password (`PASSWORD`) in the Python script.

4. Run the Python script (`birthday_wisher.py`). The program will automatically send birthday wishes to recipients whose birthdays match the current date.

**Customization:**
- You can customize the subject of the birthday emails by modifying the `SUBJECT` variable in the Python script.
  
- Modify the letter templates to create personalized birthday messages for recipients.

**Contributing:**
The Birthday Wisher Program is an open-source project, and contributions are welcome! If you have ideas for features, improvements, or bug fixes, feel free to submit a pull request or open an issue on the GitHub repository.


**Enjoy automating your birthday wishes with the Birthday Wisher Program!**
