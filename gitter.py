# TODO:
# 1. Fix this.
import os
import time
commit_message = str(input("Commit message: "))
a = False
while not a:
    if not a:

        os.system('git add .')
        os.system('git commit -m'+commit_message)
        if not os.system('git push'):
            continue
        elif os.system('git push'):
            break

    else:
        print("\nTrying again in 10 seconds.\n")
        time.sleep(10)
