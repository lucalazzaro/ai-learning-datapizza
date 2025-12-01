# main.py
from unittest import result
from pipeline import run_pipeline

def main():
    print("=== AI Learning Crew (Datapizza Edition) ===\n")

    role = input("Target role (default: AI/ML Engineer): ").strip() or "AI/ML Engineer"
    profile = input("\nDescribe your background: ")

    result = run_pipeline(profile, role)

    print("\n=== ROADMAP ===\n")
    print(result["roadmap"])

    print("\n=== RESOURCES ===\n")
    print(result["resources"])

    print("\n=== STUDY PLAN ===\n")
    print(result["study_plan"])

if __name__ == "__main__":
    main()

