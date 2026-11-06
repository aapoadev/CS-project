import pathlib
class Practice:
    def __init__(self, subject, times_practiced):
        self.subject = subject
        self.times_practiced = times_practiced

    def __str__(self):
        return f'{self.subject} {self.times_practiced}'

def read_times(file_path):
    practices_list = []

    with open(file_path) as file:
        for line in file:
            words = line.split()
            category = 
        
