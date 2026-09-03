from career_matcher import Skill_Tree_Recommender,CarrerAdvisor

class SkillLevelScheduler:
    def __init__(self):
        self.skills_hours = {
            "C++": {"Beginner": 20, "Intermediate": 35, "Advanced": 55},
            "OOP": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Data Structures": {"Beginner": 20, "Intermediate": 35, "Advanced": 50},
            "Algorithms": {"Beginner": 20, "Intermediate": 40, "Advanced": 60},
            "SQL": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "Databases": {"Beginner": 15, "Intermediate": 25, "Advanced": 40},
            "Git": {"Beginner": 5, "Intermediate": 10, "Advanced": 15},
            "HTML": {"Beginner": 10, "Intermediate": 15, "Advanced": 20},
            "CSS": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "JavaScript": {"Beginner": 20, "Intermediate": 35, "Advanced": 55},
            "TypeScript": {"Beginner": 15, "Intermediate": 25, "Advanced": 40},
            "React": {"Beginner": 20, "Intermediate": 35, "Advanced": 50},
            "Web Performance": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "Python": {"Beginner": 20, "Intermediate": 35, "Advanced": 50},
            "Linear Algebra": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Calculus": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Machine Learning": {"Beginner": 25, "Intermediate": 45, "Advanced": 65},
            "Deep Learning": {"Beginner": 25, "Intermediate": 45, "Advanced": 70},
            "Linux": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "Networking": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Web Security": {"Beginner": 15, "Intermediate": 30, "Advanced": 45},
            "Ethical Hacking": {"Beginner": 20, "Intermediate": 35, "Advanced": 55},
        }
        
        self.default_hours = {"Beginner": 15, "Intermediate": 25, "Advanced": 40}

    def get_skill_levels(self, skill_name):
        lower_skills = {k.lower(): v for k, v in self.skills_hours.items()}
        return lower_skills.get(skill_name.strip().lower(), self.default_hours)

    def calculate_total_hours(self, skill_name, target_level):
        levels = self.get_skill_levels(skill_name)
        target_level = target_level.strip().title()
        hours = levels.get(target_level)
        if hours is None:
            print(f"Level '{target_level}' not found. Choose from: Beginner, Intermediate, Advanced")
        return hours

    def calculate_schedule_for_path(self, skills_list, target_level="Advanced"):
        total_path_hours = 0
        for skill in skills_list:
            hours = self.calculate_total_hours(skill, target_level)
            if hours is not None:
                total_path_hours += hours
        return total_path_hours

    def calculate_schedule(self, skills_list, target_level):
        try:
            weekly_hours = int(input("How many hours per week are available to you? "))
            if weekly_hours <= 0:
                print("Weekly hours must be greater than zero")
                return

            skill_hours_list = []
            total_hours = 0
            for skill in skills_list:
                hours = self.calculate_total_hours(skill, target_level)
                if hours is not None:
                    skill_hours_list.append((skill, hours))
                    total_hours += hours

            if not skill_hours_list:
                print("No valid skills found for this level")
                return

            weeks_needed = round(total_hours / weekly_hours)
            print(f"\nTotal hours required: {total_hours} hours")
            print(f"Estimated duration: {weeks_needed} weeks\n")

            days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
            daily_hours = round(weekly_hours / 7)
            if daily_hours == 0:
                daily_hours = 1

            skill_index = 0
            remaining_in_skill = skill_hours_list[0][1]
            week_num = 1
            day_index = 0

            print(f"===== Week {week_num} =====")
            while skill_index < len(skill_hours_list):
                if day_index == 7:
                    day_index = 0
                    week_num += 1
                    print(f"\n===== Week {week_num} =====")

                day = days[day_index]
                hours_today = min(daily_hours, remaining_in_skill)
                current_skill = skill_hours_list[skill_index][0]
                print(f"{day} | \t {current_skill} | \t {hours_today} hours")

                remaining_in_skill -= hours_today

                if remaining_in_skill <= 0:
                    skill_index += 1
                    if skill_index < len(skill_hours_list):
                        remaining_in_skill = skill_hours_list[skill_index][1]
                day_index += 1

        except ValueError:
            print("Please enter a valid whole number, not text")


