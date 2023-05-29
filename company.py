# Вывести названия всех отделов
def print_departments_titles(departments_list):
    print('Our company has following departments:')
    for department in departments_list:
        print(f"• {department['title']}")


# Вывести имена всех сотрудников компании
# Вывести имена всех сотрудников компании с указанием отдела, в котором они работают
def print_all_employees(departments_list, with_department=False):
    print("There's list of our company employees:")
    for department in departments_list:
        for employee in department['employers']:
            full_name = f"{employee['first_name']} {employee['last_name']}"
            print(f"• {full_name} ({department['title']})")
            if with_department:
                print(f"• {full_name} ({department['title']})")
            else:    
                print(f'• {full_name}')


# Вывести имена всех сотрудников компании, которые получают больше 100к
def print_100k_and_more_gainers(departments_list):
    print("Following employees' salary outnumber 100 000 rubles:")
    for department in departments_list:
        for employee in department['employers']:
            if employee['salary_rub'] >= 100000:
                print(f"• {employee['first_name']} {employee['last_name']}")


# Вывести позиции, на которых люди получают меньше 80к (можно с повторениями)
def print_positions_with_salary_below_80k(departments_list):
    handled_positions = []
    print('Following postions are offering salary below 80 000 rubles:')
    for department in departments_list:
        for employee in department['employers']:
            salary = employee['salary_rub']
            position = employee['position']
            if salary < 80000 and position not in handled_positions:
                handled_positions.append(position)
                print(f"• {position}")


# Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
def print_departments_requirements(departments_list):
    print("Our departments' requirements:")  
    for department in departments_list:
        employees = department['employers']
        requirement = sum([employee['salary_rub'] for employee in employees])
        print(f"• {department['title']}: {requirement}")        


def main():
    departments = [
        {
            "title": "HR department",
            "employers": [
                {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
                {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
                {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
                {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
            ]
        },
        {
            "title": "IT department",
            "employers": [
                {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
                {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
                {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
                {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
            ]
        },
    ]
    taxes = [
        {"department": None, "name": "vat", "value_percents": 13},
        {"department": "IT Department", "name": "hiring", "value_percents": 6},
        {"department": "BizDev Department", "name": "sales", "value_percents": 20},
    ]
    print_departments_titles(departments)
    print()
    print_all_employees(departments)
    print()
    print_all_employees(departments, True)
    print()
    print_100k_and_more_gainers(departments)
    print()
    print_positions_with_salary_below_80k(departments)
    print()
    print_departments_requirements(departments)


if __name__ == '__main__':
    main()
