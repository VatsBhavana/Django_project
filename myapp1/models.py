from django.db import models



# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField(default=456)
    role=models.CharField(max_length=30)
    created_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.email

class AdminUser(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=15)

    pic=models.FileField(upload_to="media/images/",default="media/admin.png")

    def __str__(self):
        return self.username+"("+self.user_id.email+")"
    
class learners(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=15)
    city=models.CharField(max_length=60,blank=True,null=True)
    gender=models.CharField(max_length=10,blank=True,null=True)
    qualification=models.CharField(max_length=30,blank=True,null=True)
    primary_language=models.CharField(max_length=30,blank=True,null=True)
    status=models.BooleanField(default=False)
    
    pic=models.FileField(upload_to="media/images/",default="media/boy_default.png")

    def save(self, *args, **kwargs):
        if not self.pic or self.pic == "media/boy_default.png":  # Default image logic
            if self.gender == "female":
                self.pic = "media/girl_default.png"
            else:
                self.pic = "media/boy_default.png"
        super().save(*args, **kwargs) 


    def __str__(self):
        return self.username+"("+self.user_id.email+")"    
    
class category(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    category_name=models.CharField(max_length=30)
    category_pic=models.FileField(upload_to="media/images",default="media/category.png")
    
    def __str__(self):
        return self.category_name
    
class course(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30)
    course_duration=models.CharField(max_length=60)
    fees=models.CharField(max_length=16)
    course_discription=models.TextField()
    course_lecture_flow=models.FileField(upload_to="media/lecture_flow/")
    course_handbook=models.FileField(upload_to="media/handbook/")
    course_interview_question=models.FileField(upload_to="media/interviewpreperation/")
    course_assignment=models.FileField(upload_to="media/assignment/")
    course_pic=models.FileField(upload_to="media/images",default="media/course_pic.png")
    course_tutor_name=models.CharField(max_length=60)
    video = models.URLField(max_length=500, blank=True, null=True)
    quiz = models.URLField(max_length=500, blank=True, null=True)  # For quiz/exam links


    
class company(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=30)
    company_address=models.CharField(max_length=60)
    company_discription=models.TextField()
    company_email=models.EmailField(max_length=30,unique=True)
    company_pic=models.FileField(upload_to="media/images",default="media/tata.png")
    contact_no=models.CharField(max_length=15)
    company_website=models.CharField(max_length=30)

class enrollcourse(models.Model):
     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
     learner_id=models.ForeignKey(learners,on_delete=models.CASCADE)
     course_id=models.ForeignKey(course,on_delete=models.CASCADE)
     created_at=models.DateField(auto_now=True)
     status=models.CharField(max_length=30,default="pending")
     fees_status=models.CharField(max_length=20)
     paid_fees=models.IntegerField(default=0)



