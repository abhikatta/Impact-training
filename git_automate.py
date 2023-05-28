import os
import time
commit_message = str(input("Commit message: "))
while True:
    os.system('git add .')
    os.system('git commit -m'+commit_message)
    os.system('git push')
    print("\nTrying again in 10 seconds.\n")
    time.sleep(secs=10)
