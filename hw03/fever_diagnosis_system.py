def main():
    questions = ["Are you coughing? (yes or no)\n",
                 "Are you short of breath or wheezing or coughing up phelgm?" +
                 " (yes or no)\n",
                 "Do you have a headache? (yes or no)\n",
                 "Do you have aching bones or aching joints? (yes or no)\n",
                 "Do you have a rash? (yes or no)\n",
                 "Do you have a sore throat? (yes or no)\n",
                 "Do you have back pain just above the waist with chills" +
                 " and fever? (yes or no)\n",
                 "Do you have pain urinating or are urinating more often?" +
                 " (yes or no)\n",
                 "Have you spent the day in the sun or in hot conditions?" +
                 " (yes or no)\n",
                 "Are you experienxing any of the following: pain when" +
                 " bending your head forward, nausea or vomiting, bright" +
                 " light hurting your eyes, drowsiness or confusion?" +
                 " (yes or no)\n",
                 "Are you vomiting or had diarrhea? (yes or no)\n"]
    answers = ["Possibilites include pneumonia or infection of airways.",
               "Possibilities include viral infection.",
               "Insufficient information to list possibilities.",
               "Possibilities include a throat infection.",
               "Possibilities include kidney infection.",
               "Possibilities include a urinary tract infection.",
               "Possibilites include sunstroke or heat exhaustion.",
               "Possibilities include menigits.",
               "Possibilites include digestive tract infection."]
    yes = "yes"
    no = "no"

    if input(questions[0]).lower() == yes:
        if input(questions[1]).lower() == yes:
            print(answers[0])
        elif input(questions[2]).lower() == yes:
            print(answers[1])
        else:
            mini_fever_diagnosis_system(questions, answers, yes, no)
    elif input(questions[2]).lower() == yes:
        if input(questions[9]).lower() == yes:
            print(answers[7])
        elif input(questions[10]).lower() == yes:
            print(answers[8])
    elif input(questions[10]).lower() == no:
        mini_fever_diagnosis_system(questions, answers, yes, no)


def mini_fever_diagnosis_system(questions, answers, yes, no):
    if input(questions[3]).lower() == yes:
        print(answers[1])
    elif input(questions[4]).lower() == yes:
        print(answers[2])
    elif input(questions[5]).lower() == yes:
        print(answers[3])
    elif input(questions[6]).lower() == yes:
        print(answers[4])
    elif input(questions[7]).lower() == yes:
        print(answers[5])
    elif input(questions[8]).lower() == yes:
        print(answers[6])
    else:
        print(answers[2])


main()
