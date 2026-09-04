class Skill_Tree_Recommender:
    def __init__(self):
      self.roadmaps = {
            "Backend Developer": ["C++", "OOP", "Data Structures","Algorithms","SQL","Databases", "Git"],
            "Frontend Developer": ["HTML", "CSS", "JavaScript", "TypeScript", "React" , "Web Performance" , "Git"],
            "AI Engineer": ["Python", "Linear Algebra",  "Calculus" , "Data Structures", "Machine Learning", "Deep Learning",],
            "Cyber Security": ["Linux" , "Networking" ,"Python","Web Security", "Ethical Hacking"]
        }
      
    def get_all_tracks(self):
        return list(self.roadmaps.keys())
    
    def get_Prequirements(self,track_name):
        return f" The full path : {self.roadmaps.get(track_name.title().strip() , 'This track is not found')}"
    
    def get_path(self,track_name,current_level):
        path=[]
        roadmap  = self.roadmaps.get(track_name.title().strip())
        if not roadmap :
            return f"This track is not found"
        current_level_clean = current_level.strip().lower()
        roadmap_lower = [s.lower() for s in roadmap]
        if current_level_clean in roadmap_lower:
            idx = roadmap_lower.index(current_level_clean)
            if idx + 1 < len(roadmap):
                path += roadmap[idx+1:]
                print("Remaining Steps :" , " --> ".join(path))
                return f"The next skill: {roadmap[idx + 1]}"
            else:
                return f" Congratulations! You finish this track!"
        else:
            return f" this skill is not required."
        
    def add_track(self,track_name,skill=None):
           if isinstance(skill, list) :
               skills = skill
           elif skill is not None:
               skills = [skill]
           else: 
               skills = []
          
           self.roadmaps.update({track_name.title().strip() : skills})
    def add_skill_to_track(self,track_name ,skill):
        track_name = track_name.title().strip()
        if track_name in self.roadmaps:
          self.roadmaps[track_name].append(skill)
        else:
          return f"Track isn't found! Add it first!"