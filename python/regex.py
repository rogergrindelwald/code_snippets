# re.IGNORECASE can be used for allowing user to type arbitrary cased texts.
QUIT_NO_CASE = re.compile('quit', re.IGNORECASE)
command = input('Type Command:')
if QUIT_NO_CASE.match(command):
  print("Quiting...")
