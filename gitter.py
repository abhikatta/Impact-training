import os
import time
commit_message = str(input("Commit message: "))
a = False
while not a:
    if not a:

        os.system('git add .')
        os.system('git commit -m'+commit_message)
        os.system('git push')
        a = True
    else:
        print("\nTrying again in 10 seconds.\n")
        time.sleep(10)
