class WorkspaceRegistry:
    def __init__(self):
        self.workspaces = {}
    def register(self, workspace_id, meta):
        self.workspaces[workspace_id] = meta
    def get(self, workspace_id):
        return self.workspaces.get(workspace_id)
GLOBAL_WORKSPACES = WorkspaceRegistry()
