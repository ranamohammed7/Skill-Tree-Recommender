from skill_tree import Skill_Tree_Recommender
def show_menu():
    print('\n','='*50)
    print("Welcome to the Skill Tree Recommender!")
    print("Please Select An Option:")
    print("1. All Tracks We have:")
    print("2. Prerequisites For Your Track")
    print("3. Your Remaining Skills In Track")
    print("4. Add New Track")
    print("5. Add New Skill To Track That Already Exists")
    print("6. Exit")
    print('\n','='*50)


def get_remaining_skills():
        track_name = input("Enter the track name: ")
        Skill_Tree_Recommender().is_track_exist(track_name) 
        if Skill_Tree_Recommender().found==True:
          current_level = input("Enter Your Skills(comma-separated): ")
          Skill_Tree_Recommender().get_path(track_name, current_level)
    
def adding_track():
    track_name = input("Enter the track name: ")
    print(f"If You Want to Add Skills To Your new track: {track_name} Enter (Y) or (N) if you don't ")
    skill_choice = input("Enter your choice (Y/N): ")
    if skill_choice.upper() == 'Y':
       track_skills = input("Enter the skills for the track (comma-separated): ")
       Skill_Tree_Recommender().add_track(track_name, track_skills)
    else:
         Skill_Tree_Recommender().add_track(track_name)

def adding_skill_to_track():
    track_name = input("Enter the track name: ")
    if Skill_Tree_Recommender().exist==True:
       skill = input("Enter the skill name: ")
       Skill_Tree_Recommender().add_skill_to_track(track_name, skill)
    else:
        print("Track isn't found! Add it first!")



while True:
 show_menu()
 choice = input("Enter your choice (1-6): ")
 match choice:
    case "1":
        Skill_Tree_Recommender().get_all_tracks()
    case "2":
        track_name = input("Enter the track name: ")
        Skill_Tree_Recommender().get_Prequirements(track_name)
    case "3":
        get_remaining_skills()
    case "4":
        adding_track()
    case "5":
        adding_skill_to_track()
    case "6":
        print("Thank you for using the Skill Tree Recommender!")
        break
