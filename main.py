from flet import *
import sqlite3

# Database connection and setup
conn = sqlite3.connect("dat.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stdname TEXT,
    stdmail TEXT,
    stdphone TEXT,
    stdaddress TEXT,
    stmathmatic INTEGER,
    starabic INTEGER,
    stfrance INTEGER,
    stenglish INTEGER,
    stdrawing INTEGER,
    stchemistry INTEGER
)
""")


# Function to add a student
def add_student(name, mail, phone, address, math, arabic, france, english, drawing, chemistry):
    try:
        cursor.execute("""
        INSERT INTO Student (stdname, stdmail, stdphone, stdaddress, stmathmatic, starabic, stfrance, stenglish, stdrawing, stchemistry)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, mail, phone, address, math, arabic, france, english, drawing, chemistry))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Function to get student count
def get_student_count():
    cursor.execute("SELECT COUNT(*) FROM Student")
    result = cursor.fetchone()
    return result[0]

# Function to calculate the average score of a student
def calculate_average(math, arabic, france, english, drawing, chemistry):
    total = math + arabic + france + english + drawing + chemistry
    return total / 6  # There are 6 subjects

# Function to show all students and their scores with averages
def show_students(page):
    cursor.execute("SELECT stdname, stdmail, stdphone, stdaddress, stmathmatic, starabic, stfrance, stenglish, stdrawing, stchemistry FROM Student")
    students = cursor.fetchall()

    student_list = ListView(expand=True, spacing=10, padding=10)
    
    for student in students:
        # Calculate the student's average score
        average = calculate_average(student[4], student[5], student[6], student[7], student[8], student[9])

        student_list.controls.append(
            Container(
                content=Column([
                    Text(f"Name: {student[0]}"),
                    Text(f"Email: {student[1]}"),
                    Text(f"Phone: {student[2]}"),
                    Text(f"Address: {student[3]}"),
                    Text(f"Math: {student[4]}, Arabic: {student[5]}, French: {student[6]}"),
                    Text(f"English: {student[7]}, Drawing: {student[8]}, Chemistry: {student[9]}"),
                    Text(f"Average: {average:.2f}", weight="bold", color="green")  # Display the average
                ], spacing=5),
                border=border.all(1, colors.BLACK),
                border_radius=10,
                padding=10,
                margin=5
            )
        )

    # Add the student list to the bottom of the page
# Function to calculate the average score of a student
def calculate_average(math, arabic, france, english, drawing, chemistry):
    total = math + arabic + france + english + drawing + chemistry
    return total / 6  # There are 6 subjects

# Function to show all students and their scores with averages
def show_students(page):
    cursor.execute("SELECT stdname, stdmail, stdphone, stdaddress, stmathmatic, starabic, stfrance, stenglish, stdrawing, stchemistry FROM Student")
    students = cursor.fetchall()

    student_list = ListView(expand=True, spacing=10, padding=10)
    
    for student in students:
        # Calculate the student's average score
        average = calculate_average(student[4], student[5], student[6], student[7], student[8], student[9])

        # Determine the color of the average based on pass/fail criteria
        if average < 10:
            average_color = "red"  # Fail: red color
        else:
            average_color = "green"  # Pass: green color

        student_list.controls.append(
            Container(
                content=Column([
                    Text(f"Name: {student[0]}"),
                    Text(f"Email: {student[1]}"),
                    Text(f"Phone: {student[2]}"),
                    Text(f"Address: {student[3]}"),
                    Text(f"Math: {student[4]}, Arabic: {student[5]}, French: {student[6]}"),
                    Text(f"English: {student[7]}, Drawing: {student[8]}, Chemistry: {student[9]}"),
                    # Display the average with the appropriate color
                    Text(f"Average: {average:.2f}", weight="bold", color=average_color)
                ], spacing=5),
                border=border.all(1, colors.BLACK),
                border_radius=10,
                padding=10,
                margin=5
            )
        )

    # Add the student list to the bottom of the page
 # Function to calculate the average score of a student
def calculate_average(math, arabic, france, english, drawing, chemistry):
    total = math + arabic + france + english + drawing + chemistry
    return total / 6  # There are 6 subjects

