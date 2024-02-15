from git import *

def get_commit_comments():
    repo = Repo(r"C:\Users\William-School\dev\ProjectLog")
    commits = repo.iter_commits()
    return commits

def get_specific_commit(hexsha):
    repo = Repo(r"C:\Users\William-School\dev\ProjectLog")
    for c in repo.iter_commits():
        c_hexsha = str(c.hexsha)
        hexsha = str(hexsha)
        if c_hexsha == hexsha:
            return c