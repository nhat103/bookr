from django.db import models
from django.contrib import auth

# Create your models here.


class Publisher(models.Model):
    # a company that publisher book
    name = models.CharField(max_length=50, help_text="the name of publisher")
    website = models.URLField(help_text="the publisher's website")
    email = models.EmailField(help_text="the publisher's email")

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.title


class Contributor(models.Model):
    # A contributor to a Book, e.g. author, editor, \co-author
    first_name = models.CharField(
        max_length=50, help_text="The contributor's first name or name")
    last_name = models.CharField(
        max_length=50, help_text="The contributor's last name or name")
    email = models.EmailField(
        help_text="The contact email for the contributor.")

    def __str__(self):
        return self.first_name


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.",
                            choices=ContributionRole.choices, max_length=25)


class Review(models.Model):
    content = models.TextField(help_text="the review text")
    rating = models.IntegerField(
        help_text="the rating the  reviewer has given")
    date_created = models.DateTimeField(
        auto_now_add=True, help_text="the day and time review was created")
    date_edit = models.DateTimeField(
        null=True, help_text="date and time review was last edit")
    creator = models.ForeignKey(
        auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, help_text="The Book that this review is for")
