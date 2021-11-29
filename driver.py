import webbrowser

def main():
    message = '''Welcome to Big Data Processing Application
    Please type the number that corresponds to which application you would like to run:
    1. Apache Hadoop
    2. Apache Spark
    3. Jupyter Notebook
    4. SonarQube and SonarScanner
    5. quit

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
        elif choice == 5:
            quit()
        else:
            print("Please enter a valid number > ")
            print(message)
    


def hadoop():
    return webbrowser.open('http://35.226.26.81:9870/')

def spark():
    return webbrowser.open('http://35.223.120.201:8080/')

def jupyter():
    return webbrowser.open('http://35.239.218.131:8888/')

def sonar():
    return webbrowser.open('http://34.133.43.239:9000/')

if __name__ == '__main__':
    main()
