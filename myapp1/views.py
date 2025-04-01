from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import random
from .utils import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, learners, course, enrollcourse


# Create your views here.

def homepage(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)

            
            category_count = category.objects.count()
            course_count = course.objects.count()
            company_count = company.objects.count()

            
            last_5_categories = category.objects.all().order_by('-id')[:5]
            last_5_courses = course.objects.all().order_by('-id')[:5]
            last_5_companies = company.objects.all().order_by('-id')[:5]

            context={
                        'uid':uid,
                        'aid':aid,
                        'category_count': category_count,
                        'course_count': course_count,
                        'company_count': company_count,
                        'last_5_categories': last_5_categories,
                        'last_5_courses': last_5_courses,
                        'last_5_companies': last_5_companies,
                    }
            return render(request,"myapp/index.html",context)
        else:
          return render(request,"myapp/login.html")
    return render(request, "myapp/login.html")




def login(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            context={
                        'uid':uid,
                        'aid':aid,
                    }
                    #stored data in session
            #request.session['email']=email
            return render(request,"myapp/index.html",context)

    if request.POST:
        try:
            print("=======submit button press")
            email=request.POST["email"]
            password=request.POST["password"]

            uid=User.objects.get(email=email)

            if uid.password==password:
                if uid.role=="admin":
                    aid=AdminUser.objects.get(user_id = uid)
                    context={
                        'uid':uid,
                        'aid':aid,
                    }
                    request.session['email']=email
                    return render(request,"myapp/index.html",context)
                else:
                    lid=learners.objects.get(user_id=uid)
                    context={
                        'uid':uid,
                        'lid':lid,
                    }  
                    #stored data in session
                    request.session['email']=email
                    return render(request,"myapp/learner_index.html",context)
            else:
                context={
                    "e_msg":"invalid password"
                      }
                return render(request,"myapp/login.html",context)
            
            # print("something==============",uid)
            # return render(request,"myapp/index.html")
        except Exception as e:
            print("===============>",e)
            context={
                'e_msg':"invalid email or password"
            }
            return render(request,"myapp/login.html",context)
    else:
        print("=======only page referesh login page is here =======")
    return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")
    
def newlearner(request):
   if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        

        l1 = ['df456','67hj8','78hjk','jk880']
        password = random.choice(l1)+email[2:5]+contact_no[2:5]

        uid = User.objects.create(email = email,password = password,role="learners" )
        if uid :
            lid = learners.objects.create(
                user_id = uid,
                username = username,
                contact_no = contact_no,
                gender=gender,
               
                    )
            if lid:
                context = {
                's_msg' : "Successfully Account Created  : ) !! please check your email box for password",
                'gender': gender,
                'lid' :lid,
                'uid' :uid,
                'password' :password 
                }
                sendMail("PASSWORD","password_mail_template",email,context)
                return render(request,"myapp/login.html",context)
        else:
            context = {
                'e_msg' : "something went wrong!"
                }
            return render(request,"myapp/registration.html",context,{'gender': gender})

   else:
        return render(request,"myapp/registration.html")

def profile(request):
    if "email" in request.session:
            if  request.POST:
                print("==============> update page")
                uid=User.objects.get(email=request.session['email'])
                if uid.role=="admin":
                            aid=AdminUser.objects.get(user_id = uid)
                            aid.username=request.POST['username']
                            aid.contact_no=request.POST['contact_no']

                            if "pic" in request.FILES:
                                aid.pic=request.FILES['pic']
                                aid.save()

                            aid.save()

                            context={
                                'uid':uid,
                                'aid':aid,
                            }
                            
                            return render(request,"myapp/profile.html",context)
            else:
                uid=User.objects.get(email=request.session['email'])
                if uid.role=="admin":
                            aid=AdminUser.objects.get(user_id = uid)
                            context={
                                'uid':uid,
                                'aid':aid,
                            }
                            
                            return render(request,"myapp/profile.html",context)
    else:
      return render(request,"myapp/login.html",context)

def all_learners(request):
    if "email" in request.session:
                uid=User.objects.get(email=request.session['email'])
                learners_all=learners.objects.all()
                if uid.role=="admin":
                            aid=AdminUser.objects.get(user_id = uid)
                            context={
                                'uid':uid,
                                'aid':aid,
                                'learners_all':learners_all
                            }
                            
                            return render(request,"myapp/learner.html",context)
    else:
        return render(request,"myapp/login.html")
    
def learner_profile(request):
     if "email" in request.session:
            if request.POST:
               uid=User.objects.get(email=request.session['email'])
               if uid.role=="learners":
                            lid=learners.objects.get(user_id = uid)
                            # lid.username=request.POST['username']
                            lid.username = request.POST.get('username', lid.username)
                            # lid.contact_no=request.POST['contact_no']
                            lid.contact_no = request.POST.get('contact_no', lid.contact_no)
                            # lid.city = request.POST.get('city', lid.city)
                            print("City:", lid.city)




                            if "pic" in request.FILES:
                                lid.pic=request.FILES['pic']
                                lid.save()
                            lid.save()
                            context={
                                'uid':uid,
                                'lid':lid,
                            }
                            return render(request,"myapp/learner_profile.html",context)
            else:
                uid=User.objects.get(email=request.session['email'])
                if uid.role=="learners":
                            lid=learners.objects.get(user_id = uid)
                            context={
                                'uid':uid,
                                'lid':lid,
                            }
                            return render(request,"myapp/learner_profile.html",context)
                            
     else:
          return render(request,"myapp/login.html")

def add_category(request):
     if "email" in request.session:
                if request.POST:
                    uid=User.objects.get(email=request.session['email'])
                    if uid.role=="admin":
                        aid=AdminUser.objects.get(user_id = uid)
                        if "category_pic" in request.FILES:
                          cid=category.objects.create(user_id=uid,category_name=request.POST['category_name'],category_pic=request.FILES['category_pic'])
                        else:
                          cid=category.objects.create(user_id=uid,category_name=request.POST['category_name'])

                        context={
                                    'uid':uid,
                                    'aid':aid,
                                    's_msg':"successsfully category create"
                                }
                        return render(request,"myapp/add_category.html",context)
                else:
                      uid=User.objects.get(email=request.session['email'])
                      if uid.role=="admin":
                               aid=AdminUser.objects.get(user_id = uid)
                               context={
                                    'uid':uid,
                                    'aid':aid,
                                    
                                }
                               return render(request,"myapp/add_category.html",context)

def all_category(request):
      if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            call=category.objects.all()
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call,
                    }
            return render(request,"myapp/all-category.html",context)
        
