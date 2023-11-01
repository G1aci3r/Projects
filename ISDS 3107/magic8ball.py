import random

class Magic8Ball:
    answers = ["It is certain.", "It is decidedly so.", "Without a doubt.",
               "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
               "Most likely.", "Outlook good.", "Signs point to yes.",
               "Yes.", "Reply hazy, try again", "Ask again later.",
               "Better not tell you now.", "Cannot predict now.",
               "Concentrate and ask again.", "Cannot predict now.",
               "Concentrate and ask again.", "Don't count on it.",
               "My reply is no.", "My sources say no.",
               "Outlook not so good.", "Very doubtful."]

    # the __init__ method initializes the object.
    def __init__(self):
        self.answer = ""

    def shake(self):
        self.answer = random.choice(self.answers)

    def get_answer(self):
        return self.answer
 
 eight_ball = magic8Ball()
 eight_ball.shake()
 answer = eight_ball.get_answer()
 print("Magic 8-Ball says:", answer)   
