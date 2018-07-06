from jira import JIRA
import re

def conn(username, password):
    username = "zhangshumin"
    password = "Ycfabc"
    jira = JIRA('http://jira.yaochufa.com:8080', basic_auth=('username', 'password'))

#def get_jira_info(request):
    if request.method == "POST":
        PPID = request.POST.get('PPID')
    #PPID=4117
    issue = jira.issue("PP-%s" %PPID)
    # get project & branch
    pub_list = issue.fields.customfield_10302.split()
    pub = []
    i = 0
    while i < len(pub_list):
        project = pub_list[i]
        branch = pub_list[i + 1]
        i += 2
        pub.append("%s %s" % (project, branch))