# Function to show all students and their scores with averages
def show_students(page):
    cursor.execute("SELECT stdname, stdmail, stdphone, stdaddress, stmathmatic, starabic, stfrance, stenglish, stdrawing, stchemistry FROM Student")
    students = cursor.fetchall()

    student_list = ListView(expand=True, spacing=10, padding=10)
    
    for student in students:
        # Calculate the student's average score
        average = calculate_average(student[4], student[5], student[6], student[7], student[8], student[9])

        # Determine the color of the average based on pass/fail criteria
        if average < 10:
            average_color = "red"  # Fail: red color
        else:
            average_color = "green"  # Pass: green color

        student_list.controls.append(
            Container(
                content=Column([
                    Text(f"Name: {student[0]}"),
                    Text(f"Email: {student[1]}"),
                    Text(f"Phone: {student[2]}"),
                    Text(f"Address: {student[3]}"),
                    Text(f"Math: {student[4]}, Arabic: {student[5]}, French: {student[6]}"),
                    Text(f"English: {student[7]}, Drawing: {student[8]}, Chemistry: {student[9]}"),
                    # Display the average with the appropriate color
                    Text(f"Average: {average:.2f}", weight="bold", color=average_color)
                ], spacing=5),
                border=border.all(1, colors.BLACK),
                border_radius=10,
                padding=10,
                margin=5
            )
        )

    # Add the student list to the bottom of the page
    page.add(
        Container(
            content=student_list,
            height=300,  # Adjust height based on how many students you want to show
            border=border.all(1, colors.GREY),
            border_radius=10,
            padding=10
        )
    )
    page.update()
    page.update()


# Main UI function
def main(page: Page):
    page.title = "علامات التلميد"
    page.scroll = 'auto'
    page.window.left = 50
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

    # Input fields
    tname = TextField(label='اسم المستخدم', icon=icons.PERSON, rtl=True, height=30)
    tmail = TextField(label='اميل المستخدم', icon=icons.MAIL, rtl=True, height=30)
    tphone = TextField(label='رقم الهاتف', icon=icons.PHONE, rtl=True, height=30)
    taddress = TextField(label='الموقع الجغرافي', icon=icons.LOCATION_CITY, rtl=True, height=38)
    mathmatic = TextField(label='الرياضيات', width=110, rtl=True, height=38)
    english = TextField(label='الانجلزية', width=110, rtl=True, height=38)
    arabic = TextField(label='العربية', width=110, rtl=True, height=38)
    fronces = TextField(label='الفرنسية', width=110, rtl=True, height=38)
    music = TextField(label='موسيقى', width=110, rtl=True, height=38)
    chimic = TextField(label='الكمياء', width=110, rtl=True, height=38)

    # Add student function
    def on_add_student(e):
        if all([tname.value, tmail.value, tphone.value, taddress.value, mathmatic.value, arabic.value, fronces.value, english.value, music.value, chimic.value]):
            add_student(tname.value, tmail.value, tphone.value, taddress.value, mathmatic.value, arabic.value, fronces.value, english.value, music.value, chimic.value)
            page.snack_bar = SnackBar(Text("تم إضافة الطالب بنجاح!"))
            page.snack_bar.open = True
        else:
            page.snack_bar = SnackBar(Text("يرجى ملء جميع الحقول!"))
            page.snack_bar.open = True
        page.update()

    # Buttons
    addbuttn = ElevatedButton(
        text="جديدطالب اضافة",
        width=170,
        style=ButtonStyle(
            bgcolor=colors.BLUE,
            color=colors.WHITE,
            padding=15
        ),
        on_click=on_add_student
    )

    showbuttn = ElevatedButton(
        text="عرض كل الطلاب",
        width=170,
        style=ButtonStyle(
            bgcolor=colors.BLUE,
            color=colors.WHITE,
            padding=15
        ),
        on_click=lambda e: show_students(page)  # Update to call show_students
    )

    student_count = get_student_count()

    # Main UI layout
    page.add(
        Row([Image(src="student.jpg", width=200)], alignment=MainAxisAlignment.CENTER),
        Row([Text("تطبيق الطالب", size=20, font_family="Arial", color='black',bgcolor='yello')], alignment=MainAxisAlignment.CENTER),
        Row([Text("عدد الطلاب المسجلين : ", size=20, font_family="Arial", color='blue'), Text(str(student_count), size=20, font_family="Arial", color='black')], alignment=MainAxisAlignment.CENTER, rtl=True),
        tname,
        tmail,
        tphone,
        taddress,
        Row([Text("علامات التلميد", text_align='center', weight='bold')], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([arabic, mathmatic], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([english, fronces], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([chimic, music], alignment=MainAxisAlignment.CENTER, rtl=True),
        Row([addbuttn, showbuttn], alignment=MainAxisAlignment.CENTER, rtl=True),
    )

    page.update()

# Start the app
app(main)
