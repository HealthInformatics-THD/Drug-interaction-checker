import streamlit as st
from logic.Drug_Database import DrugDatabase
from logic.interaction_checker import InteractionChecker

def main():
    st.title("💊 Drug Interaction Checker")
    st.write("Pick your medications to see if any known issues exist.")

    db = DrugDatabase()
    checker = InteractionChecker(db)

    all_drugs = sorted(
        set(
            list(db.interactions.keys())
            + [drug for group in db.interactions.values() for drug in group.keys()]
        )
    )

    selected = st.multiselect("Choose Medications", options=all_drugs)

    if st.button("Check Interactions"):
        if len(selected) < 2:
            st.error("You’ll need to pick at least two medications.")
            return

        results = checker.check_interactions(selected)

        if results:
            st.warning("⚠️ Possible interactions found:")
            for m1, m2, detail in results:
                st.markdown(f"**{m1} ↔ {m2}**\n\n🩺 {detail}")
        else:
            st.success("✅ No known interactions detected.")

if __name__ == "__main__":
    main()