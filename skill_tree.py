class Skill_Tree_Recommender:
    #track_name= track_name.title().strip()    عما أفكر فيها
    def __init__(self):
      self.roadmaps = {
            "Backend Developer": ["C++", "OOP", "Algorithms", "Data Structures"],
            "Frontend Developer": ["HTML", "CSS", "JavaScript", "React"],
            "AI": ["Python", "Linear Algebra", "Machine Learning", "Deep Learning"]
        }

      # print(self.roadmaps)


    # لو لسه مبتديء وعايز الخريطة كاملة
    def get_Prequirements(self,track_name):
        return f" The full path :" ,self.roadmaps.get(track_name.title().strip() , "This track is not found")
        # حذفت المسافة من اليمين والشمال وخليته يكبر الحرف في أول الكلمة


    def get_path(self,track_name,current_level):
        path=[]
        roadmap  = self.roadmaps.get(track_name.title().strip())
        # print(roadmap)

        if not roadmap :
            return f"This track is not found"

        if current_level in roadmap:
            idx = roadmap.index(current_level)
            if idx + 1 < len(roadmap):
                path += roadmap[idx+1:]
                print("Remaining Steps :" , " --> ".join(path))
                return f"The next skill: {roadmap[idx + 1]}"
            else:
                return f" Congratulations! You finish this track!"
        else:
            return f" this skill is not required."

    def add_track(self,track_name,skill=None):
        skills = []
        if skill != None:
          skills = [skill]
        self.roadmaps.update({track_name.title().strip() : skills})
        # if isinstance(skill, list):
        #     skills_list = skill
        # else:
        #     skills_list = [skill]


    def add_skill_to_track(self,track_name ,skill):
        track_name = track_name.title().strip()
        if track_name in self.roadmaps:
          self.roadmaps[track_name].append(skill)
        else:
          return f"Track isn't found! Add it first!"

manager = Skill_Tree_Recommender()
print(manager.get_Prequirements("   Backend developer"))
print(manager.get_path("Backend Developer", "OOP"))
manager.add_track("Data Analyst")

# manager = Skill_Tree_Recommender()  مينفعش أعملها كده هيبدأ من جديد
