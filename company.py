import statistics


def merge_all_departments_employees(departments_list):
    employees_list = []
    for department in departments_list:
        for employee in department['employers']:
            employees_list.append(employee)
    return employees_list


# Вывести названия всех отделов
def print_departments_titles(departments_list):
    print('The company has following departments:')
    for department in departments_list:
        print(f"• {department['title']}")


# Вывести имена всех сотрудников компании
# Вывести имена всех сотрудников компании с указанием отдела, в котором они работают
def print_all_employees(departments_list, with_department=False):
    print("There's list of the company employees:")
    for department in departments_list:
        for employee in department['employers']:
            full_name = f"{employee['first_name']} {employee['last_name']}"
            if with_department:
                print(f"• {full_name} ({department['title']})")
            else:    
                print(f'• {full_name}')


# Вывести имена всех сотрудников компании, которые получают больше 100к
def print_adjusted_sum_and_more_gainers(departments_list, adjusted_salary):
    print(f"Following employees' salary outnumber {adjusted_salary} rubles:")
    employees_list = merge_all_departments_employees(departments_list)
    for employee in employees_list:
        if employee['salary_rub'] >= adjusted_salary:
            print(f"• {employee['first_name']} {employee['last_name']}")


# Вывести позиции, на которых люди получают меньше 80к (можно с повторениями)
# Вывести названия должностей, которые получают больше 90к без повторений
def print_positions_with_specific_salary(departments_list, adjusted_salary, min_or_max):
    employees_list = merge_all_departments_employees(departments_list)
    handled_positions = []
    if min_or_max == min:
        adjective = 'below'
    else:
        adjective = 'above'        
    print(f'Following postions are offering salary {adjective} {adjusted_salary} rubles:')
    for employee in employees_list:
        salary = employee['salary_rub']
        position = employee['position']
        if salary == min_or_max(salary, adjusted_salary) and salary != adjusted_salary:
            if position not in handled_positions: 
                handled_positions.append(position)
                print(f"• {position}")


# Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
def print_departments_requirements(departments_list):
    print("Departments' requirements:")  
    for department in departments_list:
        employees = department['employers']
        requirement = sum([employee['salary_rub'] for employee in employees])
        print(f"• {department['title']}: {requirement} rubles")


# Вывести названия отделов с указанием минимальной зарплаты в нём
def print_minimal_salary_in_departments(departments_list):
    print('Minimal salary in every department:')
    for department in departments_list:
        minimal_salary = min([employee['salary_rub'] for employee in department['employers']])
        print(f"• {department['title']}: {minimal_salary} rubles")


# Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём
def salary_indicators_in_departments(departments_list):
    salary_indicators = []
    for department in departments_list:
        minimal_salary = min([employee['salary_rub'] for employee in department['employers']])
        average_salary = statistics.mean([employee['salary_rub'] for employee in department['employers']])
        median_salary = statistics.median([employee['salary_rub'] for employee in department['employers']])
        maximal_salary = max([employee['salary_rub'] for employee in department['employers']])
        salary_indicators.append(
            {
                'department' : department['title'],
                'minimal salary' : minimal_salary,
                'average salary' : average_salary,
                'median salary' : int(median_salary),
                'maximal salary': maximal_salary,
            }
        )
    return salary_indicators
    

def print_salary_indicators(departments_list):
    salary_indicators = salary_indicators_in_departments(departments_list)
    for department_indicators in salary_indicators:
        print(f"Salary indicators for {department_indicators['department']}:")
        print(f"• Minimal salary: {department_indicators['minimal salary']} rubles")
        print(f"• Average salary: {department_indicators['average salary']} rubles")
        print(f"• Median salary: {department_indicators['median salary']} rubles")
        print(f"• Maximal salary: {department_indicators['maximal salary']} rubles")
        print()


# Вывести среднюю зарплату по всей компании
def average_salary(departments_list):
    employees_list = merge_all_departments_employees(departments_list)
    salaries_sum = sum([employee['salary_rub'] for employee in employees_list])
    headcount = len(employees_list)
    return salaries_sum // headcount


# Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин)
def print_average_salary_among_women(departments_list, female_names):
    print('Women average salary in every department of the company:')
    for department in departments_list:
        salaries_sum, headcount = 0, 0
        for employee in department['employers']:
            if employee['first_name'] in female_names:
                salaries_sum += employee['salary_rub']
                headcount += 1
        if headcount == 0:
            print(f"• There's no women in {department['title']}")
        else:
            average_salary = salaries_sum // headcount
            print(f"• {department['title']}: {average_salary} rubles")
    

# Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву
def vowel_ending_last_names_bearers(departments_list):
    employees_list = merge_all_departments_employees(departments_list)
    vowels = ('a', 'e', 'i', 'o', 'u', 'w', 'y')
    vowel_enders = set()
    for employee in employees_list:
        if employee['last_name'][-1] in vowels:
            vowel_enders.add(employee['first_name'])
    return vowel_enders


def print_vowel_ending_last_name_bearers_names(departments_list):
    vowel_enders = sorted(vowel_ending_last_names_bearers(departments_list))
    print('There are names of employees, whose last names end with a vovel:')
    for name in vowel_enders:
        print(f'• {name}')


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
    female_names = ('Nicole', 'Christina', 'Michelle', 'Caitlin')
    print_departments_titles(departments)
    print()
    print_all_employees(departments)
    print()
    print_all_employees(departments, True)
    print()
    print_adjusted_sum_and_more_gainers(departments, 100000)
    print()
    print_positions_with_specific_salary(departments, 80000, min)
    print()
    print_departments_requirements(departments)
    print()
    print_minimal_salary_in_departments(departments)
    print()
    print_salary_indicators(departments)
    print(f'Average salary in the company: {average_salary(departments)} rubles')
    print()
    print_positions_with_specific_salary(departments, 90000, max)
    print()
    print_average_salary_among_women(departments, female_names)
    print()
    print_vowel_ending_last_name_bearers_names(departments)


if __name__ == '__main__':
    main()
