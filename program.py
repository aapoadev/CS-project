import pathlib
class Practice:
    def __init__(self, subject, times_practiced):
        self.subject = subject
        self.times_practiced = times_practiced

    def __str__(self):
        return f'{self.subject} {self.times_practiced}'

