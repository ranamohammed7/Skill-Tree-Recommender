from colorama import Fore
import re


class CareerAdvisor :
    def __init__(self, carrer_data):
        self.carrer_data = carrer_data
        
    def Clean_skills (self , user_input):
        try:
            if not isinstance(user_input , str) or not user_input.strip():
                raise ValueError(Fore.RED+"Please Enter At Least One Skill"+Fore.RESET)
            
            clean_input = user_input.lower()

            raw_skills = re.split(r'[,-/\\-]+' , clean_input)
            clean_skills_set = {skill.strip() for skill in raw_skills if skill.strip()}

            if not clean_skills_set:
                raise ValueError(Fore.RED+"No valid skills found, try again"+Fore.RESET)
            return clean_skills_set
        
        except ValueError as e:
            print(f"[!] {e}")
            return set()
        except Exception:
            print(Fore.RED+"Something Went Wrong, Please Try Again"+Fore.RESET)
            return set()
        
    def recommend_paths(self , user_input) :
        """
        Take a seprated string with comma of user input 
        and returns a sorted list of tuples: (path_name , match_percentage , missing_courses)
        """
        try:
            cl_skills =  self.Clean_skills(user_input)
            if not cl_skills:        
                return []
            results = []
            for path_name , path_skills in self.carrer_data.items ():
                path_skills_set = set(s.lower() for s in path_skills)

                intersection_courses = path_skills_set & cl_skills
                missing_courses = path_skills_set - cl_skills

                match_percentage = round((len(intersection_courses) / len(path_skills_set)) * 100 , 2)
                results.append ((path_name , match_percentage , list(missing_courses)))

            info = sorted(results, key = lambda x : x[1] , reverse= True)
            return info 
        except Exception: 
              print(Fore.RED+"[!] Unable To Generate Recommendations"+Fore.RESET)
              return []