def edit_category(request,pk):
     if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            cid=category.objects.get(id=pk)
            context={
                        'uid':uid,
                        'aid':aid,
                        'cid':cid
                        
                    }
            return render(request,"myapp/edit_category.html",context)
        
def update_category(request):
     if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)

            category_id=request.POST['categoryid']

            cid=category.objects.get(id=category_id)
            cid.category_name=request.POST['category_name']
            cid.save()

            if 'category_pic' in request.FILES:
                 cid.category_pic=request.FILES['category_pic']
                 cid.save()

            call=category.objects.all()
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call,
                        
                    }
            return render(request,"myapp/all-category.html",context)
        
def del_category(request,pk):
     if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            cid=category.objects.get(id=pk)
            cid.delete()
            call=category.objects.all()
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call,
                        
                    }
            return render(request,"myapp/all-category.html",context)
     
def add_course(request):
     if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if request.POST:
            if uid.role=="admin":
                aid=AdminUser.objects.get(user_id = uid)
                call=category.objects.all()

                category_name = request.POST['category']
                cid = category.objects.get(category_name=category_name)
                print("================cid",cid)

                course_id = course.objects.create( user_id=uid,
                                              category_id=cid,
                                              course_name= request.POST['course_name'],
                                              course_duration= request.POST['course_duration'],
                                              fees= request.POST['fees'],
                                              course_discription= request.POST['course_discription'] ,
                                              course_lecture_flow= request.FILES['course_lecture_flow'],
                                              course_handbook= request.FILES['course_handbook'],
                                              course_interview_question= request.FILES['course_interview_question'],
                                              course_assignment= request.FILES['course_assignment'],
                                              course_pic= request.FILES['course_pic'],
                                              course_tutor_name= request.POST['course_tutor_name'],
                                            
                                            )
                if course_id:
                     s_msg= "successfully course detailed added!!"
                     context={
                                'uid':uid,
                                'aid':aid,
                                'call':call,
                                's_msg':s_msg
                            }
                     return render(request,"myapp/add_course.html",context)
                else:
                     e_msg= "something went wrong!!"
                     context={
                                'uid':uid,
                                'aid':aid,
                                'call':call,
                                'e_msg':e_msg
                            }
                     return render(request,"myapp/add_course.html",context)
                     
        else:
            if uid.role=="admin":
                aid=AdminUser.objects.get(user_id = uid)
                call=category.objects.all()
     
                context={
                                'uid':uid,
                                'aid':aid,
                                'call':call
                                
                            }
                return render(request,"myapp/add_course.html",context)
                
