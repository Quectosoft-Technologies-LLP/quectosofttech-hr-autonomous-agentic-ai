class AgentRegistry:
    _agents = {}
    @classmethod
    def register(cls, name, agent):
        cls._agents[name] = agent
    @classmethod
    def get(cls, name):
        return cls._agents[name]
    @classmethod
    def list(cls):
        return dict(cls._agents)
