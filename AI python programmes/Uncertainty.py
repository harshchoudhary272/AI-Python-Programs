import sys

# Create a dictionary to map marks
Marksprob = {}

# Get input from stdin
for line in sys.stdin:
    #Remove spaces from beginning and end of the line
    line = line.strip()

    # parse the input from mapper.py
    ClassA, Marks = line.split('\t', 1)


# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)


# Sample Space
ClassA = 30

# Determine the probability of drawing a heart
Marks = 15
grade_probability = event_probability(Marks, ClassA)

# Print each probability
print(str(grade_probability) + '%')



