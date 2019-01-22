# generic
from rest_framework import generics

from postings.models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): #detail view

    lookup_field = 'pk' #slug, id
    serializer_class = BlogPostSerializer
    #queryset = BlogPost

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.get("pk")
    #     return
