from django.db import models

# Create your models here.


class SetUpChannel(models.Model):
    # company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    # contact_person = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, blank=True)
    chat_with_us = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    video_call = models.URLField(max_length=50, blank=True) # Review this to involve Cloudinary
    feedback = models.CharField(max_length=50, blank=True)
    inquiry = models.CharField(max_length=50, blank=True)
    voip_call = models.CharField(max_length=50, blank=True) # Review field to suit voip calls
    i_buy_your_goods = models.CharField(max_length=50, blank=True)
    instagram_follow = models.CharField(max_length=100, blank=True)
    facebook_follow = models.CharField(max_length=100, blank=True)
    linkedin_follow = models.CharField(max_length=100, blank=True)
    twitter_follow = models.CharField(max_length=100, blank=True) # check to implement
    website = models.CharField(max_length=50, blank=True)
    youtube_subscribe = models.CharField(max_length=100, blank=True)
    provide_rating = models.CharField(max_length=100, blank=True) # Implement rating?
    # fill_a_survey = models.CharField(blank=True) # URL Field?

    def __str__(self):
        return self.email


