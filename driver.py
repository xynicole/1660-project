def main():
    message = '''Welcome to Big Data Processing Application
    Please type the number that corresponds to which application you would like to run:
    1. Apache Hadoop
    2. Apache Spark
    3. Jupyter Notebook
    4. SonarQube and SonarScanner

    '''

    choice = " "
    print(message)
    while (True):
        choice  = input("Type the number here > ")
        if choice == 1:
            print("Running Apache Hadoop")
            hadoop()
        elif choice == 2:
            print("Running Apache Spark")
            spark()
        elif choice == 3:
            print("Running Jupyter Notebook")
            jupyter()
        elif choice == 4:
            print("Running SonarQube and SonarScanner")
            sonar()
        else:
            print("Please enter a valid number > ")
            print(message)
    


def hadoop():
    pass

def spark():
    pass

def jupyter():
    pass

def sonar():
    pass

if __name__ == '__main__':
    main()
