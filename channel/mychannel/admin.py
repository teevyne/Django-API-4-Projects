from django.contrib import admin
from .models import SetUpChannel


# Register your models here.


class SetupChannelAdmin(admin.ModelAdmin):
    list_display = ('phone_number',
                    'chat_with_us',
                    'email',
                    'video_call',
                    'feedback',
                    'inquiry',
                    'voip_call',
                    'website',
                    'provide_rating',
                    'linkedin_follow',
                    'instagram_follow',
                    )


admin.site.register(SetUpChannel, SetupChannelAdmin)
