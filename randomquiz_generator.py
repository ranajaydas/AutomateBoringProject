"""  Here is what the program does:
•	 Creates 35 different quizzes.
•	 Creates 50 multiple-choice questions for each quiz, in random order.
•	 Provides the correct answer and three random wrong answers for each question, in random order.
•	 Writes the quizzes to 35 text files.
•	 Writes the answer keys to 35 text files. """

import random
import os

num_students = 35                                 # in case we need to make more than/less than 35 quizzes
total_questions = 50                              # or we can also make this len(capitals_dict)

capitals_dict = {'Alabama': 'Montgomery',
                 'Alaska': 'Juneau',
                 'Arizona': 'Phoenix',
                 'Arkansas': 'Little Rock',
                 'California': 'Sacramento',
                 'Colorado': 'Denver',
                 'Connecticut': 'Hartford',
                 'Delaware': 'Dover',
                 'Florida': 'Tallahassee',
                 'Georgia': 'Atlanta',
                 'Hawaii': 'Honolulu',
                 'Idaho': 'Boise',
                 'Illinois': 'Springfield',
                 'Indiana': 'Indianapolis',
                 'Iowa': 'Des Moines',
                 'Kansas': 'Topeka',
                 'Kentucky': 'Frankfort',
                 'Louisiana': 'Baton Rouge',
                 'Maine': 'Augusta',
                 'Maryland': 'Annapolis',
                 'Massachusetts': 'Boston',
                 'Michigan': 'Lansing',
                 'Minnesota': 'Saint Paul',
                 'Mississippi': 'Jackson',
                 'Missouri': 'Jefferson City',
                 'Montana': 'Helena',
                 'Nebraska': 'Lincoln',
                 'Nevada': 'Carson City',
                 'New Hampshire': 'Concord',
                 'New Jersey': 'Trenton',
                 'New Mexico': 'Santa Fe',
                 'New York': 'Albany',
                 'North Carolina': 'Raleigh',
                 'North Dakota': 'Bismarck',
                 'Ohio': 'Columbus',
                 'Oklahoma': 'Oklahoma City',
                 'Oregon': 'Salem',
                 'Pennsylvania': 'Harrisburg',
                 'Rhode Island': 'Providence',
                 'South Carolina': 'Columbia',
                 'South Dakota': 'Pierre',
                 'Tennessee': 'Nashville',
                 'Texas': 'Austin',
                 'Utah': 'Salt Lake City',
                 'Vermont': 'Montpelier',
                 'Virginia': 'Richmond',
                 'Washington': 'Olympia',
                 'West Virginia': 'Charleston',
                 'Wisconsin': 'Madison',
                 'Wyoming': 'Cheyenne'}

if not os.path.exists('./Quiz'):                                # create a directory called Quiz if it doesn't exist
    os.makedirs('./Quiz')

for quiz_number in range(num_students):
    quiz_file = open('./Quiz/capitalsquiz_%s.txt' % (quiz_number+1), 'w')                # creates the quiz files
    answer_file = open('./Quiz/capitalsquiz_answers_%s.txt' % (quiz_number+1), 'w')      # creates the answer files

    # Write out the header for the quiz.

    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + 'State Capitals Quiz (Form %s)' % (quiz_number+1))
    quiz_file.write('\n\n')

    # Create a shuffled list of states for the quiz

    state_list = list(capitals_dict.keys())
    random.shuffle(state_list)

    # Loop through the states, making a question for each
    for question_number in range(total_questions):
        correct_answer = capitals_dict[state_list[question_number]]         # extract the correct answer
        wrong_answers = list(capitals_dict.values())                        # take all the values from the dictionary
        del wrong_answers[wrong_answers.index(correct_answer)]              # remove the correct answer from the list
        wrong_answers = random.sample(wrong_answers, 3)                     # take a random sample of 3 from that list
        answer_options = wrong_answers + [correct_answer]                   # create the 4 options
        random.shuffle(answer_options)                                      # shuffle up the 4 options!!

        # Write each question to the file
        quiz_file.write('\n{}. What is the capital of {}?\n'.format(question_number+1, state_list[question_number]))
        for option_number in range(4):
            quiz_file.write(' {}. {}\n'.format('ABCD'[option_number], answer_options[option_number]))

        # Write the answer to the answers file
        answer_file.write('{}. {}\n'.format(question_number+1, 'ABCD'[answer_options.index(correct_answer)]))

    # close the files
    quiz_file.close()
    answer_file.close()
