from model.UserResponse import UserResponse

class ResponseController():
    
    def findAll(self):
        return UserResponse.objects.all()
    
    def findOne(self, id_user):
        return UserResponse.objects(id_user=id_user)

    def findUserQuiz(self, id_user, id_quiz):
        return UserResponse.objects(id_user=id_user, id_quiz=id_quiz)        
