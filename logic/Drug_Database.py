class DrugDatabase:
    """Holds and manages known drug-to-drug interactions."""

    def __init__(self):
        # Define known interactions between common medications
        self.interactions = {
            "Aspirin": {
                "Warfarin": "Can increase bleeding risk",
                "Ibuprofen": "May reduce the blood-thinning benefits",
                "Clopidogrel": "Higher chance of bleeding complications",
            },
            "Warfarin": {
                "Aspirin": "Can increase bleeding risk",
                "NSAIDs": "Raises the chance of stomach or intestinal bleeding",
                "Vitamin K": "Can make the drug less effective",
                "Amiodarone": "May raise INR and bleeding likelihood",
            },
            "Ibuprofen": {
                "Aspirin": "Can weaken its heart protection benefits",
                "Prednisolone": "Might cause more stomach ulcers or irritation",
            },
            "Metformin": {
                "Contrast Dye": "Can increase risk of lactic acidosis",
                "Cimetidine": "May raise metformin concentration in the blood",
            },
            "Simvastatin": {
                "Clarithromycin": "Higher chance of muscle pain or damage",
                "Grapefruit Juice": "Can raise statin levels and toxicity",
            },
            "Digoxin": {
                "Amiodarone": "Increases digoxin toxicity risk",
                "Verapamil": "May raise digoxin concentration",
            },
            "ACE Inhibitors": {
                "Potassium Supplements": "Can cause high potassium levels",
                "NSAIDs": "Might reduce the blood pressure–lowering effect",
            },
            "SSRIs": {
                "Tramadol": "Possible serotonin syndrome risk",
                "MAO Inhibitors": "Severe serotonin syndrome danger",
            },
            "Oral Contraceptives": {
                "Rifampicin": "May lower contraceptive effectiveness",
                "Carbamazepine": "Could increase chance of contraceptive failure",
            },
        }