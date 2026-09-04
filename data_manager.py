class DataManager:

    def save_user_plan(
        self, user_name, target_track, missing_skills, duration_weeks
    ):
        file_path = f"{user_name}_progress.txt"
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("=== SKILL-TREE RECOMMENDER USER PROGRESS ===\n")
                file.write(f"User Name: {user_name}\n")
                file.write(f"Target Track: {target_track}\n")
                file.write(f"Estimated Duration: {duration_weeks} Weeks\n")
                file.write("--- Remaining Skills to Learn ---\n")
                for skill in missing_skills:
                    file.write(f"- {skill}\n")
                file.write("===========================================\n")
            print("\n[✔] Progress saved successfully!")
            return True
        except Exception as e:
            print(f"\n[✖] Error saving progress: {e}")
            return False

    def load_user_plan(self , user_name):
        file_path = f"{user_name}_progress.txt"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                if not content.strip():
                    return "File is empty."
                return content
        except FileNotFoundError:
            return "No previous progress found. Please create a new plan first."
        except Exception as e:
            return f"Error loading progress: {e}"

    def export_final_report(self, user_name, target_track, completed_skills):
        
        report_file = f"{user_name}_final_report.txt"
        try:
            with open(report_file, "w", encoding="utf-8") as file:
                file.write("=========================================\n")
                file.write("       OFFICIAL COMPLETION REPORT        \n")
                file.write("=========================================\n")
                file.write(f"Student: {user_name}\n")
                file.write(f"Track: {target_track}\n")
                file.write("-----------------------------------------\n")
                file.write("Skills Mastered:\n")
                for idx, skill in enumerate(completed_skills, 1):
                    file.write(f" {idx}. {skill}\n")
                file.write("=========================================\n")
                file.write("Status: Completed Successfully!\n")
            print(f"\n[✔] Final report exported to {report_file}")
        except Exception as e:
            print(f"\n[✖] Failed to export report: {e}")