class SkillLevelScheduler:
    def __init__(self):
        self.skills_hours = {
            "C++": {"Beginner": 20, "Intermediate": 35, "Advanced": 55},
            "OOP": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Data Structures": {"Beginner": 20, "Intermediate": 35, "Advanced": 50},
            "Algorithms": {"Beginner": 20, "Intermediate": 40, "Advanced": 60},
            "SQL": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "Databases": {"Beginner": 15, "Intermediate": 25, "Advanced": 40},
            "Git": {"Beginner": 5, "Intermediate": 10, "Advanced": 15},
            "HTML": {"Beginner": 10, "Intermediate": 15, "Advanced": 20},
            "CSS": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "JavaScript": {"Beginner": 20, "Intermediate": 35, "Advanced": 55},
            "TypeScript": {"Beginner": 15, "Intermediate": 25, "Advanced": 40},
            "React": {"Beginner": 20, "Intermediate": 35, "Advanced": 50},
            "Web Performance": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "Python": {"Beginner": 20, "Intermediate": 35, "Advanced": 50},
            "Linear Algebra": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Calculus": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Machine Learning": {"Beginner": 25, "Intermediate": 45, "Advanced": 65},
            "Deep Learning": {"Beginner": 25, "Intermediate": 45, "Advanced": 70},
            "Linux": {"Beginner": 10, "Intermediate": 20, "Advanced": 30},
            "Networking": {"Beginner": 15, "Intermediate": 25, "Advanced": 35},
            "Web Security": {"Beginner": 15, "Intermediate": 30, "Advanced": 45},
            "Ethical Hacking": {"Beginner": 20, "Intermediate": 35, "Advanced": 55},
        }
        
        self.default_hours = {"Beginner": 15, "Intermediate": 25, "Advanced": 40}

    def get_skill_levels(self, skill_name):
        lower_skills = {k.lower(): v for k, v in self.skills_hours.items()}
        return lower_skills.get(skill_name.strip().lower(), self.default_hours)

    def calculate_total_hours(self, skill_name, target_level):
        levels = self.get_skill_levels(skill_name)
        target_level = target_level.strip().title()
        hours = levels.get(target_level)
        if hours is None:
            print(f"Level '{target_level}' not found. Choose from: Beginner, Intermediate, Advanced")
        return hours

    def calculate_schedule_for_path(self, skills_list, target_level="Advanced"):
        total_path_hours = 0
        for skill in skills_list:
            hours = self.calculate_total_hours(skill, target_level)
            if hours is not None:
                total_path_hours += hours
        return total_path_hours

    def calculate_schedule(self, skills_list, target_level):
        try:
            weekly_hours = int(input("How many hours per week are available to you? "))
            if weekly_hours <= 0:
                print("Weekly hours must be greater than zero")
                return

            skill_hours_list = []
            total_hours = 0
            for skill in skills_list:
                hours = self.calculate_total_hours(skill, target_level)
                if hours is not None:
                    skill_hours_list.append((skill, hours))
                    total_hours += hours

            if not skill_hours_list:
                print("No valid skills found for this level")
                return

            weeks_needed = round(total_hours / weekly_hours)
            print(f"\nTotal hours required: {total_hours} hours")
            print(f"Estimated duration: {weeks_needed} weeks\n")

            days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
            daily_hours = round(weekly_hours / 7)
            if daily_hours == 0:
                daily_hours = 1

            skill_index = 0
            remaining_in_skill = skill_hours_list[0][1]
            week_num = 1
            day_index = 0

            print(f"===== Week {week_num} =====")
            while skill_index < len(skill_hours_list):
                if day_index == 7:
                    day_index = 0
                    week_num += 1
                    print(f"\n===== Week {week_num} =====")

                day = days[day_index]
                hours_today = min(daily_hours, remaining_in_skill)
                current_skill = skill_hours_list[skill_index][0]
                print(f"{day} | \t {current_skill} | \t {hours_today} hours")

                remaining_in_skill -= hours_today

                if remaining_in_skill <= 0:
                    skill_index += 1
                    if skill_index < len(skill_hours_list):
                        remaining_in_skill = skill_hours_list[skill_index][1]
                day_index += 1

        except ValueError:
            print("Please enter a valid whole number, not text")


# To try the output
tree_manager = Skill_Tree_Recommender()
advisor = CarrerAdvisor(tree_manager.roadmaps)
scheduler = SkillLevelScheduler()
print(tree_manager.get_all_tracks())
print(tree_manager.get_Prequirements("Backend Developer"))
output = advisor.recommend_paths("c++ , oop")
print(output)

# testing the Scheduler on the Backend Developer track up to Intermediate level
backend_path = tree_manager.roadmaps["Backend Developer"]
total_hours = scheduler.calculate_schedule_for_path(backend_path, "Intermediate")
scheduler.calculate_schedule(backend_path, "Intermediate")

# testing the Scheduler on the Backend Developer track up to Intermediate level
backend_path = tree_manager.roadmaps["Backend Developer"]
total_hours = scheduler.calculate_schedule_for_path(backend_path, "Intermediate")
scheduler.calculate_schedule(backend_path, "Intermediate")