# This is a self study about handling hash (key-value pairs) type data structure
# The problem1 is a program that find out a runner who did not complete the marathon among numerous runners
# I used online compiler to run and test this code

# Detailed problem
# - Participant is an array which contains the participated runners' name
# - Completion is an array which contains the name of runners' who completed the marathon
# - The number of runners who participated in the marathon is more than one and less than 100,000
# - The length of completion arr is less than length of participant arr by one
# - Participants' names consist of more than 1 and less than 20 alphabetic lowercase letters.
# - Some of the participants may have the same name.

def solution(participant, completion):
    answer = ''

    # Count the occurrence of every elem in both arrays and compare with the same elem
    # The elem with different occurrence is the answer of this problem
    # It takes O(n^2) -> O(n) for going through the array loop and O(n) for count the elem in array inner loop side => O(n * n) = O(n^2)
    for x in participant:
        if participant.count(x) != completion.count(x):
            answer = x
    return answer

    # It can be faster using hash by O(n)
    # def solution(participant, completion):
    #     answer = ''
    #     .....The imporved code tbd....
    #     return answer