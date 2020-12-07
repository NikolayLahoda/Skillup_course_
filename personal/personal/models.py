from django.db import models


""" PURE PHYSICAL LIBRARY WITH PAPER BOOKS


    Shelve:
        - id (PK)
        - bookcase (FK -> BookCase)
        - order_number
        
        
    BookCase:
        - id (PK)
        - code (unique)
        
    Librarian:
        - id (PK)
        - first_name
        - last_name
        - phone
        - employeed_date 
        - unemployeed_date 
        
    ReaderCard:
        - id (PK)
        - reader (FK -> Reader)
    
    Country:
        - name (unique)    
        
    Author:
        - first_name
        - last_name
        - country (FK -> Country)    
        
    Genre:
        - id (PK)
        - name
        
    Book:
        - id (PK)
        - name
        - authors  (M2M -> Author)
        - year_issued
        - pages_count
        - genres  (M2M -> Genre)
    
    BookCopy:
        - id (PK)
        - book (FK -> Book)
        
    Reader:
        - id (PK)  
        - first_name
        - last_name 
        - phone 
             
    WishList (books to be read):
        - id (PK)
        - book (FK -> Book)
        - reader (FK -> Reader) 
        
    Order (books actually taken): 
        - id (PK)
        - bookcopy (FK -> BookCopy)
        - reader (FK -> Reader) 
        - taken_at (datetime)
        - returned_at (datetime)
        - given_by (FK -> Librarian) 
           
    
archived - status of book/journal,etc    
"""



class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=100)
    year_issued = models.PositiveSmallIntegerField()
    authors = models.ManyToManyField("Author")
    pages_count = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField("Genre")

class Genre(models.Model):
    name = models.CharField(max_length=100)


class BookCopy(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField()

