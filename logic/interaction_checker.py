class InteractionChecker:
    """Handles the main logic for detecting any overlapping drug interactions."""

    def __init__(self, db):
        self.db = db

    def check_interactions(self, meds):
        meds = [m.strip() for m in meds if m.strip()]
        found = []

        for i in range(len(meds)):
            for j in range(i + 1, len(meds)):
                m1, m2 = meds[i], meds[j]
                if m1 in self.db.interactions and m2 in self.db.interactions[m1]:
                    found.append((m1, m2, self.db.interactions[m1][m2]))
                elif m2 in self.db.interactions and m1 in self.db.interactions[m2]:
                    found.append((m2, m1, self.db.interactions[m2][m1]))
        return found