import argparse, os, rich, bcrypt
from dotenv import load_dotenv
import mysql.connector as mysql
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet
import user
from getpass import getpass, getuser
def main():
    load_dotenv(verbose=True)
    try:
        import colorama
        colorama.init()
    except ImportError:
        colorama = None
    try:
        from termcolor import colored
    except ImportError:
        colored = None

    console = Console()
    init = Text()
    init.append('Starting Application \n\n', style='italic')
    console.print(init)
    font = Figlet(font='larry3d')
    # console.print(font.renderText('IntlApp Dashboard - CLI'), style='bold green')
    text = Text(justify='center').assemble((font.renderText('IntlApp'), 'bold green'), (font.renderText('Dashboard'), 'bold yellow'))
    console.print(text)

    ps = 3306 if os.name == 'nt' else '3306'

    
    db = mysql.connect(
        host='localhost',
        user=os.getenv('DATABASE_USERNAME'),
        password=os.getenv('DATABASE_PASSWORD'),
        port=ps,
        database=os.getenv('DATABASE_NAME')
    )
    if db:
        cursor = db.cursor()
        cursor.execute('use {};'.format(os.getenv('DATABASE_NAME')))
        console.print('Connection [green][b]successfull[/b][/green][blink]...[/blink]\n\n :gear: Initialising Tables')
        # init and check for tables: user, counselor, teacher, sessions ...
        user.student_create_table(cursor)
        # admin.admin_create_table(cursor)
        console.print('🔐 Login as ? \n (1) Counselor / Teacher \n (2) Student')
        login = False
        while not login:
            inp = str(input('Please enter number to login as: '))
            if inp == '1':
                console.print('Enter the [b]Admin Credentials [/b]')
            elif inp == '2':
                admmno = str(input('Enter your admission number: '))
                console.print('🔎 Searching for existing record in the database...')
                if user.exists(cursor, admmno):
                    # ask for password, unhash and confirm login = True
                    pass
                else:
                    # create new user, ask for password, ask for details then show table to confirm reg and login = True
                    console.print(':pensive: Record not found.')
                    new = str(input('Would you like to create an account [y/n] ? '))
                    if new[0] == 'n':
                        console.print("Uh-oh! Thank you for using IntlApp Dashboard.\n\n[i]Exiting...[/i]")
                        exit()
                    else:
                        console.print('🙈 [i green]We do not store your passwords.[/i green]')
                        admnno = str(input('Enter Admission Number: '))
                        password = getpass(prompt='Enter password: ')
                        password = password.encode('ascii')
                        hsh = bcrypt.hashpw(password, os.getenv('BCRYPT_SALT').encode('ascii'))
                        # send admnno and pswd hash to creation function
                        user.student_create_prompt(cursor, admnno, hsh.decode('ascii'))
                        print('todo...')
            else:
                print('catch something maybe')
    else:
        console.print('⚠️  Something went wrong... Please try again.')
    # except:
    #     console.print('There was some error connecting to the database.\n\n[bold red]⚠️  Something went wrong... Please try again.[/bold red]')
    #     exit

    # prompt starts now

if __name__ == '__main__':
    main()