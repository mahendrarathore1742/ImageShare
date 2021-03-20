from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save,m2m_changed
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount


class Userdata(models.Model):


	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile',default=1,null = True)
	Profileimage=models.ImageField(upload_to='userimage',blank=True,null=True,default="defaultimage/svg.png");
	Male = 'M'
	Female = 'F'
	GENDER_CHOICES =( 
        (Male, 'male'),
        (Female, 'female'),)

	GENDER = models.CharField(max_length=5, 
                                      choices=GENDER_CHOICES,
                                      default="M")

	FirstName=models.CharField(max_length=20,blank=True,null=True,default='');
	LastName=models.CharField(max_length=20,blank=True,null=True,default='');
	City=models.CharField(max_length=10,blank=True,null=True,default='');
	Country =models.CharField(max_length=10,null=True,blank=True,default='');
	Aboutme=models.TextField(max_length=50,default=' ',blank=True,null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Userdata.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class ImagePost(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=0,null=True)
	Title=models.CharField(max_length=30,null=False,);
	slug=models.SlugField(unique=True,editable=False)
	Images=models.ImageField(upload_to='photos/%Y/%m/%d')
	like=models.ManyToManyField(User,blank=True,related_name='post_like')
	save_post=models.ManyToManyField(User,blank=True,related_name='post_save')
	tags = TaggableManager()
	hit  = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

 
	def __str__(self):
		return f"Image  By {self.user}"

	
	def get_absolute_url(self):
		return reverse("Title:detail",kwargs={'slug':self.slug});

	def get_detail_url(self):
		return reverse("DiplayImages",kwargs={"username":self.user.username,'slug':self.slug})

	def get_like_url(self):
		return reverse("like",kwargs={"username":self.user.username,'slug':self.slug})

 
	def get_api_like_url(self):
		return reverse("like_api",kwargs={"username":self.user.username,'slug':self.slug})



	def get_api_save_url(self):
		return reverse("save_api",kwargs={"username":self.user.username,'slug':self.slug})

def create_slug(instance,new_slug=None):
	slug=slugify(instance.Title);
	if new_slug is not None:
		slug=new_slug;
	qs=ImagePost.objects.filter(slug=slug).order_by('-id');
	exists=qs.exists();
	if exists:
		new_slug=f"{slug}-{qs.first().id}";
		return create_slug(instance,new_slug=new_slug);
	return slug;
	
def pre_save_receiver(sender,instance,*args,**kwars):
	if not instance.slug:
		instance.slug=create_slug(instance);
pre_save.connect(pre_save_receiver,sender=ImagePost);

################################################################################
# for the follow and unfollow syatem

class Following(models.Model):
	# the user
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	followed=models.ManyToManyField(User,related_name='Followingdata',blank=True)
	follower=models.ManyToManyField(User,related_name='follower',blank=True)

	@classmethod
	def follow(cls,user,aother_account):
		obj,create=cls.objects.get_or_create(user=user);
		obj.followed.add(aother_account)
		print("followed")

	@classmethod
	def unfollow(cls,user,aother_account):
		obj,create=cls.objects.get_or_create(user=user);
		obj.followed.remove(aother_account)
		print("unfollow")


	def __str__(self):
		return str(self.user)

@receiver(post_save,sender=User)
def pre_save_data(sender,instance,created,**kwargs):
	if created:
		Following.objects.create(user=instance);


@receiver(m2m_changed,sender=Following.followed.through)
def addfollower(sender,instance,action,reverse,pk_set,**kwargs):
	followed_user=[];
	logged_user=User.objects.get(username=instance);

	for i in pk_set:
		user=User.objects.get(pk=i);
		following_obj=Following.objects.get(user=user);
		followed_user.append(following_obj);
 
	if action=="pre_add":
		for i in followed_user:
			i.follower.add(logged_user);
			i.save();

	if action=='pre_remove':
		for i in followed_user:
			i.follower.remove(logged_user);
			i.save();





