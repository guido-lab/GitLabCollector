import requests, json
import pandas as pd


class GilLbabCollector:
    def __init__(self):
        pass

    def collect_data(gitlabGroup):
        query = """
        {
        group(fullPath: "gitlab_group") {
            name
            projects {
            nodes {
                name
            }
            }
            groupMembers {
            nodes {
                user {
                username
                name
                }
            }
            }
            projects {
            nodes {
                name
                projectMembers {
                nodes {
                    user {
                    username
                    name
                    }
                }
                }
            }
            }
        }
        }
        """

        query = query.replace('gitlab_group', gitlabGroup)
        url = 'https://gitlab.com/api/graphql'
        request = requests.post(url, json={'query': query})
        print(request.status_code)
        json_data = json.loads(request.text)

        projects = json_data['data']['group']['projects']['nodes']
        projects_df = pd.DataFrame(projects)
        projects_df.to_csv('projects_df.csv', sep=',')

        groupMembers = json_data['data']['group']['groupMembers']['nodes']
        groupMembers_df = pd.DataFrame(groupMembers)
        groupMembers_df.to_csv('groupMembers.csv', sep=',')

        projectMembers = json_data['data']['group']['projects']['nodes']
        projectMembers_df = pd.DataFrame(projectMembers)
        projectMembers_df.to_csv('projectMembers.csv', sep=',')



glg = input("Enter GitLab GroupName: ")
GilLbabCollector.collect_data(gitlabGroup = glg)