from django.db import models

# Create your models here.


class Publisher(models.Model):
    # a company that publisher book
    name = models.CharField(max_length=50, help_text="the name of publisher")
    website = models.URLField(help_text="the publisher's website")
    email = models.EmailField(help_text="the publisher's email")


class Book(models.Model):
    # A published book.
    title = models.CharField(max_length=50, help_text="the title of the book")
    publication_date = models.DateField(
        verbose_name="Date the book was published")
    isbn = models.CharField(
        max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        'Contributor', through="BookContributor")


class Contributor(models.Model):
    # A contributor to a Book, e.g. author, editor, \co-author
    first_name = models.CharField(
        max_length=50, help_text="The contributor's first name or name")
    last_name = models.CharField(
        max_length=50, help_text="The contributor's last name or name")
    email = models.EmailField(
        help_text="The contact email for the contributor.")
