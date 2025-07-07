import sqlite3
from datetime import date
connection = sqlite3.connect("employee.db")
# creating cursor

cursor = connection.cursor()

# Drop table if exists for repeatability
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")

table_info = """
CREATE TABLE EMPLOYEE(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(50),
    DEPARTMENT VARCHAR(30),
    ROLE VARCHAR(30),
    EMAIL VARCHAR(50),
    SALARY INT,
    DATE_JOINED DATE
);
"""

cursor.execute(table_info)

# Inserting records (30+ realistic entries)
employees = [
    ("Alice Johnson", "Engineering", "Software Engineer", "alice.johnson@company.com", 95000, "2018-03-15"),
    ("Bob Smith", "Engineering", "DevOps Engineer", "bob.smith@company.com", 90000, "2019-07-22"),
    ("Carol Lee", "HR", "HR Manager", "carol.lee@company.com", 85000, "2017-01-10"),
    ("David Kim", "Finance", "Accountant", "david.kim@company.com", 78000, "2020-11-05"),
    ("Eva Brown", "Marketing", "Marketing Specialist", "eva.brown@company.com", 72000, "2021-06-18"),
    ("Frank Miller", "Engineering", "Backend Developer", "frank.miller@company.com", 98000, "2016-09-30"),
    ("Grace Wilson", "Sales", "Sales Executive", "grace.wilson@company.com", 67000, "2019-02-14"),
    ("Henry Clark", "Engineering", "Frontend Developer", "henry.clark@company.com", 93000, "2018-12-01"),
    ("Ivy Martinez", "HR", "Recruiter", "ivy.martinez@company.com", 69000, "2022-03-12"),
    ("Jack Turner", "Finance", "Financial Analyst", "jack.turner@company.com", 81000, "2020-08-25"),
    ("Karen White", "Marketing", "Content Writer", "karen.white@company.com", 65000, "2021-10-09"),
    ("Leo Harris", "Engineering", "QA Engineer", "leo.harris@company.com", 87000, "2017-05-20"),
    ("Mona Patel", "Sales", "Sales Manager", "mona.patel@company.com", 95000, "2015-04-17"),
    ("Nina Scott", "Engineering", "Data Scientist", "nina.scott@company.com", 105000, "2019-11-11"),
    ("Oscar Young", "Finance", "Controller", "oscar.young@company.com", 120000, "2016-07-03"),
    ("Paula Adams", "HR", "HR Coordinator", "paula.adams@company.com", 72000, "2020-01-29"),
    ("Quinn Baker", "Engineering", "Machine Learning Engineer", "quinn.baker@company.com", 110000, "2021-04-21"),
    ("Rita Evans", "Marketing", "SEO Specialist", "rita.evans@company.com", 70000, "2018-08-13"),
    ("Sam Foster", "Sales", "Account Executive", "sam.foster@company.com", 68000, "2019-06-07"),
    ("Tina Green", "Engineering", "Cloud Architect", "tina.green@company.com", 125000, "2017-10-30"),
    ("Uma Hall", "Finance", "Payroll Specialist", "uma.hall@company.com", 76000, "2022-02-19"),
    ("Victor King", "Engineering", "DevOps Lead", "victor.king@company.com", 115000, "2015-12-12"),
    ("Wendy Lopez", "HR", "Benefits Specialist", "wendy.lopez@company.com", 73000, "2018-04-23"),
    ("Xander Moore", "Marketing", "Brand Manager", "xander.moore@company.com", 95000, "2016-11-16"),
    ("Yara Nelson", "Sales", "Sales Associate", "yara.nelson@company.com", 62000, "2021-09-05"),
    ("Zane Ortiz", "Engineering", "Full Stack Developer", "zane.ortiz@company.com", 99000, "2019-03-28"),
    ("Ava Perez", "Finance", "Auditor", "ava.perez@company.com", 83000, "2020-05-15"),
    ("Ben Quinn", "Engineering", "Mobile Developer", "ben.quinn@company.com", 92000, "2017-08-08"),
    ("Cathy Reed", "HR", "HR Assistant", "cathy.reed@company.com", 60000, "2022-07-01"),
    ("Derek Stone", "Marketing", "Digital Marketer", "derek.stone@company.com", 71000, "2018-06-19"),
    ("Elena Taylor", "Sales", "Regional Manager", "elena.taylor@company.com", 102000, "2016-03-11"),
    ("Felix Underwood", "Engineering", "Security Engineer", "felix.underwood@company.com", 108000, "2019-12-22"),
    ("Gina Vasquez", "Finance", "Treasurer", "gina.vasquez@company.com", 118000, "2015-11-27"),
    ("Hank Walker", "Engineering", "Systems Engineer", "hank.walker@company.com", 97000, "2018-01-15"),
    ("Isabel Xu", "HR", "HR Generalist", "isabel.xu@company.com", 75000, "2020-09-10"),
    ("Jonas Young", "Marketing", "PR Specialist", "jonas.young@company.com", 69000, "2021-12-03"),
    ("Kylie Zane", "Sales", "Sales Representative", "kylie.zane@company.com", 66000, "2019-05-27"),
    ("Liam Allen", "Engineering", "Tech Lead", "liam.allen@company.com", 130000, "2017-07-21"),
    ("Maya Brown", "Finance", "Budget Analyst", "maya.brown@company.com", 80000, "2022-01-13"),
    ("Noah Carter", "Engineering", "UI/UX Designer", "noah.carter@company.com", 88000, "2018-10-02"),
    ("Olivia Davis", "HR", "Compensation Analyst", "olivia.davis@company.com", 77000, "2020-03-18"),
    ("Peter Evans", "Marketing", "Event Coordinator", "peter.evans@company.com", 68000, "2016-05-25"),
    ("Quincy Ford", "Sales", "Business Development", "quincy.ford@company.com", 99000, "2017-11-14"),
    ("Rachel Grant", "Engineering", "Data Engineer", "rachel.grant@company.com", 102000, "2019-01-07"),
    ("Steve Harris", "Finance", "Chief Financial Officer", "steve.harris@company.com", 200000, "2015-02-20"),
    ("Tara Ingram", "HR", "HR Director", "tara.ingram@company.com", 125000, "2016-08-29"),
    ("Umar Jones", "Engineering", "Network Engineer", "umar.jones@company.com", 94000, "2018-11-11"),
    ("Vera Knight", "Marketing", "Creative Director", "vera.knight@company.com", 120000, "2017-03-03"),
    ("Will Lee", "Sales", "Inside Sales Rep", "will.lee@company.com", 70000, "2021-11-20"),
    ("Xenia Moore", "Finance", "Risk Analyst", "xenia.moore@company.com", 85000, "2020-06-30"),
    ("Yusuf Novak", "Engineering", "Site Reliability Engineer", "yusuf.novak@company.com", 112000, "2019-09-17"),
    ("Zara Owens", "HR", "HR Business Partner", "zara.owens@company.com", 95000, "2018-02-06"),
    # 50 new records below
    ("Aaron Black", "Engineering", "Software Engineer", "aaron.black@company.com", 97000, "2020-04-12"),
    ("Bethany Clark", "HR", "HR Specialist", "bethany.clark@company.com", 72000, "2019-05-23"),
    ("Carlos Diaz", "Finance", "Accountant", "carlos.diaz@company.com", 79000, "2021-07-15"),
    ("Diana Evans", "Marketing", "Marketing Analyst", "diana.evans@company.com", 73000, "2018-11-30"),
    ("Ethan Foster", "Sales", "Sales Executive", "ethan.foster@company.com", 68000, "2022-02-10"),
    ("Fiona Grant", "Engineering", "Backend Developer", "fiona.grant@company.com", 99000, "2017-09-18"),
    ("George Hill", "Engineering", "Frontend Developer", "george.hill@company.com", 95000, "2019-12-05"),
    ("Hannah Irwin", "HR", "Recruiter", "hannah.irwin@company.com", 71000, "2020-06-21"),
    ("Ian Jones", "Finance", "Financial Analyst", "ian.jones@company.com", 82000, "2018-08-14"),
    ("Julia King", "Marketing", "Content Writer", "julia.king@company.com", 66000, "2021-03-19"),
    ("Kevin Lee", "Engineering", "QA Engineer", "kevin.lee@company.com", 88000, "2016-12-22"),
    ("Laura Moore", "Sales", "Sales Manager", "laura.moore@company.com", 97000, "2015-05-27"),
    ("Michael Nguyen", "Engineering", "Data Scientist", "michael.nguyen@company.com", 107000, "2020-10-11"),
    ("Natalie Owens", "Finance", "Controller", "natalie.owens@company.com", 121000, "2017-02-16"),
    ("Owen Parker", "HR", "HR Coordinator", "owen.parker@company.com", 73000, "2019-01-08"),
    ("Penelope Quinn", "Engineering", "Machine Learning Engineer", "penelope.quinn@company.com", 112000, "2021-05-25"),
    ("Quentin Ross", "Marketing", "SEO Specialist", "quentin.ross@company.com", 72000, "2018-09-29"),
    ("Rebecca Smith", "Sales", "Account Executive", "rebecca.smith@company.com", 69000, "2020-07-13"),
    ("Samuel Taylor", "Engineering", "Cloud Architect", "samuel.taylor@company.com", 127000, "2017-11-02"),
    ("Tessa Underwood", "Finance", "Payroll Specialist", "tessa.underwood@company.com", 77000, "2022-03-17"),
    ("Ulysses Vega", "Engineering", "DevOps Lead", "ulysses.vega@company.com", 117000, "2016-01-19"),
    ("Vanessa White", "HR", "Benefits Specialist", "vanessa.white@company.com", 74000, "2018-05-11"),
    ("William Xu", "Marketing", "Brand Manager", "william.xu@company.com", 97000, "2017-12-28"),
    ("Ximena Young", "Sales", "Sales Associate", "ximena.young@company.com", 63000, "2021-10-16"),
    ("Yosef Zimmerman", "Engineering", "Full Stack Developer", "yosef.zimmerman@company.com", 101000, "2019-04-04"),
    ("Alicia Brown", "Finance", "Auditor", "alicia.brown@company.com", 84000, "2020-06-20"),
    ("Brandon Carter", "Engineering", "Mobile Developer", "brandon.carter@company.com", 93000, "2017-10-13"),
    ("Cynthia Davis", "HR", "HR Assistant", "cynthia.davis@company.com", 61000, "2022-08-02"),
    ("Derek Edwards", "Marketing", "Digital Marketer", "derek.edwards@company.com", 72000, "2018-07-25"),
    ("Eliza Foster", "Sales", "Regional Manager", "eliza.foster@company.com", 103000, "2016-04-15"),
    ("Frederick Green", "Engineering", "Security Engineer", "frederick.green@company.com", 109000, "2019-11-29"),
    ("Gabriella Harris", "Finance", "Treasurer", "gabriella.harris@company.com", 119000, "2015-12-10"),
    ("Harold Ingram", "Engineering", "Systems Engineer", "harold.ingram@company.com", 98000, "2018-02-17"),
    ("Isabelle Johnson", "HR", "HR Generalist", "isabelle.johnson@company.com", 76000, "2020-10-05"),
    ("James Kim", "Marketing", "PR Specialist", "james.kim@company.com", 70000, "2021-01-22"),
    ("Kara Lee", "Sales", "Sales Representative", "kara.lee@company.com", 67000, "2019-06-30"),
    ("Landon Miller", "Engineering", "Tech Lead", "landon.miller@company.com", 132000, "2017-08-25"),
    ("Megan Nelson", "Finance", "Budget Analyst", "megan.nelson@company.com", 81000, "2022-02-14"),
    ("Nathan Owens", "Engineering", "UI/UX Designer", "nathan.owens@company.com", 89000, "2018-11-09"),
    ("Olga Perez", "HR", "Compensation Analyst", "olga.perez@company.com", 78000, "2020-04-27"),
    ("Paul Quinn", "Marketing", "Event Coordinator", "paul.quinn@company.com", 69000, "2016-06-12"),
    ("Quincy Reed", "Sales", "Business Development", "quincy.reed@company.com", 100000, "2017-12-03"),
    ("Renee Stone", "Engineering", "Data Engineer", "renee.stone@company.com", 103000, "2019-02-15"),
    ("Steven Turner", "Finance", "Chief Financial Officer", "steven.turner@company.com", 201000, "2015-03-18"),
    ("Tina Underhill", "HR", "HR Director", "tina.underhill@company.com", 126000, "2016-09-21"),
    ("Ulrich Vogel", "Engineering", "Network Engineer", "ulrich.vogel@company.com", 95000, "2018-12-13"),
    ("Valerie White", "Marketing", "Creative Director", "valerie.white@company.com", 121000, "2017-04-07"),
    ("Winston Xu", "Sales", "Inside Sales Rep", "winston.xu@company.com", 71000, "2021-12-11"),
    ("Xavier Young", "Finance", "Risk Analyst", "xavier.young@company.com", 86000, "2020-07-21"),
    ("Yasmine Zane", "Engineering", "Site Reliability Engineer", "yasmine.zane@company.com", 113000, "2019-10-23"),
    ("Zelda Abbott", "HR", "HR Business Partner", "zelda.abbott@company.com", 96000, "2018-03-15")
]

cursor.executemany('''
    INSERT INTO EMPLOYEE (NAME, DEPARTMENT, ROLE, EMAIL, SALARY, DATE_JOINED)
    VALUES (?, ?, ?, ?, ?, ?)
''', employees)

connection.commit()
connection.close()