def arithmetic_arranger(problems, show_answers=False):
    firstLine = []
    secondLine = []
    dashes = []
    results  = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    

    for problem in problems: 
        operation = problem.split()
        leftN, operator, rightN = operation
        if len(leftN) > 4 or len(rightN) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not leftN.isdigit() or not rightN.isdigit() :
            return 'Error: Numbers must only contain digits.'
        if not operator == '+' and not operator == '-':
            return "Error: Operator must be '+' or '-'."
        width = max(len(leftN), len(rightN)) +2    

        firstLine.append(leftN.rjust(width))
        secondLine.append(operator +rightN.rjust(width - 1))

        dashes.append('-' * width)
        if show_answers:
            if operator == '+':
                answer = str(int(leftN) + int(rightN))
            else:
                answer = str(int(leftN) - int(rightN))
            results.append(answer.rjust(width))
        
        arranged = '    '.join(firstLine) + '\n' + \
               '    '.join(secondLine) + '\n' + \
               '    '.join(dashes)

        if show_answers:
            arranged += '\n' + '    '.join(results)
    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')