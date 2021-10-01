with open('data.txt') as f:
    lines = f.readlines()

Input = []
Output = []

for i in lines:
    j = i.strip()
    Input.append(j)

ques_phrase = ['which', 'what', 'whose', 'who', 'whom', 'whose', 'what', 'which', 'where', 'when', 'how', 'why']

for sen in Input:
    if any(x in sen for x in ques_phrase):
        Output.append((str(sen) + ' Yes'))
    else:
        Output.append((str(sen) + ' No'))

with open('data0.txt', 'w+') as g:
    for item in Output:
        g.write('{}\n'.format(item))

g.close()
