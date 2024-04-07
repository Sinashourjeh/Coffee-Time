import requests

class GitHubRepoManager:
    def __init__(self, token):
        self.headers = {'Authorization': f'token {token}'}
        self.results = []

    def _handle_response(self, response, success_message):
        if response.status_code == 200:
            print(success_message)
            return True
        else:
            print(f"Failed (Status code: {response.status_code})")
            return False

    def change_visibility(self, repo_name, visibility):
        url = f'https://api.github.com/repos/username/{repo_name}'
        data = {'private': visibility}
        response = requests.patch(url, headers=self.headers, json=data)
        success_message = f"Visibility of repository {repo_name} changed successfully."
        if self._handle_response(response, success_message):
            self.results.append(success_message)

    def get_user_repositories(self, visibility='all'):
        url = f'https://api.github.com/user/repos?type={visibility}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch repositories (Status code: {response.status_code})")
            return None

    def change_visibility_bulk(self, repo_names, visibility):
        for repo_name in repo_names:
            self.change_visibility(repo_name, visibility)
        
        print("\nSummary of changes:")
        for result in self.results:
            print(result)


    def manage_files(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/contents'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            files = response.json()
            print(f"Files in repository {repo_name}:")
            for file in files:
                print(file['name'])
        else:
            print(f"Failed to fetch files in repository {repo_name} (Status code: {response.status_code})")


    def send_commit(self, repo_name, commit_message, files):
        url = f'https://api.github.com/repos/username/{repo_name}/contents/'
        data = {
            'message': commit_message,
            'content': files
        }
        response = requests.put(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Commit sent to repository {repo_name} successfully.")
        else:
            print(f"Failed to send commit to repository {repo_name} (Status code: {response.status_code})")


    def manage_branches(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/branches'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            branches = response.json()
            print(f"Branches in repository {repo_name}:")
            for branch in branches:
                print(branch['name'])
        else:
            print(f"Failed to fetch branches in repository {repo_name} (Status code: {response.status_code})")


    def create_pull_request(self, repo_name, title, body, head, base):
        url = f'https://api.github.com/repos/username/{repo_name}/pulls'
        data = {
            'title': title,
            'body': body,
            'head': head,
            'base': base
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Pull Request created in repository {repo_name} successfully.")
        else:
            print(f"Failed to create Pull Request in repository {repo_name} (Status code: {response.status_code})")


    def manage_issues(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/issues'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            issues = response.json()
            print(f"Issues in repository {repo_name}:")
            for issue in issues:
                print(f"Title: {issue['title']}, Number: {issue['number']}")
        else:
            print(f"Failed to fetch Issues in repository {repo_name} (Status code: {response.status_code})")


    def manage_projects(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/projects'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            projects = response.json()
            print(f"Projects in repository {repo_name}:")
            for project in projects:
                print(f"Name: {project['name']}, ID: {project['id']}")
        else:
            print(f"Failed to fetch Projects in repository {repo_name} (Status code: {response.status_code})")


    def manage_wikis(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/wikis'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            wikis = response.json()
            print(f"Wikis in repository {repo_name}:")
            for wiki in wikis:
                print(wiki['title'])
        else:
            print(f"Failed to fetch Wikis in repository {repo_name} (Status code: {response.status_code})")


    def manage_secrets(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/actions/secrets'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            secrets = response.json()
            print(f"Secrets in repository {repo_name}:")
            for secret in secrets['secrets']:
                print(secret['name'])
        else:
            print(f"Failed to fetch Secrets in repository {repo_name} (Status code: {response.status_code})")


    def manage_collaborators(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/collaborators'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            collaborators = response.json()
            print(f"Collaborators in repository {repo_name}:")
            for collaborator in collaborators:
                print(collaborator['login'])
        else:
            print(f"Failed to fetch Collaborators in repository {repo_name} (Status code: {response.status_code})")


    def manage_deployments(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/deployments'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            deployments = response.json()
            print(f"Deployments in repository {repo_name}:")
            for deployment in deployments:
                print(f"ID: {deployment['id']}, Environment: {deployment['environment']}")
        else:
            print(f"Failed to fetch Deployments in repository {repo_name} (Status code: {response.status_code})")


    def manage_actions(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/actions/workflows'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            actions = response.json()
            print(f"Actions in repository {repo_name}:")
            for action in actions['workflows']:
                print(f"Name: {action['name']}, ID: {action['id']}")
        else:
            print(f"Failed to fetch Actions in repository {repo_name} (Status code: {response.status_code})")


    def manage_webhooks(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/hooks'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            webhooks = response.json()
            print(f"Webhooks in repository {repo_name}:")
            for webhook in webhooks:
                print(f"ID: {webhook['id']}, URL: {webhook['config']['url']}")
        else:
            print(f"Failed to fetch Webhooks in repository {repo_name} (Status code: {response.status_code})")


    def manage_customers_and_orgs(self):
        url = 'https://api.github.com/user/orgs'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            orgs = response.json()
            print("Organizations:")
            for org in orgs:
                print(org['login'])
        else:
            print(f"Failed to fetch Organizations (Status code: {response.status_code})")


    def manage_emails(self):
        url = 'https://api.github.com/user/emails'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            emails = response.json()
            print("Emails:")
            for email in emails:
                print(email['email'])
        else:
            print(f"Failed to fetch Emails (Status code: {response.status_code})")


    def manage_gists(self):
        url = 'https://api.github.com/gists'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            gists = response.json()
            print("Gists:")
            for gist in gists:
                print(gist['id'])
        else:
            print(f"Failed to fetch Gists (Status code: {response.status_code})")


    def manage_comments(self, repo_name, issue_number=None):
        if issue_number:
            url = f'https://api.github.com/repos/username/{repo_name}/issues/{issue_number}/comments'
        else:
            url = f'https://api.github.com/repos/username/{repo_name}/comments'
        
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            comments = response.json()
            if issue_number:
                print(f"Comments on Issue #{issue_number} in repository {repo_name}:")
            else:
                print(f"Comments in repository {repo_name}:")
                
            for comment in comments:
                print(f"ID: {comment['id']}, Body: {comment['body']}")
        else:
            print(f"Failed to fetch Comments in repository {repo_name} (Status code: {response.status_code})")


    def manage_teams(self):
        url = 'https://api.github.com/user/teams'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            teams = response.json()
            print("Teams:")
            for team in teams:
                print(f"Name: {team['name']}, ID: {team['id']}")
                print("Members:")
                for member in team['members']:
                    print(member['login'])
                print("")
        else:
            print(f"Failed to fetch Teams (Status code: {response.status_code})")


    def manage_reports(self):
        url = 'https://api.github.com/user/repos'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            repos = response.json()
            print("Repositories:")
            for repo in repos:
                print(f"Name: {repo['name']}")
                print("Statistics:")
                print(f"Watchers: {repo['watchers_count']}")
                print(f"Stars: {repo['stargazers_count']}")
                print(f"Forks: {repo['forks_count']}")
                print("")

        else:
            print(f"Failed to fetch Repositories (Status code: {response.status_code})")


    def create_issue(self, repo_name, title, body):
        url = f'https://api.github.com/repos/username/{repo_name}/issues'
        data = {
            'title': title,
            'body': body
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Issue created in repository {repo_name} successfully.")
        else:
            print(f"Failed to create issue in repository {repo_name} (Status code: {response.status_code})")


    def manage_labels(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/labels'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            labels = response.json()
            print(f"Labels in repository {repo_name}:")
            for label in labels:
                print(f"Name: {label['name']}, Color: {label['color']}")
        else:
            print(f"Failed to fetch Labels in repository {repo_name} (Status code: {response.status_code})")


    def create_label(self, repo_name, label_name, color):
        url = f'https://api.github.com/repos/username/{repo_name}/labels'
        data = {
            'name': label_name,
            'color': color
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Label '{label_name}' created in repository {repo_name} successfully.")
        else:
            print(f"Failed to create label '{label_name}' in repository {repo_name} (Status code: {response.status_code})")


    def delete_label(self, repo_name, label_name):
        url = f'https://api.github.com/repos/username/{repo_name}/labels/{label_name}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Label '{label_name}' deleted from repository {repo_name} successfully.")
        else:
            print(f"Failed to delete label '{label_name}' from repository {repo_name} (Status code: {response.status_code})")


    def manage_milestones(self, repo_name):
    url = f'https://api.github.com/repos/username/{repo_name}/milestones'
    response = requests.get(url, headers=self.headers)
    if response.status_code == 200:
        milestones = response.json()
        print(f"Milestones in repository {repo_name}:")
        for milestone in milestones:
            print(f"Title: {milestone['title']}, Description: {milestone['description']}")
    else:
        print(f"Failed to fetch Milestones in repository {repo_name} (Status code: {response.status_code})")


    def create_milestone(self, repo_name, title, description=None, due_date=None):
        url = f'https://api.github.com/repos/username/{repo_name}/milestones'
        data = {
            'title': title,
            'description': description,
            'due_on': due_date
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Milestone '{title}' created in repository {repo_name} successfully.")
        else:
            print(f"Failed to create milestone '{title}' in repository {repo_name} (Status code: {response.status_code})")


    def update_milestone(self, repo_name, milestone_number, title=None, description=None, due_date=None, state=None):
        url = f'https://api.github.com/repos/username/{repo_name}/milestones/{milestone_number}'
        data = {}
        if title:
            data['title'] = title
        if description:
            data['description'] = description
        if due_date:
            data['due_on'] = due_date
        if state:
            data['state'] = state
        response = requests.patch(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Milestone {milestone_number} updated successfully in repository {repo_name}.")
        else:
            print(f"Failed to update milestone {milestone_number} in repository {repo_name} (Status code: {response.status_code})")


    def delete_milestone(self, repo_name, milestone_number):
        url = f'https://api.github.com/repos/username/{repo_name}/milestones/{milestone_number}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Milestone {milestone_number} deleted successfully from repository {repo_name}.")
        else:
            print(f"Failed to delete milestone {milestone_number} from repository {repo_name} (Status code: {response.status_code})")


    def protect_branch(self, repo_name, branch_name, required_status_checks=None, enforce_admins=None, required_pull_request_reviews=None, restrictions=None):
        url = f'https://api.github.com/repos/username/{repo_name}/branches/{branch_name}/protection'
        data = {}
        if required_status_checks:
            data['required_status_checks'] = required_status_checks
        if enforce_admins is not None:
            data['enforce_admins'] = enforce_admins
        if required_pull_request_reviews:
            data['required_pull_request_reviews'] = required_pull_request_reviews
        if restrictions:
            data['restrictions'] = restrictions
        response = requests.put(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Branch protection set up successfully for branch '{branch_name}' in repository {repo_name}.")
        else:
            print(f"Failed to set up branch protection for branch '{branch_name}' in repository {repo_name} (Status code: {response.status_code})")


    def unprotect_branch(self, repo_name, branch_name):
        url = f'https://api.github.com/repos/username/{repo_name}/branches/{branch_name}/protection'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Branch protection removed successfully for branch '{branch_name}' in repository {repo_name}.")
        else:
            print(f"Failed to remove branch protection for branch '{branch_name}' in repository {repo_name} (Status code: {response.status_code})")


    def list_repository_hooks(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/hooks'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            hooks = response.json()
            print(f"Repository hooks in repository {repo_name}:")
            for hook in hooks:
                print(f"ID: {hook['id']}, Name: {hook['name']}, Events: {hook['events']}")
        else:
            print(f"Failed to fetch repository hooks in repository {repo_name} (Status code: {response.status_code})")
 
 
    def create_repository_hook(self, repo_name, hook_name, hook_config):
        url = f'https://api.github.com/repos/username/{repo_name}/hooks'
        data = {
            'name': hook_name,
            'config': hook_config,
            'events': ['push', 'pull_request', 'issues']
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Repository hook '{hook_name}' created successfully in repository {repo_name}.")
        else:
            print(f"Failed to create repository hook '{hook_name}' in repository {repo_name} (Status code: {response.status_code})")


    def update_repository_hook(self, repo_name, hook_id, hook_config):
        url = f'https://api.github.com/repos/username/{repo_name}/hooks/{hook_id}'
        data = {
            'config': hook_config
        }
        response = requests.patch(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Repository hook {hook_id} updated successfully in repository {repo_name}.")
        else:
            print(f"Failed to update repository hook {hook_id} in repository {repo_name} (Status code: {response.status_code})")


    def delete_repository_hook(self, repo_name, hook_id):
        url = f'https://api.github.com/repos/username/{repo_name}/hooks/{hook_id}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Repository hook {hook_id} deleted successfully from repository {repo_name}.")
        else:
            print(f"Failed to delete repository hook {hook_id} from repository {repo_name} (Status code: {response.status_code})")


    def list_repository_topics(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/topics'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            topics = response.json()['names']
            print(f"Repository topics in repository {repo_name}:")
            for topic in topics:
                print(topic)
        else:
            print(f"Failed to fetch repository topics in repository {repo_name} (Status code: {response.status_code})")


    def add_repository_topic(self, repo_name, topic):
        url = f'https://api.github.com/repos/username/{repo_name}/topics'
        data = {
            'names': [topic]
        }
        response = requests.put(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Topic '{topic}' added successfully to repository {repo_name}.")
        else:
            print(f"Failed to add topic '{topic}' to repository {repo_name} (Status code: {response.status_code})")


    def remove_repository_topic(self, repo_name, topic):
        url = f'https://api.github.com/repos/username/{repo_name}/topics'
        data = {
            'names': [topic]
        }
        response = requests.delete(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Topic '{topic}' removed successfully from repository {repo_name}.")
        else:
            print(f"Failed to remove topic '{topic}' from repository {repo_name} (Status code: {response.status_code})")


    def list_repository_collaborators(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/collaborators'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            collaborators = response.json()
            print(f"Collaborators in repository {repo_name}:")
            for collaborator in collaborators:
                print(collaborator['login'])
        else:
            print(f"Failed to fetch collaborators in repository {repo_name} (Status code: {response.status_code})")


    def add_repository_collaborator(self, repo_name, collaborator_username, permission='push'):
        url = f'https://api.github.com/repos/username/{repo_name}/collaborators/{collaborator_username}'
        data = {
            'permission': permission
        }
        response = requests.put(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Added collaborator {collaborator_username} to repository {repo_name} with permission level '{permission}'.")
        else:
            print(f"Failed to add collaborator {collaborator_username} to repository {repo_name} (Status code: {response.status_code})")


    def remove_repository_collaborator(self, repo_name, collaborator_username):
        url = f'https://api.github.com/repos/username/{repo_name}/collaborators/{collaborator_username}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Removed collaborator {collaborator_username} from repository {repo_name}.")
        else:
            print(f"Failed to remove collaborator {collaborator_username} from repository {repo_name} (Status code: {response.status_code})")

    def list_repository_releases(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/releases'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            releases = response.json()
            print(f"Releases in repository {repo_name}:")
            for release in releases:
                print(f"Name: {release['name']}, Tag: {release['tag_name']}, URL: {release['html_url']}")
        else:
            print(f"Failed to fetch releases in repository {repo_name} (Status code: {response.status_code})")


    def create_repository_release(self, repo_name, tag_name, target_commitish=None, name=None, body=None, draft=False, prerelease=False):
        url = f'https://api.github.com/repos/username/{repo_name}/releases'
        data = {
            'tag_name': tag_name,
            'target_commitish': target_commitish,
            'name': name,
            'body': body,
            'draft': draft,
            'prerelease': prerelease
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Release '{tag_name}' created successfully in repository {repo_name}.")
        else:
            print(f"Failed to create release '{tag_name}' in repository {repo_name} (Status code: {response.status_code})")


    def update_repository_release(self, repo_name, release_id, name=None, body=None, draft=None, prerelease=None):
        url = f'https://api.github.com/repos/username/{repo_name}/releases/{release_id}'
        data = {}
        if name:
            data['name'] = name
        if body:
            data['body'] = body
        if draft is not None:
            data['draft'] = draft
        if prerelease is not None:
            data['prerelease'] = prerelease
        response = requests.patch(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Release {release_id} updated successfully in repository {repo_name}.")
        else:
            print(f"Failed to update release {release_id} in repository {repo_name} (Status code: {response.status_code})")


    def delete_repository_release(self, repo_name, release_id):
        url = f'https://api.github.com/repos/username/{repo_name}/releases/{release_id}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Release {release_id} deleted successfully from repository {repo_name}.")
        else:
            print(f"Failed to delete release {release_id} from repository {repo_name} (Status code: {response.status_code})")


    def list_repository_projects(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/projects'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            projects = response.json()
            print(f"Projects in repository {repo_name}:")
            for project in projects:
                print(f"Name: {project['name']}, ID: {project['id']}")
        else:
            print(f"Failed to fetch projects in repository {repo_name} (Status code: {response.status_code})")

    def create_repository_project(self, repo_name, project_name, body=None):
        url = f'https://api.github.com/repos/username/{repo_name}/projects'
        data = {
            'name': project_name,
            'body': body
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Project '{project_name}' created successfully in repository {repo_name}.")
        else:
            print(f"Failed to create project '{project_name}' in repository {repo_name} (Status code: {response.status_code})")

    def delete_repository_project(self, repo_name, project_id):
        url = f'https://api.github.com/projects/{project_id}'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"Project {project_id} deleted successfully from repository {repo_name}.")
        else:
            print(f"Failed to delete project {project_id} from repository {repo_name} (Status code: {response.status_code})")


    def enable_repository_pages(self, repo_name, source_branch='main'):
        url = f'https://api.github.com/repos/username/{repo_name}/pages'
        data = {
            'source': {
                'branch': source_branch,
                'path': '/'
            }
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"GitHub Pages enabled successfully for repository {repo_name}.")
        else:
            print(f"Failed to enable GitHub Pages for repository {repo_name} (Status code: {response.status_code})")


    def disable_repository_pages(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/pages'
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print(f"GitHub Pages disabled successfully for repository {repo_name}.")
        else:
            print(f"Failed to disable GitHub Pages for repository {repo_name} (Status code: {response.status_code})")


    def get_repository_license(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/license'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            license_info = response.json()
            print(f"License information for repository {repo_name}:")
            print(f"License: {license_info['license']['name']}")
        else:
            print(f"Failed to fetch license information for repository {repo_name} (Status code: {response.status_code})")


    def list_repository_topics(self, repo_name):
        url = f'https://api.github.com/repos/username/{repo_name}/topics'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            topics = response.json()['names']
            print(f"Repository topics in repository {repo_name}:")
            for topic in topics:
                print(topic)
        else:
            print(f"Failed to fetch repository topics in repository {repo_name} (Status code: {response.status_code})")


    def add_repository_topic(self, repo_name, topic):
        url = f'https://api.github.com/repos/username/{repo_name}/topics'
        data = {
            'names': [topic]
        }
        response = requests.put(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Topic '{topic}' added successfully to repository {repo_name}.")
        else:
            print(f"Failed to add topic '{topic}' to repository {repo_name} (Status code: {response.status_code})")


    def remove_repository_topic(self, repo_name, topic):
        url = f'https://api.github.com/repos/username/{repo_name}/topics'
        data = {
            'names': [topic]
        }
        response = requests.delete(url, headers=self.headers, json=data)
        if response.status_code == 200:
            print(f"Topic '{topic}' removed successfully from repository {repo_name}.")
        else:
            print(f"Failed to remove topic '{topic}' from repository {repo_name} (Status code: {response.status_code})")


    @staticmethod
    def display_repositories_with_numbers(repos):
        for i, repo in enumerate(repos, start=1):
            print(f"{i}. {repo['name']}")

def main():
    github_manager = GitHubRepoManager('YOUR_TOKEN')

    while True:
        print("\nMenu:")
        print("0. Quit")
        print("1. Make public repositories private")
        print("2. Make private repositories public")
        print("3. Change visibility of specific repository")
        print("4. List all public repositories")
        print("5. List all private repositories")
        print("6. List all repositories")
        print("7. List files in a repository")
        print("8. Send commit to a repository")
        print("9. List branches in a repository")
        print("10. Create pull request in a repository")
        print("11. List issues in a repository")
        print("12. List projects in a repository")
        print("13. List wikis in a repository")
        print("14. List secrets in a repository")
        print("15. List collaborators in a repository")
        print("16. List deployments in a repository")
        print("17. List actions in a repository")
        print("18. List webhooks in a repository")
        print("19. List teams")
        print("20. List reports for user's repositories")
        print("21. Create an issue in a repository")
        print("22. List labels in a repository")
        print("23. Create a label in a repository")
        print("24. Delete a label in a repository")
        print("25. List milestones in a repository")
        print("26. Create a milestone in a repository")
        print("27. Update a milestone in a repository")
        print("28. Delete a milestone in a repository")
        print("29. Protect a branch in a repository")
        print("30. Unprotect a branch in a repository")
        print("31. List repository hooks")
        print("32. Create repository hook")
        print("33. Update repository hook")
        print("34. Delete repository hook")
        print("35. List repository topics")
        print("36. Add repository topic")
        print("37. Remove repository topic")
        print("38. List repository collaborators")
        print("39. Add repository collaborator")
        print("40. Remove repository collaborator")
        print("41. List repository releases")
        print("42. Create repository release")
        print("43. Update repository release")
        print("44. Delete repository release")
        print("45. List repository projects")
        print("46. Create repository project")
        print("47. Delete repository project")
        print("48. Enable repository pages")
        print("49. Disable repository pages")
        print("50. Get repository license")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting program...")
            break
        elif choice == '1':
            github_manager.change_visibility_bulk(github_manager.get_user_repositories(visibility='public'), visibility=False)
        elif choice == '2':
            github_manager.change_visibility_bulk(github_manager.get_user_repositories(visibility='private'), visibility=True)
        elif choice == '3':
            repo_name = input("Enter the repository name: ")
            visibility = input("Enter 'public' to make it public, 'private' to make it private: ")
            github_manager.change_visibility(repo_name, visibility)
        elif choice == '4':
            public_repos = github_manager.get_user_repositories(visibility='public')
            print("Public Repositories:")
            for repo in public_repos:
                print(repo['name'])
        elif choice == '5':
            private_repos = github_manager.get_user_repositories(visibility='private')
            print("Private Repositories:")
            for repo in private_repos:
                print(repo['name'])
        elif choice == '6':
            all_repos = github_manager.get_user_repositories()
            print("All Repositories:")
            for repo in all_repos:
                print(repo['name'])
        elif choice == '7':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_files(repo_name)
        elif choice == '8':
            repo_name = input("Enter the repository name: ")
            commit_message = input("Enter commit message: ")
            files = input("Enter files: ")
            github_manager.send_commit(repo_name, commit_message, files)
        elif choice == '9':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_branches(repo_name)
        elif choice == '10':
            repo_name = input("Enter the repository name: ")
            title = input("Enter pull request title: ")
            body = input("Enter pull request body: ")
            head = input("Enter head: ")
            base = input("Enter base: ")
            github_manager.create_pull_request(repo_name, title, body, head, base)
        elif choice == '11':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_issues(repo_name)
        elif choice == '12':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_projects(repo_name)
        elif choice == '13':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_wikis(repo_name)
        elif choice == '14':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_secrets(repo_name)
        elif choice == '15':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_collaborators(repo_name)
        elif choice == '16':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_deployments(repo_name)
        elif choice == '17':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_actions(repo_name)
        elif choice == '18':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_webhooks(repo_name)
        elif choice == '19':
            github_manager.list_teams()
        elif choice == '20':
            github_manager.manage_reports()
        elif choice == '21':
            repo_name = input("Enter the repository name: ")
            title = input("Enter issue title: ")
            body = input("Enter issue body: ")
            github_manager.create_issue(repo_name, title, body)
        elif choice == '22':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_labels(repo_name)
        elif choice == '23':
            repo_name = input("Enter the repository name: ")
            label_name = input("Enter label name: ")
            color = input("Enter label color: ")
            github_manager.create_label(repo_name, label_name, color)
        elif choice == '24':
            repo_name = input("Enter the repository name: ")
            label_name = input("Enter label name to delete: ")
            github_manager.delete_label(repo_name, label_name)
        elif choice == '25':
            repo_name = input("Enter the repository name: ")
            github_manager.manage_milestones(repo_name)
        elif choice == '26':
            repo_name = input("Enter the repository name: ")
            title = input("Enter milestone title: ")
            description = input("Enter milestone description: ")
            due_on = input("Enter due date (YYYY-MM-DD): ")
            github_manager.create_milestone(repo_name, title, description, due_on)
        elif choice == '27':
            repo_name = input("Enter the repository name: ")
            milestone_number = input("Enter milestone number to update: ")
            title = input("Enter new milestone title (leave empty to keep current): ")
            description = input("Enter new milestone description (leave empty to keep current): ")
            due_on = input("Enter new due date (YYYY-MM-DD) (leave empty to keep current): ")
            github_manager.update_milestone(repo_name, milestone_number, title, description, due_on)
        elif choice == '28':
            repo_name = input("Enter the repository name: ")
            milestone_number = input("Enter milestone number to delete: ")
            github_manager.delete_milestone(repo_name, milestone_number)
        elif choice == '29':
            repo_name = input("Enter the repository name: ")
            branch_name = input("Enter branch name: ")
            github_manager.protect_branch(repo_name, branch_name)
        elif choice == '30':
            repo_name = input("Enter the repository name: ")
            branch_name = input("Enter branch name: ")
            github_manager.unprotect_branch(repo_name, branch_name)
        elif choice == '31':
            github_manager.list_repository_hooks()
        elif choice == '32':
            github_manager.create_repository_hook()
        elif choice == '33':
            hook_id = input("Enter hook ID to update: ")
            github_manager.update_repository_hook(hook_id)
        elif choice == '34':
            hook_id = input("Enter hook ID to delete: ")
            github_manager.delete_repository_hook(hook_id)
        elif choice == '35':
            github_manager.list_repository_topics()
        elif choice == '36':
            topic = input("Enter topic to add: ")
            github_manager.add_repository_topic(topic)
        elif choice == '37':
            topic = input("Enter topic to remove: ")
            github_manager.remove_repository_topic(topic)
        elif choice == '38':
            github_manager.list_repository_collaborators()
        elif choice == '39':
            username = input("Enter username of collaborator to add: ")
            github_manager.add_repository_collaborator(username)
        elif choice == '40':
            username = input("Enter username of collaborator to remove: ")
            github_manager.remove_repository_collaborator(username)
        elif choice == '41':
            repo_name = input("Enter the repository name: ")
            github_manager.list_repository_releases(repo_name)
        elif choice == '42':
            repo_name = input("Enter the repository name: ")
            tag_name = input("Enter tag name for the release: ")
            target_commitish = input("Enter target commitish: ")
            name = input("Enter name for the release: ")
            body = input("Enter body for the release: ")
            github_manager.create_repository_release(repo_name, tag_name, target_commitish, name, body)
        elif choice == '43':
            repo_name = input("Enter the repository name: ")
            release_id = input("Enter release ID to update: ")
            tag_name = input("Enter new tag name for the release: ")
            target_commitish = input("Enter new target commitish: ")
            name = input("Enter new name for the release: ")
            body = input("Enter new body for the release: ")
            github_manager.update_repository_release(repo_name, release_id, tag_name, target_commitish, name, body)
        elif choice == '44':
            repo_name = input("Enter the repository name: ")
            release_id = input("Enter release ID to delete: ")
            github_manager.delete_repository_release(repo_name, release_id)
        elif choice == '45':
            repo_name = input("Enter the repository name: ")
            github_manager.list_repository_projects(repo_name)
        elif choice == '46':
            repo_name = input("Enter the repository name: ")
            name = input("Enter name for the project: ")
            body = input("Enter body for the project: ")
            github_manager.create_repository_project(repo_name, name, body)
        elif choice == '47':
            repo_name = input("Enter the repository name: ")
            project_id = input("Enter project ID to delete: ")
            github_manager.delete_repository_project(repo_name, project_id)
        elif choice == '48':
            repo_name = input("Enter the repository name: ")
            github_manager.enable_repository_pages(repo_name)
        elif choice == '49':
            repo_name = input("Enter the repository name: ")
            github_manager.disable_repository_pages(repo_name)
        elif choice == '50':
            repo_name = input("Enter the repository name: ")
            github_manager.get_repository_license(repo_name)
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()