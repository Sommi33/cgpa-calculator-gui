import tkinter as tk
from tkinter import ttk, messagebox

class GradeCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Grade Calculation Tool')

        self.courses_list = []
        self.grades_list = []

        self.selected_grade_system = tk.StringVar()
        self.selected_grade_system.set('A-F')

        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.master, padding='20')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.create_course_input_section(main_frame)
        self.create_separator(main_frame)
        self.create_grades_display_section(main_frame)
        self.create_gpa_cgpa_section(main_frame)

    def create_course_input_section(self, parent_frame):
        ttk.Label(parent_frame, text='Course Title:').grid(row=0, column=0, sticky=tk.W)
        self.course_title_entry = ttk.Entry(parent_frame)
        self.course_title_entry.grid(row=0, column=1)

        ttk.Label(parent_frame, text='Course Units:').grid(row=1, column=0, sticky=tk.W)
        self.course_units_entry = ttk.Entry(parent_frame)
        self.course_units_entry.grid(row=1, column=1)

        ttk.Label(parent_frame, text='Course Score:').grid(row=2, column=0, sticky=tk.W)
        self.course_score_entry = ttk.Entry(parent_frame)
        self.course_score_entry.grid(row=2, column=1)

        ttk.Label(parent_frame, text='Grade System:').grid(row=3, column=0, sticky=tk.W)
        grade_systems = ['A-F', 'Numeric']
        self.grade_system_combobox = ttk.Combobox(parent_frame, values=grade_systems, state="readonly", textvariable=self.selected_grade_system)
        self.grade_system_combobox.set('A-F')
        self.grade_system_combobox.grid(row=3, column=1)

        ttk.Button(parent_frame, text='Calculate', command=self.calculate_and_add_course).grid(row=4, column=0, columnspan=2, pady=10)

    def create_separator(self, parent_frame):
        ttk.Separator(parent_frame, orient='horizontal').grid(row=5, column=0, columnspan=2, sticky='ew', pady=10)

    def create_grades_display_section(self, parent_frame):
        ttk.Label(parent_frame, text='Course Grades:').grid(row=6, column=0, sticky=tk.W)
        self.grades_treeview = ttk.Treeview(parent_frame, columns=('Course', 'Grade', 'Points'))
        self.grades_treeview.grid(row=7, column=0, columnspan=2)

    def create_gpa_cgpa_section(self, parent_frame):
        self.gpa_label = ttk.Label(parent_frame, text='GPA: 0.00')
        self.gpa_label.grid(row=8, column=0, sticky=tk.W)
        self.cgpa_label = ttk.Label(parent_frame, text='CGPA: 0.00')
        self.cgpa_label.grid(row=9, column=0, sticky=tk.W)

    def calculate_and_add_course(self):
        try:
            course_name = self.course_title_entry.get()
            course_credits = int(self.course_units_entry.get())
            course_score = float(self.course_score_entry.get())

            if not (0 <= course_score <= 100):
                messagebox.showerror("Error", "Course score should be between 0 and 100.")
                return

            letter_grade, grade_point = self.calculate_grade(course_score)
            self.grades_treeview.insert('', 'end', values=(course_name, f'{letter_grade} ({grade_point} points)'))
            self.courses_list.append((course_name, course_credits, letter_grade, grade_point))

            self.update_gpa_and_cgpa()

            self.course_title_entry.delete(0, tk.END)
            self.course_units_entry.delete(0, tk.END)
            self.course_score_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    def calculate_grade(self, score):
        if self.selected_grade_system.get() == 'A-F':
            if score >= 90:
                return 'A', 4.0
            elif score >= 80:
                return 'B', 3.0
            elif score >= 70:
                return 'C', 2.0
            elif score >= 60:
                return 'D', 1.0
            else:
                return 'F', 0.0
        elif self.selected_grade_system.get() == 'Numeric':
            # Implement numeric grade logic here
            pass

    def update_gpa_and_cgpa(self):
        total_gpa = sum([course[3] for course in self.courses_list])
        total_courses = len(self.courses_list)
        cgpa = total_gpa / total_courses if total_courses > 0 else 0

        self.gpa_label.config(text=f'GPA: {total_gpa:.2f}')
        self.cgpa_label.config(text=f'CGPA: {cgpa:.2f}')

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculatorApp(root)
    root.mainloop()
