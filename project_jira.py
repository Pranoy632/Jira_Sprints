from jira import JIRA


class Connect:

    server = 'https://crm.monumetric.com'
    boards = ["TM3 board"]
    def connect_jira(self, jira_user, jira_password):

        """
        Connect to JIRA

        """
        if not hasattr(self, 'connection'):
            try:
                
                jira_options = {'server': self.server}
                jira = JIRA(options=jira_options,basic_auth=(jira_user,jira_password))
                
                self.connection = jira
            
            except Exception:
                print("Failed to connect to JIRA")
                return None
        return self.connection
    
        

    def get_board_ids(self):
        
        boards = self.connection.boards()
        board_ids = []
        for board in boards:
            if board.name in self.boards:
                board_ids.append(board.id)
                
        return board_ids
            
   
    def get_current_sprints(self):
        self.connect_jira("rinku", "R8ik,9ol.")
        board_ids = self.get_board_ids()
        current_sprints = []
        for board_id in board_ids:
            sprints = self.connection.sprints(board_id, state="active,")
            for sprint in sprints:
                if sprint.state == "ACTIVE" and sprint not in current_sprints:
                    current_sprints.append(sprint)
                
        print("********",current_sprints) 
        
         
        
        # issue = jira.issue('MAIN-226')
        
        # print("\n*********",jira.__dict__)
        # print("\n",jira.projects())
        # print("\nissue", issue.key)
        # print("\ndescription", issue.fields.description)
        # print("\nassigne", issue.fields.assignee.displayName)
        # print("\nstatus", issue.fields.status.name)
        # print("\nstatus", issue.fields.status)
        # print("\nvelocity",issue.fields.customfield_10200)
        # print("\npriority",issue.fields.priority)


obj = Connect()

print("********",dir(obj))
print(obj.get_current_sprints())
