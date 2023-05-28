import os
commit_message = str(input("Commit message: "))
os.system('git add .')
os.system('git commit -m'+commit_message)
os.system('git push')
