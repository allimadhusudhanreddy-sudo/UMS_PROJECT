# University Management System
# OOPs, Functions, list comprehension, Git & Github, Cloud

# to build the frontend
import streamlit as st

# app front page configuration
st.set_page_config(
    page_title = "UMS portal",
    layout = "wide"
)

st.title("University Management System")

# create a empty list to store list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

# side bar
menu_choice = st.sidebar.radio(
    "SELECT ACTION",
    (
        "Create College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teachers",
        "List College"
    )
)
# This class will add new student and teacher in a college
class college:
    def __init__(self, cname):
        self.cname = cname  # storing name of college
        self.students = []  # list of student objects
        self.teachers = []  # list of teacher objects

    def add_student(self, s):  # adding new student in the student list
        self.students.append(s)
    def add_teacher(self, t):  # New teacher will be added into teacher list
        self.teachers.append(t)

class person:
    def __init__(self, branch, name):
        self.branch = branch
        self.name = name

class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(branch, name)
        self.rollno = rollno

class teacher(person):
    def __init__(self, branch, name, subject):
        super().__init__(branch, name)
        self.subject = subject

# finding and returning the college which student selected
def find_college(cname):
    return next((c for c in st.session_state.colleges if c.cname == cname), None)
# Create a New college
if menu_choice == "Create College":
    cname = st.text_input("Enter New College Name")
    if st.button("CREATE"):
        st.session_state.colleges.append(college(cname))
        st.success(f"{cname} created successfully")

elif menu_choice == "Add Student":
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        roll = st.text_input("Enter your Roll Number")
        sname = st.text_input("Enter Student Name")
        branch = st.text_input("Enter the branch")
        if st.button("ADD STUDENT"):
            if not(roll and sname and branch and clgname):
                st.error("Please Enter all the details")
            else:
                clg = find_college(clgname)
                clg.add_student(student(roll, sname, branch))
                st.success("Student added successfully")

elif menu_choice == "Add Teacher":
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        subject = st.text_input("Enter your subject")
        tname = st.text_input("Enter teacher Name")
        branch = st.text_input("Enter the branch")
        if st.button("ADD TEACHER"):
            if not(subject and tname and branch and clgname):
                st.error("Please Enter all the details")
            else:
                clg = find_college(clgname)
                clg.add_teacher(teacher(branch, tname, subject))
                st.success("teacher added successfully")

elif menu_choice == "Display Students":
    clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
    clg = find_college(clgname)
    st.subheader(f"List of Students in {clgname}")
    if clg.students:
        for i, s in enumerate(clg.students,1):
            st.write(f"{i} : {s.name}")
    else:
        st.warning("No Student found")

elif menu_choice == "Display Teachers":
    clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
    clg = find_college(clgname)
    st.subheader(f"List of Teachers in {clgname}")
    if clg.teachers:
        for i, t in enumerate(clg.teachers,1):
            st.write(f"{i} : {t.name}")
    else:
        st.warning("No Teacher found") 

elif menu_choice == "List College":
    if not st.session_state.colleges:
            st.info("Please insert a college first")
    else:
        for i, c in enumerate(st.session_state.colleges,1):
            st.write(f"{i} : {c.cname}")