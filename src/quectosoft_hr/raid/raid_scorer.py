class RAIDScorer:
    def score(self, entry):
        return entry.likelihood * entry.impact
