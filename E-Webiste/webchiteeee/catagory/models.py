from django.db import models

# Create your models here.
#  catagory name ta boro hater hobe
class Catagory(models.Model) :
    catagory_name = models.CharField(max_length =50 , unique=True)  # A character field to store the name of the category
    slug = models.CharField(max_length =100 , unique=True)     # A character field to store the unique slug (max length 100), used for creating SEO-friendly URLs

    # A "slug" is   way    of    generating    a    valid    URL, generally    using    data    already  obtained.For    instance, a    slug
    # uses    the    title   of    an    article to    generate    a    URL.I   advise    to  generate    the    slug    by
    # means   of   a   function, given   the   title( or another  piece  of data), rather  than  setting  it  manually

    # A text field to store a description of the category, with a max length of 255 characters
    # It is optional, so it can be left blank

    desciption = models.TextField(max_length=255 , blank=True)
    # An image field to store the category image
    # Files are uploaded to the 'photos/catagories' directory
    # This field is also optional, so it can be left blank
    cat_image = models.ImageField(upload_to= 'photos/catagories' , blank=True )
    # The
    # cat_image
    # field
    # stores
    # an
    # image
    # file.Ensure
    # that
    # you
    # 've configured your Django app to serve and store media files correctly.
# The string representation of the model instance (what will be displayed in admin or other places)
    # In this case, it returns the category name when the object is called as a string

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'


def __str__(self) :
    return  self.catagory_name
