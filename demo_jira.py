from jira import JIRA


options={'server':'https://crm.monumetric.com'}
jira=JIRA(options=options,basic_auth=('rinku','R8ik,9ol.'))
issue = jira.issue('MAIN-226')


print("\n*********",jira.__dict__)
print("\n",jira.projects())
print("\nissue", issue.key)
print("\ndescription", issue.fields.description)
print("\nassigne", issue.fields.assignee.displayName)
print("\nstatus", issue.fields.status.name)
print("\nstatus", issue.fields.status)
print("\nvelocity",issue.fields.customfield_10200)
print("\npriority",issue.fields.priority)

