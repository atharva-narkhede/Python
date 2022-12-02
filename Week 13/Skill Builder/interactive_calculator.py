#write an interactive calculator! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). 
#Split user input using str.split(), and check whether the resulting list is valid:


class FormulaError(Exception): pass
def parse_input(user_input):

  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  n1, op, n2 = input_list
  try:
    n1 = float(n1)
    n2 = float(n2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return n1, op, n2

def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  
  raise FormulaError('{0} is not a valid operator'.format(op))
while True:
  user_input = input()
  if user_input == 'quit':
    print("end of program")
    break
  n1, op, n2 = parse_input(user_input)
  result = calculate(n1, op, n2)
  print(result)
