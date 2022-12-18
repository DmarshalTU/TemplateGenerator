from git import Repo
import gitlab
import sh


def upload_new(new_project):
    # sh.mkdir(f'/tmp/{new_project}')
    sh.mv(f"{new_project}/", f"/tmp/{new_project}")
    sh.rm("-rf", new_project)
    gl = gitlab.Gitlab(
        url="https://gitlab-ber1.cyren.io/dataservices/template-playground",
        oauth_token="/Users/v1291l/.ssh/id_ed25519",
    )
    project = gl.projects.create({"name": f"{new_project}"})
    repo = Repo(project.ssh_url_to_repo, f"/tmp/{new_project}")
    repo.git.add(all=True)
    repo.git.commit(message="First upload of generated project")
    repo.git.push()
