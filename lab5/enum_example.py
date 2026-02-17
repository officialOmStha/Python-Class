from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()

def process_application(status):
    if status == Status.PENDING:
        print("Application is pending.")
    elif status == Status.APPROVED:
        print("Application approved!")
    elif status == Status.REJECTED:
        print("Application rejected.")

process_application(Status.APPROVED)
