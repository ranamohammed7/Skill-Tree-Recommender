from colorama import Fore


class Skill_Tree_Recommender:
    def __init__(self):
      self.roadmaps = {
            "Backend Developer": ["C++", "OOP", "Data Structures","Algorithms","SQL","Databases", "Git"],
            "Frontend Developer": ["HTML", "CSS", "JavaScript", "TypeScript", "React" , "Web Performance" , "Git"],
            "Ai Engineer": ["Python", "Linear Algebra",  "Calculus" , "Data Structures", "Machine Learning", "Deep Learning",],
            "Cyber Security": ["Linux" , "Networking" ,"Python","Web Security", "Ethical Hacking"]
        }
      
    def get_all_tracks(self):
        return list(self.roadmaps.keys())
    
    def get_Prequirements(self,track_name):
        return f" The full path : {self.roadmaps.get(track_name.title().strip() , 'This Track Is Not Found')}"
    
    def get_path(self,track_name,current_level):
        path=[]
        roadmap  = self.roadmaps.get(track_name.title().strip())
        if not roadmap :
            return Fore.RED+"This Track Is Not Found"+Fore.RESET
        current_level_clean = current_level.strip().lower()
        roadmap_lower = [s.lower() for s in roadmap]
        if current_level_clean in roadmap_lower:
            idx = roadmap_lower.index(current_level_clean)
            if idx + 1 < len(roadmap):
                path += roadmap[idx+1:]
                print("Remaining Steps :" , " --> ".join(path))
                return f"The Next Skill: {roadmap[idx + 1]}"
            else:
                return f" Congratulations! You Finish This Track!"
        else:
            return Fore.RED+" This Skill Is Not Required."+Fore.RESET
        
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
          return Fore.RED+"Track Isn't Found! Add It First!"+Fore.RESET


    def remove_skill (self , track_name , skill= None):
        track_name = track_name.strip().title()
        if track_name in self.roadmaps:
            roadmap = self.roadmaps.get(track_name)
            roadmap_lower = [s.lower() for s in roadmap]
            print(f"Skills of {track_name} : {roadmap_lower}")
            if skill:
                if skill.lower() in roadmap_lower:
                    idx = roadmap_lower.index(skill.lower())
                    del roadmap[idx]          
                    print(Fore.RED,f"'{skill.title()}' removed from {track_name.title()}",Fore.RESET)
                else:
                    print(Fore.RED,f"'{skill.title()}' not found in {track_name.title()}",Fore.RESET)
        else:
            print(Fore.RED,f"Track '{track_name.title()}' not found",Fore.RESET)   


    def remove_track (self , track_name):
        track_name = track_name.title().strip()
        if track_name in self.roadmaps :
            del self.roadmaps[track_name]
            print(Fore.RED,f'{track_name.title()} Deleted !',Fore.RESET)
        else:
            print(Fore.RED,f"{track_name.title()} Doesn't Exist TO REMOVE !",Fore.RESET)
