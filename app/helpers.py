from rich.table import Table
from rich.console import Console

#we can format the tables later
def help_counselor():
    table = Table(title="Help", border_style="red")

    table.add_column("Name of command", justify="left", style="cyan", no_wrap=True)
    table.add_column("Usage", justify="left", style="yellow bold italic", no_wrap=True)
    table.add_column("Function", justify="left", style="green", no_wrap=True)

    table.add_row("search name", "search name <student_name>", "Searches for the name of the student")

    console = Console()
    console.print(table)


def help_student(title):
    table = Table(title=title, border_style="red")

    table.add_column("Name of command", justify="left", style="cyan", no_wrap=True)
    table.add_column("Usage", justify="left", style="yellow bold italic", no_wrap=True)
    table.add_column("Function", justify="left", style="green", no_wrap=True)

    table.add_row("search student name", "search sname <student_name>", "Searches for the name of the student")

    console = Console()
    console.print(table)