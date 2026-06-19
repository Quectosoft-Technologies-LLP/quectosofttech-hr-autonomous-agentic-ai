class RAIDStore:
    def __init__(self):
        self.entries = []
    def add(self, item):
        self.entries.append(item)
    def all(self):
        return list(self.entries)
    def summary(self):
        counts = {"low": 0, "medium": 0, "high": 0, "critical": 0}
        for item in self.entries:
            zone = item.get("zone", "low")
            counts[zone] = counts.get(zone, 0) + 1
        return {"counts": counts, "total": len(self.entries)}
GLOBAL_RAID_STORE = RAIDStore()
