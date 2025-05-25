# cgpa-calculator-gui

# Grade Calculation Tool

A desktop application built with Python and Tkinter for calculating student grades, GPA, and CGPA. This tool allows students and educators to input course information and automatically calculate cumulative grade point averages.

## Features

- **Course Management**: Add multiple courses with titles, units/credits, and scores
- **Grade Systems**: Support for A-F letter grades and numeric grading systems
- **Automatic Calculations**: Real-time GPA and CGPA computation
- **User-friendly Interface**: Clean, intuitive desktop GUI built with Tkinter
- **Input Validation**: Error handling for invalid inputs and score ranges
- **Grade Display**: Visual table showing all entered courses and their calculated grades

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python installation)

## Installation

1. Clone or download this repository
2. Ensure Python 3.6+ is installed on your system
3. No additional packages need to be installed (uses built-in libraries)

## Usage

1. Run the application:
   ```bash
   python Cgpa_Gui.py
   ```

2. **Adding a Course**:
   - Enter the course title
   - Input the number of course units/credits
   - Enter the course score (0-100)
   - Select the grading system (A-F or Numeric)
   - Click "Calculate" to add the course

3. **Viewing Results**:
   - Added courses appear in the table with calculated grades
   - GPA and CGPA are automatically updated after each course addition
   - All calculations are displayed in real-time

## Grading Scale (A-F System)

| Score Range | Letter Grade | Grade Points |
|-------------|--------------|--------------|
| 90-100      | A            | 4.0          |
| 80-89       | B            | 3.0          |
| 70-79       | C            | 2.0          |
| 60-69       | D            | 1.0          |
| 0-59        | F            | 0.0          |

## File Structure

```
├── Cgpa_Gui.py          # Main application file
└── README.md            # This file
```

## How It Works

The application calculates:
- **GPA**: Sum of all grade points from entered courses
- **CGPA**: Average grade points (total grade points ÷ number of courses)

Each course contributes to both calculations based on the grade points earned from the course score.

## Known Limitations

- Numeric grading system is not fully implemented
- Course units/credits are collected but not used in weighted calculations
- No data persistence (courses are lost when application closes)
- No option to edit or delete previously entered courses

## Future Enhancements

- Implement weighted GPA calculations using course units
- Add data saving/loading functionality
- Complete numeric grading system implementation
- Add course editing and deletion features
- Export results to PDF or Excel

## Contributing

Feel free to fork this project and submit pull requests for improvements. Some areas that could use enhancement:
- Better error handling
- Additional grading systems
- Data persistence features
- UI/UX improvements

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please create an issue in the repository or contact the developer.

---

**Note**: This tool is designed for educational purposes and basic grade calculation needs. For institutional use, please verify that the grading calculations meet your specific requirements.
