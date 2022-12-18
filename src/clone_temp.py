import logging
from git import Repo


logging.basicConfig(filename="app.log", filemode="w", level=logging.INFO)


def clone_template(git_repo: str, new_project: str) -> bool:

    logging.info(f"started cloning template {git_repo}")

    try:
        repo = Repo.clone_from(git_repo, f"{new_project}")
        logging.info(f"cloned template {git_repo}")
        return True
    except Exception as e:
        print(e)
        logging.error(e)
        return False
