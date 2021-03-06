from PyInquirer import Separator


def get_student_questions():
    questions = [
        {
            "type": "input",
            "name": "full_name",
            "message": "What's your name",
        },
        {
            "type": "input",
            "name": "clsec",
            "message": "What's your class and section",
            "default": "12I",
        },
        {
            "type": "list",
            "name": "stream",
            "message": "What's your stream ?",
            "choices": ["PCB", "PCMC", "PCMB", "PCME", "COMM.", "HUMA.", "ARTS"],
        },
    ]
    return questions


def deadline_prompt():
    dl = {
        "type": "list",
        "name": "deadline",
        "message": "What's your college applcation deadline",
        "choices": [
            "November first-week (US_EARLY1)",
            "Mid-November (UK/US_EARLY2)",
            "November End (US_UCs)",
            "January first-week (UK/US_REGULAR)",
            "Indian Private Colleges (INDIA_PRIV)",
            "Not decided (ND)",
        ],
        "when": lambda answers: answers["add_new"],
    }
    return dl


def get_college_questions():
    dl = deadline_prompt()
    college_questions = [
        {
            "type": "confirm",
            "name": "add_new",
            "message": "Add a new college to your Watchlist?",
            "default": True,
        },
        {
            "type": "input",
            "name": "new_college",
            "message": "What's your college/university name",
            "when": lambda answers: answers["add_new"],
        },
        dl,
    ]
    return college_questions


def get_admin_questions():
    admin_questions = [
        {
            "type": "input",
            "name": "full_name",
            "message": "What's your name",
        },
        {
            "type": "confirm",
            "name": "is_counselor",
            "message": "Are you a counselor?",
            "default": False,
        },
        {
            "type": "list",
            "name": "subject",
            "message": "What subject do you teach?",
            "choices": [
                "Accountancy",
                "Biology",
                "Biotechnology",
                "BusinessStudies",
                "Chemistry",
                "ComputerScience",
                "Economics",
                "English",
                "FineArts",
                "Geography",
                "Hindi",
                "Mathematics",
                "PerformingArts",
                "PE",
                "Physics",
                "Political Science",
                "Sanskrit",
                "French",
                "German",
            ],
            "when": lambda answers: not answers["is_counselor"],
        },
    ]
    return admin_questions


def get_admin_options():
    options = [
        {
            "type": "list",
            "name": "option",
            "message": "What would you like to do? (Ctrl+C to force quit)",
            "choices": [
                Separator("=== Student Actions ==="),
                "Search for a student",
                "Update status of a student (documents)",
                Separator("=== College Actions ==="),
                "Add a college to the database",
                "Delete a college from the database",
                Separator("=== Session/Notification Actions ==="),
                "Add a session/notification",
                "Cancel a session/notification",
                Separator("=== Account Actions ==="),
                "Hide this prompt (to scroll up)",
                "Exit IntlApp Dashboard",
                "Delete your IntlApp account and exit",
            ],
        }
    ]
    return options


def get_admin_search_method():
    searchMethods = [
        {
            "type": "list",
            "name": "method",
            "message": "Select a method for searching",
            "choices": [
                "Search by AdmnNO",
                "Search by Class-Section",
                "Search by Stream",
                "Search by Deadline",
                "Go back",
            ],
        }
    ]
    return searchMethods


def get_student_options():
    options = [
        {
            "type": "list",
            "name": "opr",
            "message": "What would you like to do?",
            "choices": [
                Separator("=== Watchlist Actions ==="),
                "Add a college",
                "Remove a college",
                Separator("=== Application Actions ==="),
                "Request a LOR from a teacher",
                "Change the deadline of a college",
                "Change your application status for a college",
                Separator("=== Account Actions ==="),
                "Hide this prompt (to scroll up)",
                "Exit IntlApp Dashboard",
                "Delete your IntlApp account and exit.",
            ],
        }
    ]
    return options

def get_teacher_options():
    options = [
        {
            "type": "list",
            "name": "option",
            "message": "What would you like to do? (Ctrl+C to force quit)",
            "choices": [
                Separator("=== Student Actions ==="),
                "Search for a student",
                "Update status of a Student LOR",
                Separator("=== Account Actions ==="),
                "Hide this prompt (to scroll up)",
                "Exit IntlApp Dashboard",
                "Delete your IntlApp account and exit",
            ]
        }
    ]
    return options