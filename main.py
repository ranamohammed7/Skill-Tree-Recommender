from skill_tree import Skill_Tree_Recommender
from career_matcher import CareerAdvisor
from scheduler import SkillLevelScheduler
from data_manager import DataManager

class Cli_Interface:
    def __init__(self):
        self.tree_manager = Skill_Tree_Recommender()
        self.advisor = CareerAdvisor(self.tree_manager.roadmaps)
        self.scheduler = SkillLevelScheduler()
        self.data_mgr = DataManager()

    def show_menu(self):
        print("\n============ SKILL-TREE RECOMMENDER =============")
        print("1. View All Tracks")
        print("2. View Track Prequirements")
        print("3. View Your Next Skill in Track")
        print("4. Add New Track (Admins Only)")
        print("5. Add Skill to Existing Track (Admins Only)")
        print("6. Recommend Career Paths")
        print("7. View Skill Levels")
        print("8. Total Hours Required For a Skill level")
        print("9. Total Study Hours Required For a Path")
        print("10. Generate a Study Schedule for a Learning Path")
        print("11. Save Your Plan")
        print("12. Load Your Plan")
        print("13. Export Final Report")
        print("0. Exit")
        print('='*50,'\n')

    def admins(self,name,password):
        admins_names=['Rana','Mariam','Trevena','Jana','Zeinab']
        if name.lower() in [n.lower() for n in admins_names] and password == "admin":
            return True
        else:
            return False

    def is_track_exists(self, track_name):
        return track_name.title().strip() in self.tree_manager.roadmaps


cli = Cli_Interface()
while True:
    
    cli.show_menu()
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            tracks = cli.tree_manager.get_all_tracks()
            print("\nAvailable Tracks:")
            for idx, track in enumerate(tracks, start=1):
                print(f"{idx}. {track}")

        case "2":
            track_name = input("Enter The Track Name: ")
            print(cli.tree_manager.get_Prequirements(track_name))

        case "3":
            track_name = input("Enter The Track Name: ")
            current_skill = input("Enter Your Current Skill: ")  
            print(cli.tree_manager.get_path(track_name, current_skill))
        

        case "4":
           print("Admin authentication required to add a new track.")
           admin_name = input("Enter Your Admin Name: ")
           admin_password = input("Enter Your Admin Password: ")
           if not cli.admins(admin_name, admin_password):
              print("Authentication failed. You Do Not Have Permission To Add a New Track.")
              continue
           else:
               print("Authentication Successful. You Can Add a New Track.")
               track_name = input("Enter The New Track Name: ")
               if cli.is_track_exists(track_name):
                 print(f"Track '{track_name}' Already Exists. Please Choose a Different Name.")
                 continue
               else:
                 print("Enter The Skills For This Track (Comma-Separated). If You Want To Add Skills Later, Just Leave It Empty.")
                 skills_input = input("Enter Skills for This Track (Comma-Separated): ")
                 skills_list = [skill.strip() for skill in skills_input.split(",") if skill.strip()]
                 cli.tree_manager.add_track(track_name, skills_list)
                 print(f"Track '{track_name}' Added Successfully.")

        case "5":
          track_name = input("Enter The Existing Track Name: ")
          skill_to_add = input("Enter The Skill to Add: ")
          result = cli.tree_manager.add_skill_to_track(track_name, skill_to_add)
          if result:
            print(result)
          else:
            print(f"Skill '{skill_to_add}' Added To Track '{track_name}'.")

        case"6":
          user_skills = input("Enter Your Skills (Comma-Separated): ")
          recommendations = cli.advisor.recommend_paths(user_skills)
          print("\nRecommended Career Paths:")
          for idx, (path_name, match_percentage, missing_courses) in enumerate(recommendations, start=1):
             print(f"{idx}. {path_name} - Match: {match_percentage}% - Missing Skills: {', '.join(missing_courses)}")

        case "7":
          skill_name = input("Enter The Skill Name to Get Levels: ")
          levels = cli.scheduler.get_skill_levels(skill_name)
          print(f"\nSkill Levels For {skill_name}")
          for level, hours in levels.items():
            print(f"{level}: {hours} Hours")

        case"8":
          skill_name = input("Enter The Skill Name: ")
          target_level = input("Enter The Target Level (Beginner, Intermediate, Advanced): ")
          hours = cli.scheduler.calculate_total_hours(skill_name, target_level)
          if hours is not None:
            print(f"\nTotal hours Required To Reach {target_level} Level in {skill_name}: {hours} Hours")
          else:
              print(f"Level '{target_level}' Not Found For Skill '{skill_name}'. Choose From: Beginner, Intermediate, Advanced")

        case "9":
          skills_input = input("Enter The skills For The Path (Comma-Separated): ").strip().lower().split(',')
          skills_list = [skill.strip() for skill in skills_input if skill.strip()]
          target_level = input("Enter The Target Level (Beginner, Intermediate, Advanced): ")
          total_hours = cli.scheduler.calculate_schedule_for_path(skills_list, target_level)
          if total_hours==0:
              print(f"Level '{target_level}' Not Found. Choose from: Beginner, Intermediate, Advanced")
          else:
              print(f"\nTotal Study Hours Required for the Path at {target_level} Level: {total_hours} Hours")

        case "10":
          skills_input = input("Enter The skills For The Path (Comma-Separated): ").strip().lower().split(',')
          skills_list = [skill.strip() for skill in skills_input if skill.strip()]
          target_level = input("Enter The Target Level (Beginner, Intermediate, Advanced): ")
          weekly_hours = input("Enter The Number of Hours You Can Dedicate Per Week: ")
          cli.scheduler.calculate_schedule(skills_list, target_level, weekly_hours)
        case "11":
            user_name = input("Enter Your Name: ")
            target_track = input("Enter Your Target Track: ").title().strip()
            duration_weeks = input("Enter The Estimated Duration in Weeks: ")
            missing_skills_input = input("Enter The Missing Skills (Comma-Separated): ")
            cli.data_mgr.save_user_plan(
                user_name, target_track, [skill.strip() for skill in missing_skills_input.split(",") if skill.strip()], duration_weeks)
        case "12":
            user_name = input("Enter Your Name: ")
            plan_content = cli.data_mgr.load_user_plan(user_name)
            print(f"\n--- {user_name}'s Plan ---")
            print(plan_content)
        case "13":
            user_name = input("Enter Your Name: ")
            target_track = input("Enter Your Target Track: ").title().strip()
            completed_skills_input = input("Enter The Completed Skills (Comma-Separated): ")
            cli.data_mgr.export_final_report(user_name, target_track, [skill.strip() for skill in completed_skills_input.split(",") if skill.strip()])

        case "0":
            print("Exiting The Program. Goodbye!")
            break
        case _:
            print("Invalid choice. Please Try Again (from 0 to 13).")