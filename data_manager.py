from colorama import Fore,init
import os

class DataManager:

  def save_user_plan(self, user_name, target_track_or_skills, skills_list, duration_weeks):
        file_path = f"{user_name}_progress.txt"
        try:
            with open(file_path, "w",encoding="utf-8") as file:
                file.write("===========================================\n")
                file.write("   SKILL-TREE RECOMMENDER USER PROGRESS    \n")
                file.write("===========================================\n")
                file.write(f"User Name: {user_name}\n")
                file.write(f"Target Track/Skills: {target_track_or_skills}\n")
                file.write(f"Estimated Duration: {duration_weeks} Weeks\n")
                file.write("-------------------------------------------\n")
                file.write("--- Roadmap Skills Status ---\n")
                for skill in skills_list:
                    file.write(f"[ ] {skill}\n")
                file.write("===========================================\n")
            print(Fore.GREEN,f"\n[OK] Progress Plan Created Successfully In {file_path}!"+Fore.RESET)
            return True
        except Exception as e:
            print(Fore.RED,f"\n[!] Error Saving Progress: {e}"+Fore.RESET)
            return False

  def mark_skill_completed(self, user_name, completed_skill_list):
        file_path = f"{user_name}_progress.txt"
        if not os.path.exists(file_path):
            print(Fore.RED+"\n No Progress File Found! Please Create A Plan First!"+Fore.RESET)
            return False

        try:
            with open(file_path, "r",encoding="utf-8") as file:
                lines = file.readlines()

            skills_to_mark = [s.strip().lower() for s in completed_skill_list if s.strip()]
            updated_count = 0
            new_lines = []

            for line in lines:
                if line.startswith("[ ]") :
                    skill_in_file = line.replace("[ ]", "").strip()
                    if skill_in_file.lower() in skills_to_mark:
                       line = line.replace("[ ]", "[✅]")
                       updated_count += 1
                new_lines.append(line)

            if updated_count > 0:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.writelines(new_lines)
                print(Fore.GREEN,f"\n Successfully marked '{updated_count}' skill(s) as Completed!"+Fore.RESET)
                return True
            else:
                print(Fore.RED,f"\n None Of The Entered Skills Were Found As Pending In Your Roadmap."+Fore.RESET)
                return False

        except Exception as e:
            print(Fore.RED,f"\n[!] Error Updating Skill: {e}"+Fore.RESET)
            return False

  def load_user_plan(self, user_name):
        file_path = f"{user_name}_progress.txt"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                if not content.strip():
                    return Fore.RED+"File Is Empty."+Fore.RESET
                return content
        except FileNotFoundError:
            return Fore.RED+"No Previous Progress Found. Please Create A Plan First."+Fore.RESET
        except Exception as e:
            return Fore.RED,f"Error Loading Progress: {e}"+Fore.RESET

  def export_final_report(self, user_name):
        file_path = f"{user_name}_progress.txt"
        
        if not os.path.exists(file_path):
            print(Fore.RED+"\n❌ Cannot generate certificate: No progress file found!"+Fore.RESET)
            return False

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            pending_skills = []
            completed_skills = []
            target_track = "Custom Roadmap"

            for line in lines:
                if line.startswith("Target Track/Skills:"):
                    target_track = line.split(":", 1)[1].strip()
                elif line.startswith("[ ]"):
                    pending_skills.append(line.replace("[ ]", "").strip())
                elif line.startswith("[✅]"):
                    completed_skills.append(line.replace("[✅]", "").strip())

            if pending_skills:
                print(Fore.RED+"\n================ ⚠️  ROADMAP INCOMPLETE ================"+Fore.RESET)
                print(f"Sorry {user_name}, You Haven't Finished All Skills In Your File Yet.")
                print("Remaining Skills You Need To Complete:")
                for skill in pending_skills:
                    print(f"  • {skill}")
                print("=======================================================")
                return False

            if not completed_skills:
                print(Fore.RED+"\n❌ No skills found in your progress file."+Fore.RESET)
                return False

            report_file = f"{user_name}_final_report.txt"
            with open(report_file, "w",encoding="utf-8") as file:
                file.write("=========================================\n")
                file.write("      OFFICIAL COMPLETION CERTIFICATE🎉    \n")
                file.write("=========================================\n")
                file.write(f"Student Name : {user_name}\n")
                file.write(f"Roadmap      : {target_track}\n")
                file.write("-----------------------------------------\n")
                file.write("Skills Mastered:\n")
                for idx, skill in enumerate(completed_skills, 1):
                    file.write(f"  {idx}. {skill}\n")
                file.write("-----------------------------------------\n")
                file.write("Status: ALL ROADMAP SKILLS MASTERED! \n")
                file.write("=========================================\n")
            
            print(f"\n🎓 Congratulations {user_name}! Final Report & Certificate Exported To {report_file}")
            return True

        except Exception as e:
            print(Fore.RED,f"\n[✖] Failed to export report: {e}"+Fore.RESET)
            return False