def all_course(request):
      if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            print("------>>>>")
            call=course.objects.all()

            print("---->>>> call ",call)
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call,
                        
                    }
            return render(request,"myapp/all_courses_list.html",context)
        
def edit_course(request,pk):
     if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            call=category.objects.all()
            cid=course.objects.get(id=pk)
            context={
                            'uid':uid,
                            'aid':aid,
                            'cid':cid,
                            'call':call
                        
                            }
            return render(request,"myapp/edit-course.html",context)

def update_course(request):
      if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)

            course_id=request.POST['courseid']

            cid=course.objects.get(id=course_id)
            cid.course_name=request.POST['course_name']
            
            
            cid=course.objects.get(id=course_id)
            cid.course_tutor_name=request.POST['course_tutor_name']
            

            cid=course.objects.get(id=course_id)
            cid.course_duration=request.POST['course_duration']
            

            cid=course.objects.get(id=course_id)
            cid.fees=request.POST['fees']

            # cid.video_url = request.POST.get('vedio_url',cid.video_url)
            # cid.quiz_url = request.POST.get('quiz_url',cid.quiz_url)  # For quiz/exam links
            cid.save()



            if 'course_pic' in request.FILES:
                 cid.course_pic=request.FILES['course_pic']
                 cid.save()

            call=course.objects.all()
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call,
                        
                    }
            return render(request,"myapp/all_courses_list.html",context)

def del_course(request,pk):
      if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            cid=course.objects.get(id=pk)
            cid.delete()
            call=course.objects.all()
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call,
                        
                    }
            return render(request,"myapp/all_course_list.html",context)
        
def add_company(request):
     if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if request.POST:
            if uid.role=="admin":
                aid=AdminUser.objects.get(user_id = uid)
                

                # company_name = request.POST['company_name']
                # cid = company.objects.get(category_name=company_name)
                # print("================cid",cid)

                company_id = company.objects.create( user_id=uid,
                                            
                                              company_name= request.POST['company_name'],
                                            
                                              company_address= request.POST['company_address'],
                                              company_discription= request.POST['company_discription'] ,
                                            
                                              company_email= request.POST['company_email'],
                                              contact_no= request.POST['contact_no'],
                                              company_website= request.POST['company_website'],
                                              company_pic= request.FILES['company_pic'],
                                            
                                            )
                if company_id:
                     s_msg= "successfully company detailed added!!"
                     context={
                                'uid':uid,
                                'aid':aid,
                            
                                's_msg':s_msg
                            }
                     return render(request,"myapp/add_company.html",context)
                else:
                     e_msg= "something went wrong!!"
                     context={
                                'uid':uid,
                                'aid':aid,
                                'call':call,
                                'e_msg':e_msg
                            }
                     return render(request,"myapp/add_company.html",context)
                     
        else:
            if uid.role=="admin":
                aid=AdminUser.objects.get(user_id = uid)
                call=company.objects.all()
     
                context={
                                'uid':uid,
                                'aid':aid,
                                'call':call
                                
                            }
                return render(request,"myapp/add_company.html",context)
            
