from pyscript import document

def calculate_gwa(grades):
    """
    Calculate General Weighted Average
    grades: dictionary with subject grades
    """
    # Subject units
    units = {
        'science': 5,
        'math': 5,
        'english': 5,
        'filipino': 3,
        'ict': 2,
        'pe': 1
    }
    
    # Calculate weighted sum
    weighted_sum = 0
    total_units = 0
    
    for subject, grade in grades.items():
        if subject in units:
            weighted_sum += grade * units[subject]
            total_units += units[subject]
    
    # Return average
    if total_units == 0:
        return 0
    return weighted_sum / total_units

def validate_grades(grades):
    """
    Validate grades are between 0 and 100
    """
    errors = []
    for subject, grade in grades.items():
        if grade < 0 or grade > 100:
            errors.append(f"{subject.capitalize()} must be between 0 and 100")
    return errors

def format_result(name, grades, gwa):
    """
    Format result like the screenshot
    """
    result = f"Name: {name}\n\n"
    result += f"Science: {grades.get('science', 0)}\n"
    result += f"Math: {grades.get('math', 0)}\n"
    result += f"English: {grades.get('english', 0)}\n"
    result += f"Filipino: {grades.get('filipino', 0)}\n"
    result += f"ICT: {grades.get('ict', 0)}\n"
    result += f"PE: {grades.get('pe', 0)}\n\n"
    result += f"Your general weighted average is {gwa:.2f}"
    return result

# Test function
def test_calculation():
    """Test with sample data"""
    test_data = {
        'science': 91,
        'math': 89,
        'english': 86,
        'filipino': 88,
        'ict': 89,
        'pe': 85
    }
    
    errors = validate_grades(test_data)
    if errors:
        return f"Validation errors: {errors}"
    
    gwa = calculate_gwa(test_data)
    return format_result("Josua Ortiz", test_data, gwa)