### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

# We are originally given two questions in the template code.
# All nine are at the bottom so add them (in order) to welcome_assignment_answers

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "82805a76df1be876a4b7e1ed29b3e10b7ed7be483897765a9057c9f203c0c5ec"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = int(7)
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        # answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
        answer = "Question solution not found."
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    print()
    debug_question = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "Is it possible to decrypt a message without a key? - Yes/No"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "Is it possible to decode a message without a key? - Yes/No"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

    debug_question = "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    print(debug_question, " ..... ", welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":