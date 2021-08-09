# GitLabCollector

## Tasker - Requirements
1. Write a script that receives a Gitlab group (e.g. gitlab-org) as a mandatory parameter.
2. The script should extract the following information:
- All projects in the group
- All users in the group
- User per project
3. The script should store all the above information.
4. You can use Gitlab’s API (either Graphql or REST) or an external Gitlab client.
#
## Clone Project:
Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/guido-lab/GitLabCollector.git
```
#
## How to run 
The following command creates a new virtual environment named venv in the current directory:

```bash
python -m venv env
```

Activate virtual environment:

```bash
(Mac/Linux) $ source env/bin/activate
```

```bash
(Windows) $ source env/Scripts/activate
```

Install Dependencies:

```
pip install -r requirements.txt
```

Running the script to collect the data from GitLab

```
python getGitlabGroups.py
```
Executing the script in terminal, it will ask to add a GitLab Group as parameter (eg. gitlab-org)

After the exection is finishted, in the same directory will be places three CSV with the required data.