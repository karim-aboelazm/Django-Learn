from django.contrib import admin
from myapp.models import Posts,Customers,Comments,CommentsReply,PostReact
# Register your models here.
admin.site.register(Posts)
admin.site.register(Customers)
admin.site.register(Comments)
admin.site.register(CommentsReply)
admin.site.register(PostReact)