
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from Efficient_Spam_Detection import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', remoteuser.login, name="login"),


    url(r'^Register1/$', remoteuser.Register1, name="Register1"),

    url(r'^Recommend/(?P<pk>\d+)/$', remoteuser.Recommend, name="Recommend"),
    url(r'^Review/(?P<pk>\d+)/$', remoteuser.Review, name="Review"),
    url(r'^External_Spam_Attacker/$', remoteuser.External_Spam_Attacker, name="External_Spam_Attacker"),

    url(r'^View_All_Post_Details/$', remoteuser.View_All_Post_Details, name="View_All_Post_Details"),
    url(r'^View_Post_Reviews/$', remoteuser.View_Post_Reviews, name="View_Post_Reviews"),
    url(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    url(r'^dislikes/(?P<pk>\d+)/$', remoteuser.dislikes, name="dislikes"),
    url(r'^likes/(?P<pk>\d+)/$', remoteuser.likes, name="likes"),
    url(r'ViewTrending/$', remoteuser.ViewTrending, name="ViewTrending"),
    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    url(r'^View_Post_Recommends/$', remoteuser.View_Post_Recommends, name="View_Post_Recommends"),

    url(r'^Upload_Post/$', serviceprovider.Upload_Post, name="Upload_Post"),
    url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    url(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    url(r'ViewTrendings/$',serviceprovider.ViewTrendings,name="ViewTrendings"),
    url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    url(r'^dislikeschart/(?P<dislike_chart>\w+)', serviceprovider.dislikeschart,name="dislikeschart"),
    url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart,name="likeschart"),
    url(r'^View_Post_Details/$',serviceprovider.View_Post_Details, name='View_Post_Details'),
    url(r'^viewallpostsreviews/$', serviceprovider.viewallpostsreviews, name='viewallpostsreviews'),
    url(r'^View_Attackers/$', serviceprovider.View_Attackers, name='View_Attackers'),

    url(r'^View_Recommended_Post/$', serviceprovider.View_Recommended_Post, name='View_Recommended_Post'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
