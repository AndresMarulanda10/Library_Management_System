from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models

# Create your models here.
def validate_publication_year(value):
    if value > timezone.now().year:
        raise ValidationError(f'El año de publicación {value} está en el futuro.')

class Book(models.Model):
    """
    Modelo que representa un libro en el sistema de gestión de biblioteca.

    Atributos:
    - title (str): El título del libro.
    - author (str): El nombre del autor del libro.
    - publisher (str): La editorial del libro.
    - publication_year (int): El año de publicación del libro.
    - category (str): La categoría o género del libro.
    - is_available (bool): Indica si el libro está disponible para préstamo.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_year = models.IntegerField(validators=[validate_publication_year])
    category = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

class User(models.Model):
    """
    Modelo que representa a un usuario del sistema de gestión de biblioteca.

    Atributos:
    - name (str): El nombre del usuario.
    - identification (str): La identificación única del usuario.
    - email (str): El correo electrónico del usuario.
    """
    name = models.CharField(max_length=100)
    identification = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)

class Loan(models.Model):
    """
    Modelo que representa un préstamo en el sistema de gestión de biblioteca.

    Atributos:
    - user (models.ForeignKey): Una relación many-to-one con el modelo User,
      que representa el usuario que tiene el préstamo.
    - book (models.ForeignKey): Una relación many-to-one con el modelo Book,
      que representa el libro que está prestado.
    - loan_date (datetime): La fecha en que se realizó el préstamo.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)