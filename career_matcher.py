class CareerAdvisor :
    def __init__(self, carrer_data):
        self.carrer_data = carrer_data
        
    def Clean_skills (self , user_input):
        CleanSkills = user_input.lower()
        CleanSkills1 = CleanSkills.split(',')
        CleanSkills2 = set( skill.strip() for skill in CleanSkills1 if skill.strip())
        return CleanSkills2
    
    def recommend_paths(self , user_input) :
        """
        Take a seprated string with comma of user input 
        and returns a sorted list of tuples: (path_name , match_percentage , missing_courses)
        """
        cl_skills =  self.Clean_skills(user_input)
        results = []
        for path_name , path_skills in self.carrer_data.items ():
           path_skills_set = set(s.lower() for s in path_skills)
           intersection_courses = path_skills_set & cl_skills
           missing_courses = path_skills_set - cl_skills
           match_percentage = round((len(intersection_courses) / len(path_skills_set)) * 100 , 2)
           results.append ((path_name ,match_percentage , list(missing_courses)))
        info = sorted(results, key = lambda x : x[1] , reverse= True)
        return info 