def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(per):
    if per >= 75:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 50:
        return "C"
    elif per >= 35:
        return "D"
    else:
        return "Fail"