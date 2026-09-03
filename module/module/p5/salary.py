def gross_salary(basic, allowance):
    return basic + allowance


def deductions(gross):
    return gross * 0.10


def net_salary(gross, deduction):
    return gross - deduction