from math import ceil
from django.shortcuts import render,redirect
from django.urls.base import reverse
from googletrans import Translator
from gallary.decorators import allowed_user
from .models import images,Like,Comment,Catagory
from django.contrib.auth.models import Group, User
from django.http import JsonResponse, request
from .forms import Post_Model_From,CommentModelForm,CategoryModelform
from django.http import HttpResponse
from .filters import PostFilter
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup


#-------------------------------------NewsFeed----------------------------
def newsFeed(request):
    try:

        postPerPage  = 4
        posts = images.objects.all()
        numPosts = images.objects.all().count()
        totalPages = int(ceil(numPosts/postPerPage))+1

        form = Post_Model_From()
        category_form = CategoryModelform()
        c_form = CommentModelForm()
        catagorys = Catagory.objects.all()
        myfilter = PostFilter(request.GET, posts)
        posts = myfilter.qs

        lenList = []
        for i in posts:
            lenOfContent = len(i.content)
            lenList.append(lenOfContent)
        postAndLen = zip(posts[0:postPerPage],lenList)


        context = {
            # 'posts':posts,
            'form':form,
            'c_form':c_form,
            'catagorys':catagorys,
            'myfilter':myfilter,
            'posts':postAndLen,
            'category_form':category_form,
            'totalPages':range(2,totalPages)

        }
        return render (request,'newsfeed.html',context,)
    except:
        return render(request,'errorpage.html')


#-------------------------------------NewsFeed2----------------------------
def newsFeed2(request,pk):

    try:
        
        reqPage = int(pk)

        postPerPage  = 4
        upper = postPerPage*reqPage
        lower = (reqPage-1)*postPerPage

        posts = images.objects.all()
        numPosts =images.objects.all().count()
        totalPages = int(ceil(numPosts/postPerPage))+1

        form = Post_Model_From()
        category_form = CategoryModelform()
        c_form = CommentModelForm()
        catagorys = Catagory.objects.all()
        myfilter = PostFilter(request.GET, posts)
        posts = myfilter.qs

        lenList = []
        for i in posts:
            lenOfContent = len(i.content)
            lenList.append(lenOfContent)
        postAndLen = zip(posts[lower:upper],lenList)


        context = {
            # 'posts':posts,
            'form':form,
            'c_form':c_form,
            'catagorys':catagorys,
            'myfilter':myfilter,
            'posts':postAndLen,
            'category_form':category_form,
            'totalPages':range(2,totalPages)

        }
        return render (request,'newsfeed.html',context,)

    except:
        return render(request,'errorpage.html')




#-------------------------------------Save The Post----------------------------
@allowed_user(allowed_roles=['admin'])
def save_post(request):
    if request.method == 'POST':
        catId = request.POST.get('catagory')

        p_form =Post_Model_From(request.POST,request.FILES or None)

        if p_form.is_valid():
            instance = p_form.save(commit = False)
            # instance.catagory = catId
            instance.save()
            p_form.save_m2m()

    return redirect('newsfeed')
#-------------------------------------Save The category----------------------------



@allowed_user(allowed_roles=['admin'])
def save_category(request):
    if request.method == 'POST':
        catId = request.POST.get('catagory')

        cat_form =CategoryModelform(request.POST,request.FILES or None)

        if cat_form.is_valid():
            instance = cat_form.save(commit = False)
            # instance.catagory = catId
            instance.save()


    return redirect('newsfeed')




#-------------------------------------delete The Post----------------------------

@allowed_user(allowed_roles=['admin'])
def delete_post(request,pk):
    obj = images.objects.get(id=pk)
    if 'confirm_delete_btn' in request.POST:
            obj.delete()
            return redirect('newsfeed')
    context = {
        'post':obj,
    }
    return render(request,'delete.html',context)


@allowed_user(allowed_roles=['admin'])
def update_post(request,pk):


    obj = images.objects.get(id=pk)
    form = Post_Model_From(instance=obj)
    if request.method == 'POST':
        form = Post_Model_From(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('newsfeed')

    context = {
        'form':form,
        'id':pk,
    }
    return render (request,'updatepost.html',context)
        



#-------------------------------------Like Dislike The Post----------------------------

def like_unlike_post(request):
    user = request.user
    if request.method =='POST':
        post_like_id = request.POST.get('post_id')
        image_obj = images.objects.get(id=post_like_id)


        if user in image_obj.liked.all():
            image_obj.liked.remove(user)
        else:
            image_obj.liked.add(user)

        like,created = Like.objects.get_or_create(user = user ,post_id =post_like_id)

        
        if not created:
            if like.value =='Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value ='Like'
            image_obj.save()
            like.save()
        data = {
            'value':like.value,
            'likes':image_obj.liked.all().count(),


            }
        return JsonResponse(data,safe=False)





#-------------------------------------Save Comment----------------------------  

def save_comments(request,pk,post_title):
    # commentAuthor = request.user
    user = request.user

    if request.method == 'POST':
        post_comm_id = request.POST.get('form')
        comm_body = request.POST.get('body')

        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit = False)
            instance.user = user
            instance.post = images.objects.get(id = post_comm_id)
            instance.body = comm_body
            instance.save()
            count = images.objects.get(id=post_comm_id).CommentCount()
            allCommQs =  instance.post.comment_set.values()


            userId = []
            body = []
            user_final_list = []

            for i in allCommQs:                
                userId.append(i['user_id'])
                body.append(i['body'])

            for j in userId:
                user1 = str(User.objects.get(id=j))
                user_final_list.append(user1)

            a = zip(user_final_list,body)
            zipList = list(a)
            allComments = list(allCommQs)
            user = str(user)
            return JsonResponse({'count':count,'status':'ok','allComments':allComments,'zipList':zipList,'user':user})