def all_company(request):
      if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="admin":
            aid=AdminUser.objects.get(user_id = uid)
            call=company.objects.all()
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call,
                    }
            return render(request,"myapp/all-company.html",context)
        
def edit_company(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "admin":
            aid = AdminUser.objects.get(user_id = uid)
            cid = company.objects.get(id = pk)

            context={
                        'uid' :uid,
                        'aid' :aid,
                        'cid' :cid
                    }
                    
            return render(request,"myapp/edit_company.html",context)
        
def update_company(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "admin":
            aid = AdminUser.objects.get(user_id = uid)
            
            companyid = request.POST['companyid']
            cid = company.objects.get(id = companyid)

            if request.POST:
                cid.company_name = request.POST['company_name']
                cid.company_website = request.POST['company_website']
                cid.company_email = request.POST['company_email']
                cid.company_discription = request.POST['company_discription']
                cid.company_address = request.POST['company_address']
                cid.contact_no = request.POST['contact_no']
                
                cid.save()
                if 'company_pic' in request.FILES:
                    cid.company_pic = request.FILES['company_pic']
                    
                cid.save()
                course = company.objects.all()
                s_msg = "Company Updated Successfully!"
                context = {
                    'uid': uid,
                    'aid': aid,
                    'companyid' : companyid,
                    's_msg': s_msg
                }
                #return render(request, "myapp/all-company.html", context)
                return redirect('all-company')

            else:
                context={
                            'uid' :uid,
                            'aid' :aid,
                            'cid' : cid
                        }
                return render(request,"myapp/edit_company.html",context)
            
def delete_company(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "admin":
            aid = AdminUser.objects.get(user_id = uid)
            cid = company.objects.get(id = pk)

            cid.delete()

            call = company.objects.all()
            s_msg = "company deleted successfully!"
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call,
                        's_msg' : s_msg
                     }
                    
            return render(request,"myapp/all-company.html",context) 
        
        

        
def add_enroll_course(request,pk):
      if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="learners":
            # lid=learners.objects.get(user_id = uid)
            lid = learners.objects.filter(user_id=uid).first()
            if not lid:
              print("Learner not found for user:", uid)
            else:
              print(lid, "==================hello")
        
            id=course.objects.get(id=pk)
            e_id=enrollcourse.objects.create(user_id=uid,
                                             learner_id=lid,
                                             course_id=id,
                                             fees_status="pending",
                                             status="pending"
                                             )
            
            
            if e_id:
                 s_msg="enrollment request send please wait !!"
            
            context={
                        'uid':uid,
                        'lid':lid,
                        's_msg':s_msg
                    
                    }
            return render(request,"myapp/all-courses_list.html",context)
        
def forgot_password(request):
    if request.POST:
        email=request.POST['email']
        try:
            uid=User.objects.get(email=email)
            print(f"User Role==========>: {uid}")
            if uid:
                print(f"User Role==========>: {uid.role}")
                if uid.role == "learners":
                     pass
                elif uid.role=="admin":
                    aid = AdminUser.objects.get(user_id=uid)
                    print(f"User Role==========>: {aid}")
                    otp = random.randint(1111,9999)
                    uid.otp = otp  
                    uid.save()
                    print("=========>",otp)
                    context = {
                        'otp':otp,
                        'uid':uid,
                        'aid' : aid
                    }
                    print(f"Email: {email}, User: {uid}, Role: {uid.role}")

            
                sendMail("Forgot-password","mail_template",email,context)
                print("=====================>done")
                context = {
                    'email' : email
                }
                return render(request,"myapp/reset_password.html",context)
            return render(request, "myapp/forgot_password.html", {'e_msg': "Invalid role or operation not supported!"})
        except:

            context = {
                'e_msg' : "invalid email address - does not exists ! "
            }
            return render(request,"myapp/forgot_password.html",context)
    else:
        return render(request,"myapp/forgot_password.html")    
    
def reset_password(request):
      if request.POST:
            email=request.POST['email']
            uid=User.objects.get(email=email)
            otp=request.POST['otp']
            newpassword=request.POST['newpassword']
            confirmpassword=request.POST['confirmpassword']
            if str(uid.otp)==otp:
                 if newpassword==confirmpassword:
                      uid.password=newpassword
                      uid.save()
                      s_msg="successfully password reset!!!"
            
                      context = {
                                   's_msg' :s_msg
                                }
                 
                      return render(request,"myapp/login.html",context)
                 else:
                      context={
                           'e_msg':"invalid otp",
                           'email':email
                      }
                      return render(request,"myapp/reset_password.html",context)
                 
def all_request(request):
     if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "admin":
            aid = AdminUser.objects.get(user_id=uid)
            # e_id = enrollcourse.objects.all()
            e_id = enrollcourse.objects.select_related('learner_id', 'learner_id__user_id', 'course_id').all()
            print(e_id,"==================hii")

            context = {
                'uid': uid,
                'aid': aid,
                'e_id': e_id
            }
            return render(request, "myapp/all_request.html", context)
     return redirect('login')

def accept_request(request,pk):
     if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "admin":
            try:
                e_id = enrollcourse.objects.get(id = pk)

                learner_name = e_id.learner_id.username
                learner_email = e_id.learner_id.user_id.email
                print("========>",learner_email)
                course_name = e_id.course_id.course_name

                e_id.status = "APPROVED"
                e_id.save()

                
                
                context = {
                    'l_n' : learner_name,
                    'l_e' : learner_email,
                    'c_n' : course_name,
                
                } 

                sendMail("APPROVE REQUEST", "accept_template", learner_email, context)
                #return render(request, "myapp/all_request.html")
                return redirect('all-request')
            except enrollcourse.DoesNotExist:
                return render(request, 'error.html', {'error': 'Enrollment request does not exist.'})
        else:
         return redirect('login')

def reject_request(request,pk):
     if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "admin":
            try:
                e_id = enrollcourse.objects.get(id = pk)

                learner_name = e_id.learner_id.username
                learner_email = e_id.learner_id.user_id.email
                course_name = e_id.course_id.course_name

                e_id.status = "REJECTED"
                e_id.save()

                
                
                context = {
                    'l_n' : learner_name,
                    'l_e' : learner_email,
                    'c_n' : course_name
                    
                }

                sendMail("Reject REQUEST", "reject_template", learner_email, context)
                
                return redirect('all-request')
            except enrollcourse.DoesNotExist:
                return render(request, 'error.html', {'error': 'Enrollment request does not exist.'})
        else:
         return redirect('login')
   
    #-------------------------------------------learner----------------------------------------------------
def learner_all_category(request):
     if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="learners":
            aid=learners.objects.get(user_id = uid)
            call=category.objects.all()
            context={
                        'uid':uid,
                        'aid':aid,
                        'call':call
                    }
            return render(request,"myapp/learner_all_category.html",context)
        
def learner_all_course_list(request):
     if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            if uid.role=="learners":
                lid=learners.objects.get(user_id = uid)
                print("------>>>>")
                call=course.objects.all()

                print("---->>>> call ",call)
                enrolcourse=enrollcourse.objects.filter(learner_id=lid)

                

                print("course found",call)
                print("enrolled course",enrolcourse)
                
                context={
                            'uid':uid,
                            'lid':lid,
                            'call':call,
                            
                        }
            return render(request,"myapp/learner-all-course-list.html",context)
        

def learner_enroll_course(request,pk):
    print(f"Received pk======>>>>>>>>> i m the one!!!!: {pk}") 
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="learners":
            lid=learners.objects.get(user_id=uid)
            id=course.objects.get(id=pk)
            call=category.objects.all()
    
            context={
                'uid':uid,
                'lid':lid,
                 'id':id,
                'call':call,
                'pk':pk,
            
            }

            return render(request, "myapp/lear_enroll_course.html",context)
        
def learner_add_enroll_course(request, pk):
    if "email" not in request.session:
        return redirect('login')

    # Get user, learner, and course details
    uid = User.objects.get(email=request.session['email'])
    lid = learners.objects.get(user_id=uid)
    cid = course.objects.get(id=pk)

    # Extract videos related to the selected course (e.g., Python)
    videos = cid.video.split(',') if cid.video else []

    # Enrollment logic (as before)
    enrollment = enrollcourse.objects.filter(user_id=uid, learner_id=lid, course_id=cid).first()
    s_msg = ""

    if enrollment:
        if enrollment.status == "approved":
            return redirect('learner-course-vedio', pk=pk)
        elif enrollment.status == "pending":
            s_msg = "Your enrollment is pending approval. Please wait for admin acceptance."
        elif enrollment.status == "rejected":
            s_msg = "Your request was rejected. Please enroll again."
            enrollment.delete()
    else:
        enrollcourse.objects.create(
            user_id=uid,
            learner_id=lid,
            course_id=cid,
            fees_status="pending",
            status="pending"
        )
        s_msg = "Your enrollment request has been submitted successfully! Please wait for approval."

    # Send videos to the template
    context = {
        'uid': uid,
        'lid': lid,
        'cid': cid,
        's_msg': s_msg,
        'videos': videos
    }
    return render(request, "myapp/learner_course_vedio.html", context)
  # Change to enroll page


# def learner_add_enroll_course(request, pk):
#     if "email" in request.session:
#         uid = User.objects.get(email=request.session['email'])
#         learner = learners.objects.get(user_id=uid)
#         course_obj = course.objects.get(id=pk)

#         # Check if enrollment already exists
#         enrollment = enrollcourse.objects.filter(user_id=uid, learner_id=learner, course_id=course_obj).first()

#         if not enrollment:
#             # Create new enrollment (First time)
#             enrollcourse.objects.create(
#                 user_id=uid,
#                 learner_id=learner,
#                 course_id=course_obj,
#                 status="pending",
#                 fees_status="unpaid",
#                 paid_fees=0
#             )
#             message = "Enrollment request sent. Pending approval."
#         else:
#             if enrollment.status == "approved":
#                 # Redirect to the video page if approved
#                 return redirect('learner-course-vedio', pk=pk)
#             elif enrollment.status == "pending":
#                 message = "Your enrollment is pending approval."
#             else:  # If rejected, show enroll button again
#                 message = "Your request was rejected. Please enroll again."

#         # Stay on the same page with the message
#         return render(request, 'myapp/all_courses_list.html', {'cid': course_obj, 'message': message})
#     else:
#         return redirect('login')



        
def learner_course_vedio(request, pk):
    cid = course.objects.get(id=pk)

    # Add videos manually if needed
    # videos = [
    #     "https://www.youtube.com/embed/8C_kHJ5YEiA",
    #     "https://www.youtube.com/embed/Vdt_wKTDPQ4"
    # ]
    print("Course Video URL:", cid.video)
    print("Course Video URL:", cid.quiz)


    context = {'cid': cid}
    return render(request, 'myapp/learner_course_vedio.html', context)

def learner_all_company(request):
    if "email" in request.session:
                
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="learners":
            call=company.objects.all()
            context={
                        
                        'call':call,
                    }
            return render(request,"myapp/learner-all-company.html",context)
        
    return redirect('login')


def dashboard(request):
    courses = course.objects.all()  # Sare courses fetch kar rahe hain
    companies = company.objects.all()  # Sare companies fetch kar rahe hain
    context = {
        'courses': courses,
        'companies': companies,
    }
    return render(request, 'learner_index.html', context)
