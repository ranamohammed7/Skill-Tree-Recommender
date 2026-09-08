import re
from colorama import Fore,init
from skill_tree import Skill_Tree_Recommender
from career_matcher import CareerAdvisor
from scheduler import SkillLevelScheduler
from data_manager import DataManager
from cli import Cli_Interface
cli = Cli_Interface()
init()
print(Fore.GREEN+"""
                                                               ███████╗██╗  ██╗██╗██╗     ██╗     
                                                               ██╔════╝██║ ██╔╝██║██║     ██║     
                                                               ███████╗█████╔╝ ██║██║     ██║     
                                                               ╚════██║██╔═██╗ ██║██║     ██║     
                                                               ███████║██║  ██╗██║███████╗███████╗
                                                               ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                                                               
                                                                     🌳TREE RECOMMENDER🌳
"""+Fore.RESET)
while True:
    print("\n============ 🚀 SKILL "+Fore.GREEN+ "TREE" +Fore.RESET+" SYSTEM =============")
    print("1. User Access"+Fore.RESET)
    print("2. Admin Access")
    print(Fore.RED+"0. Exit"+Fore.RESET)
    print("="*47,"\n")

    main_choice = input("Select Portal: ").strip()
    match main_choice:
      case "1":
        while True:
          cli.show_user_menu()
          choice = input("Enter your choice: ")

          match choice:
           case "1":
             tracks = cli.tree_manager.get_all_tracks()
             print("\nAvailable Tracks:")
             for idx, track in enumerate(tracks, start=1):
                print(f"{idx}. {track}")

           case "2":
             track_name = input("Enter Track Name: ").strip()
             print(cli.tree_manager.get_Prequirements(track_name))

           case "3":
              track_name = input("Enter Track Name: ").strip()
              current_skill = input("Enter Your Current Skill: ").strip()
              print("\n Next Step: ")
              print(cli.tree_manager.get_path(track_name, current_skill))
        
           case"4":
              user_skills = input("Enter Your Current Skills : ")
              recommendations = cli.advisor.recommend_paths(user_skills)
              if recommendations:
                  print(Fore.GREEN+"\n============ RECOMMENDED CARRER PATHS ============"+Fore.RESET)
                  has_matches = False

                  for idx, (path_name, match_percentage, missing_courses) in enumerate(recommendations, start=1):
                       if match_percentage > 0:
                           has_matches = True
                           print(f"{idx}. Track: {path_name} ")
                           print(f"   Match Percentage: {match_percentage}")
                           if missing_courses:
                               print(f"   Missing Skills: {', '.join(missing_courses)} ")
                           else:
                               print(" You Have All Required Skills For This Track!")
                  if not has_matches:
                      print(Fore.RED+"\n No Matching Tracks Found With Match Rate > 0%"+Fore.RESET)

           case "5":
              print("\n--- ⏱️  Skill Hours & Level Analysis ---")
              skills_name = input("Enter Skill(s) Name: ").strip().lower()
              skills_list = [skill.strip() for skill in re.split(r'[,-/\\-]+', skills_name) if skill.strip()]

              if skills_list:
                  target_level = input("Enter Target Level (Beginner, Intermediate, Advanced): ").strip().capitalize()
                  total_hours = 0
                  found_any = False

                  print(f"\n Hours Breakdown For Level '{target_level}':")
                  for skill in skills_list:
                      hours = cli.scheduler.calculate_total_hours(skill, target_level)
                      if hours is not None:
                            print(f"  • {skill.title()}: {hours} Hours")
                            total_hours += hours
                            found_any = True
                      else:
                          print(Fore.RED,f"  • {skill.title()}: Level Or Skill Not Found!"+Fore.RESET)

                  if found_any:
                         print("-" * 35)
                         print(f"  Total Hours Required: {total_hours} Hours")
              else:
                  print(Fore.RED+"\n No Skills Entered"+Fore.RESET)
              

           case "6":
                print("\n--- 📅 Generate Study Schedule ---")
                print("1. Schedule for an entire Track")
                print("2. Schedule for Custom Skills")
                    
                schedule_choice = input("Enter Your Choice (1 Or 2): ").strip()
                skills_list = []

                if schedule_choice == "1":
                    track_name = input("Enter Track Name: ").strip().title()
                    if cli.is_track_exists(track_name):
                        skills_list = cli.tree_manager.roadmaps[track_name]
                        print(f"\n Skills Loaded For {track_name}: {', '.join(skills_list)}")
                    else:
                        print(Fore.RED,f"\n Track '{track_name}' Not Found."+Fore.RESET)
                        continue
                            
                elif schedule_choice == "2":
                    skills_input = input("Enter Skills: ").strip().lower()
                    skills_list = [skill.strip() for skill in re.split(r'[,-/\\-]+' , skills_input) if skill.strip()]
                    
                else:
                     print(Fore.RED+"\n Invalid Choice!"+Fore.RESET)
                     continue

                if skills_list:
                    target_level = input("Enter Target Level (Beginner, Intermediate, Advanced): ").strip()
                    weekly_hours = input("Enter Available Study Hours Per Week: ").strip()
                        
                    if weekly_hours.isdigit() and int(weekly_hours) > 0:
                            cli.scheduler.calculate_schedule(skills_list, target_level, int(weekly_hours))
                    else:
                        print(Fore.RED+"\n Invalid Hours! Please Enter A Valid Number"+Fore.RESET)

           case "7":
              print("\n--- Save Your Study Plan ---")
              user_name = input("Enter Your Name: ").strip().title()
              print("1. Save Plan for an entire Track")
              print("2. Save Plan for Custom Skills")
                    
              save_choice = input("Enter Your Choice (1 Or 2): ").strip()
              skills_list = []
              target_name = ""

              if save_choice == "1":
                    target_name = input("Enter Track Name: ").strip().title()
                    if cli.is_track_exists(target_name):
                        skills_list = cli.tree_manager.roadmaps[target_name]
                    else:
                        print(Fore.RED,f"\n❌ Track '{target_name}' Not Found."+Fore.RESET)
                        continue
                            
              elif save_choice == "2":
                    target_name = input("Enter Plan/Skills Title (e.g., My Skills Plan): ").strip()
                    skills_input = input("Enter Skills (Comma or Slash Separated): ").strip()
                    clean_input = skills_input.replace('/', ',')
                    skills_list = [s.strip() for s in clean_input.split(',') if s.strip()]
              else:
                    print(Fore.RED+"\n❌ Invalid Choice."+Fore.RESET)
                    continue

              if skills_list:
                    weekly_hours = input("Enter Available Study Hours Per Week: ").strip()
                    target_level = input("Enter Target Level (Beginner, Intermediate, Advanced): ").strip().title()
                        
                    if weekly_hours.isdigit() and int(weekly_hours) > 0 :
                        total_hours = cli.scheduler.calculate_schedule_for_path(skills_list, target_level)
                        weeks_needed = (total_hours + int(weekly_hours) - 1) // int(weekly_hours)
                    else:
                        print(Fore.RED+"\n❌ Invalid Hours! Please Enter A Valid Number."+Fore.RESET)
                        continue
                    if target_level in ['Beginner','Intermediate','Advanced']:
                        cli.data_mgr.save_user_plan(user_name, target_name, skills_list, weeks_needed)
                    else:
                        print(Fore.RED+'Invalid Level,Please Try (Beginner,Intermediate,Advanced)'+Fore.RESET)
                        continue
             
           case "8":
                  user_name = input("Enter Your Name: ").strip().title()
                  skill = input("Enter The Skill(s) Completed: ").strip().lower()

                  completed_skills_list = [s.strip() for s in re.split(r'[,-/\\-]+' , skill) if s.strip()]
                  if completed_skills_list:
                      cli.data_mgr.mark_skill_completed(user_name, completed_skills_list)
                  else:
                      print(Fore.RED+"\n[!] No Skills Entered"+Fore.RESET)

           case "9":
              user_name = input("Enter Your Name: ").strip().title()
              plan_content = cli.data_mgr.load_user_plan(user_name)
              print(f"\n--- {user_name}'s Plan ---")
              print(plan_content)

           case "10":
              user_name = input("Enter Your Name: ").strip().title()
              cli.data_mgr.export_final_report(user_name)

           case "0":
              break
              
           case _:
              print(Fore.RED+"Invalid Choice. Please Try Again (From 0 To 10)."+Fore.RESET)

      case "2":
        if cli.admin_login():
            while True:
                cli.show_admin_menu()
                admin_choice = input("Enter Admin Choice: ").strip()

                match admin_choice:
                    case "1":
                        track_name = input("Enter New Track Name: ").strip()
                        if not cli.is_track_exists:
                            print(Fore.RED,f"\n Track {track_name} Already Exists"+Fore.RESET)
                        else:
                            skills_input = input("Enter Skills (Comma-Seprated) or press Enter to skip :")
                            skills_list = [s.strip() for s in skills_input.split(',') if s.strip()]
                            cli.tree_manager.add_track(track_name , skills_list)
                            print(Fore.GREEN,f"\n Track {track_name.title()} Added Successfully"+Fore.RESET)
                    case "2":
                        track_name = input("Enter Existing Track Name: ").strip()
                        skill_to_add = input("Enter Skill to Add: ").strip()
                        result = cli.tree_manager.add_skill_to_track(track_name , skill_to_add)
                        if result:
                            print(f"\n{result}")
                        else:
                            print(Fore.GREEN,f"\n Skill '{skill_to_add.title()}' Added To Track '{track_name.title()}'"+Fore.RESET)
                    case "3":
                        track_name=input("Enter Track Name TO REMOVE: ")
                        print(Fore.RED+'WARNING: Now You Are REMOVING A TRACK'+Fore.RESET)
                        is_sure=input("ENTER 'Y' TO CONTINUE OR 'N' TO EXIT: ").upper()
                        if is_sure=='Y':
                           cli.tree_manager.remove_track(track_name)
                        else:
                            print(Fore.MAGENTA+'RETURNING BACK TO THE MENU WITHOUT REMOVING THE TRACK!'+Fore.RESET)
                            continue
                    case "4":
                        track_name=input("Enter Existing Track TO REMOVE SKILL FROM IT: ")
                        skill_name=input("Enter The Skill To REMOVE: ")
                        is_sure=input(Fore.RED+"ENTER 'Y' TO CONTINUE OR 'N' TO EXIT: "+Fore.RESET).upper()
                        if is_sure=='Y':
                           cli.tree_manager.remove_skill(track_name,skill_name)
                        else:
                            print(Fore.MAGENTA+'RETURNING BACK TO THE MENU WITHOUT REMOVING THE Skill!'+Fore.RESET)
                            continue
                    case "0":
                        break
                    case _ :
                        print(Fore.RED+"\n Invalid Choice,Please Try Again (From 0 To 4)"+Fore.RESET)
      case "0":
        print(Fore.GREEN+"""\n
                                                                  ███████╗████████╗ █████╗ ██╗   ██╗
                                                                  ██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝
                                                                  ███████╗   ██║   ███████║ ╚████╔╝
                                                                  ╚════██║   ██║   ██╔══██║  ╚██╔╝
                                                                  ███████║   ██║   ██║  ██║   ██║
                                                                  ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝
                                                       
                                                         ██████╗██╗   ██╗██████╗ ██╗ ██████╗ ██╗   ██╗███████╗
                                                        ██╔════╝██║   ██║██╔══██╗██║██╔═══██╗██║   ██║██╔════╝
                                                        ██║     ██║   ██║██████╔╝██║██║   ██║██║   ██║███████╗
                                                        ██║     ██║   ██║██╔══██╗██║██║   ██║██║   ██║╚════██║
                                                        ╚██████╗╚██████╔╝██║  ██║██║╚██████╔╝╚██████╔╝███████║
                                                         ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                       
                                                                          🌱 Keep Growing! 🌱
"""+Fore.RESET)
        break
      case _:
        print(Fore.RED+"\n Invalid Choise, Please Try Again (From 0 To 2)"+Fore.RESET)     