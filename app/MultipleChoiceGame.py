from app.WorkingWithClassAndObject import Questions

Question_prompt = [
    "what colour are green apples - \n(a)Red\n(b)Green\n(c)Blue\n(d)Orange",
    "what colour are bananas - \n(a)Red\n(b)Green\n(c)yellow\n(d)Orange",
    "what colour are strawberies - \n(a)Red\n(b)Green\n(c)Blue\n(d)Orange"
]

Question = [
    Questions(Question_prompt[0], "b"),
    Questions(Question_prompt[1], "c"),
    Questions(Question_prompt[2], "a")
]

def run_test(Questions):
    score = 0
    for question in Questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(score)

run_test(Question)
