from django.db import models
from django.conf import settings

class twitterAccount(models.Model):
    handle = models.CharField(max_length = 100)
    twitterid = models.CharField(max_length = 100)
    chainid = models.CharField(max_length = 100,blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                related_name="twitteraccounts")
    # trackers = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                                   related_name="tracking")

    def __str__(self):
        return  self.handle

# class trackingInfo(models.Model):
#     tracked_at = models.DateTimeField(auto_now_add=True)
#     twitterAccount = models.ForeignKey(twitterAccount,
#                                         on_delete=models.CASCADE, 
#                                         related_name="trackingino")
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, 
#                             on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