#-------------------------------------Continue Reading----------------------------
    
translator = Translator(service_urls=['translate.googleapis.com'])


def ContinueReading(request,pk,post_title):
    posts =   images.objects.all()
    myfilter = PostFilter(request.GET, posts)
    posts = myfilter.qs

    obj = images.objects.get(id=pk)
    objContent = obj.content[0:50]

    detect_lang = translator.detect(objContent)
    article_lang = detect_lang.lang

    
    if article_lang =='en':
        article_lang = 'English'
    elif article_lang =='bn':
        article_lang = 'Bangla'

    cnt = obj.subCat
    subcatList = cnt.split(',')
    subcatListSet = set(subcatList)

    rellist = []
    newestPost = []

    contentDes = BeautifulSoup(objContent,'lxml').get_text()
    keylist = obj.title.split(' ')+contentDes.split(' ')
    keywords = (',').join(keylist)
    


    allPosts = images.objects.all().exclude(id =pk)


    for i in allPosts:
        currentPostCatList = i.subCat.split(',')
        currentPostCatListSet = set(currentPostCatList)
        match = set.intersection(currentPostCatListSet,subcatListSet)
        if len(match)>4:
            rellist.append(i)
            if len(rellist)>3:
                break
    len_of_relpost = len(rellist)



    for newPost in allPosts:
        newestPost.append(newPost)
        if len(newestPost) == 4:break

    c_form = CommentModelForm()

    context ={

        'post':obj,
        'c_form':c_form,
        'rellist':rellist,
        'len_of_relpost':len_of_relpost,
        'newestPost':newestPost,
        'myfilter':myfilter,
        'keywords':keywords,
        'cnt':cnt,
        'article_lang':article_lang,
        'contentDes':contentDes

      
    }
    return render(request,'singlePost.html',context)


#-------------------------------------Continue Reading Translate----------------------------
def ContinueReadingTranslate(request,pk,post_title,lang_name):
    translator = Translator(service_urls=['translate.googleapis.com'])

    posts =   images.objects.all()
    myfilter = PostFilter(request.GET, posts)
    posts = myfilter.qs
    
    obj = images.objects.get(id=pk)
    objContent = obj.content
    detect_lang = translator.detect(objContent)
    article_lang = detect_lang.lang
    
    if article_lang =='en':
        article_lang = 'English'
    elif article_lang =='bn':
        article_lang = 'Bangla'

    cnt = obj.subCat
    rellist = []
    newestPost = []
    contentDes = BeautifulSoup(objContent,'lxml').get_text()
    keylist = obj.title.split(' ')+contentDes.split(' ')

    keywords = (',').join(keylist)
    


    allPosts = images.objects.all().exclude(id =pk)


    j = 0
    for i in allPosts:
        if i.subCat == cnt:

            rellist.append(i)
            j+=1
            if j==4:break
    len_of_relpost = len(rellist)



    for newPost in allPosts:
        newestPost.append(newPost)
        if len(newestPost) == 4:break

    c_form = CommentModelForm()
    reqLang  =lang_name

    LangConvert = translator.translate(objContent[:2000], dest=reqLang)
    LangConvert1 = translator.translate(objContent[2000:4000], dest=reqLang)
    LangConvert2 = translator.translate(objContent[4000:len(objContent)], dest=reqLang)
    finalLang = LangConvert.text+LangConvert1.text+LangConvert2.text






    context = {
        'post':obj,
        'c_form':c_form,
        'rellist':rellist,
        'len_of_relpost':len_of_relpost,
        'newestPost':newestPost,
        'keywords':keywords,
        'cnt':cnt,
        'myfilter':myfilter,
        'article_lang':article_lang,
        'finalLang':finalLang,
        'contentDes':contentDes

    }
    return render(request,'tranlateReading.html',context)


#---------------------------------catagoryWiseSearch----------------------------


def catagory_wise_filter(request,pk,title):
    c_form = CommentModelForm()
    postObj = images.objects.filter(category=pk)

    context ={

        'posts':postObj,
        'c_form':c_form,
        'title':title

    }
    return render(request,'catagoryRes.html',context)



#---------------------------------DeleteComment----------------------------
@csrf_exempt
def delete_comment(request):
    if request.method == 'POST':
        comId = request.POST.get('cmId')
        postId = request.POST.get('postId')
        com_del = Comment.objects.get(id =comId)
        com_del.delete()
        return JsonResponse({'status':'OK'})
        


@allowed_user(allowed_roles=['admin'])      
def allposts(request):
    allPosts = images.objects.all()
    myfilter = PostFilter(request.GET, allPosts)
    allPosts = myfilter.qs
    context = {
        'allPosts':allPosts,
        'myfilter':myfilter
    }
    return render(request,'allpost.html',context)



def about(request):
    catagorys = Catagory.objects.all()
    context = {
        'catagorys':catagorys
    }
    return render(request,'about.html',context)



def termsAndConditions(request):
    context = {
        
    }
    return render(request,'termandcondition.html',context)



    
@allowed_user(allowed_roles=['admin'])
def admins(request):
    group = Group.objects.all()
    users = User.objects.all()
    roles = []
    userrole =[]
    for user in users:
        if user.groups.exists():
            groupname = request.user.groups.all()[0].name
            roles.append(groupname)
            userrole.append(user)
    webRoles = list(zip(roles,userrole))
    context = {
        'groups':group,
        'webRoles':webRoles
    }
    return render(request,'admin.html',context)