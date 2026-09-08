from colorama import Fore,init
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

    def admin_login(self):
        print("\n--- 🔐 Admin Login ---")
        name= input("Enter Admin Name: ").strip()
        password = input("Enter admin password: ").strip()
        admins_names = ['Rana' , 'Mariam' , 'Trevena' , 'Jana' , 'Zainab']

        if name.title() in  admins_names and password == "admin":
            print(f"\n Welcome, Admin {name.title()}!")
            return True
        else:
            print(Fore.RED+"Inncorrect Admin or Password!"+Fore.RESET)
            return False


    def show_user_menu(self):
        print("\n============ 🎓 USER MENU =============")
        print("1. View All Tracks")
        print("2. View Track Prequirements")
        print("3. View Your Next Skill in Track")
        print("4. Recommend Career Paths")
        print("5. View Skill Levels & Calculate Required Study Hours")
        print("6. Generate a Study Schedule for a Learning Path")
        print("7. Save Your Plan")
        print("8. Update Progress (Mark Skill Completed)")
        print("9. Load Your Plan")
        print("10. Export Final Report")
        print(Fore.RED+"0. Exit"+Fore.RESET)
        print('='*50,'\n')

    def show_admin_menu(self):
        print("\n============ ADMIN MENU =============")
        print("1. ADD NEW TRACK")
        print("2. ADD SKILL TO EXISTING TRACK")
        print("3. REMOVE EXISTING TRACK")
        print("4. REMOVE SKILL FROM A TRACK")
        print(Fore.RED+"0. Exit"+Fore.RESET)
        print('=' *52,'\n')

    def is_track_exists(self, track_name):
        return track_name.title().strip() in self.tree_manager.roadmaps