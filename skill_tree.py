import re
class Skill_Tree_Recommender:
    found = True
    exist = False
    def __init__(self):
      self.roadmaps = {
            "Backend Developer": ["C++", "OOP", "Data Structures","Algorithms","SQL","Databases", "Git"],
            "Frontend Developer": ["HTML", "CSS", "JavaScript", "TypeScript", "React" , "Web Performance" , "Git"],
            "AI Engineer": ["Python", "Linear Algebra",  "Calculus" , "Data Structures", "Machine Learning", "Deep Learning",],
            "Cyber Security": ["Linux" , "Networking" ,"Python","Web Security", "Ethical Hacking"]
        }
      
    def get_all_tracks(self):
        print('All Tracks We Have:',list(self.roadmaps.keys()))
    
    def get_Prequirements(self,track_name):
        print(f"{self.roadmaps.get(track_name.title().strip() , 'This track is not found')}")

    def is_track_exist(self,track_name):
        roadmap  = self.roadmaps.get(track_name.title().strip(','))

        if not roadmap :
            Skill_Tree_Recommender.found = False
            print(f"This track is not found")
            return
        Skill_Tree_Recommender.found = True

    def get_path(self,track_name,current_level):
        roadmap  = self.roadmaps.get(track_name.title().strip(','))
        current_level=[skill.strip().title() for skill in current_level.split(',')]
        roadmap=[skill.title() for skill in roadmap]
        path=roadmap.copy()
        for skill in current_level:
            if skill in path:
                path.remove(skill)
            else:
              print(f" {skill} is not required.")
              
            if not path:
                print(f" Congratulations! You have finished this track!")
                return
        else:
            print(f" Your remaining skills in {track_name.title().strip()} track are:")
            print(*[f' {i}.{skill}' for i, skill in enumerate(path,1)], sep=' \n')
        
    def add_track(self,track_name,skill=None):
           track_name=re.search(track_name.strip(),' '.join(self.roadmaps.keys()),re.IGNORECASE)
           if track_name in self.roadmaps:
               print(f"Track already exists!")
           else:
              if isinstance(skill, list) :
                skills = skill
              elif skill is not None:
                skills =[ s.strip() for s in skill.split(',')]
              else: 
                skills = [] 
              self.roadmaps.update({str(track_name).title().strip() : skills})

    def add_skill_to_track(self,track_name ,skill):
        track_name = track_name.title().strip()
        if track_name in self.roadmaps:
          self.exist=True
          self.roadmaps[track_name].append(skill)
        else:
          self.exist=False

# manager = Skill_Tree_Recommender()
# print(manager.get_Prequirements("   Backend developer"))
# print(manager.get_path("Backend Developer", "OOP"))
# manager.add_track("Data Analyst")

# manager = Skill_Tree_Recommender()  مينفعش أعملها كده هيبدأ من جديد
