# re.IGNORECASE can be used for allowing user to type arbitrary cased texts.
QUIT_NO_CASE = re.compile('quit', re.IGNORECASE)
command = input('Type Command:')
if QUIT_NO_CASE.match(command):
  print("Quiting...")

# Dissect multiple pieces from a string, using re.split.
PHONE_NUMBER_REG = re.compile('(\d+)-(\d+)-(\d+)')
# 0: area code, 1: extension1, 2: extension2
items = PHONE_NUMBER_REG.split(phone_number)
