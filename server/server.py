from git import *
repo = Repo(r"C:\Users\William-School\dev\ProjectLog")
print(repo)

''' (OLD) Only Does Most Recent Commit
commit = repo.commit()
print(repo.commit())
print(commit.message)
'''

commits = repo.iter_commits()
print(commits)
commits = next(commits)
print(commits.message)