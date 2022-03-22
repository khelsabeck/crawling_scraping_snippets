import json, datetime, re, time
from django.core.management.base import BaseCommand
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import ThisModel
from myapp.models import usermodel
from myapp.forms import YourEventForm
import events.csv_loader

'''
This class runs automation scripts for taking data out of a local file and processing 
it into items on the database. The local file with data to be added should be placed 
into a directory to match the field called 'directory' in the class variable below.
The data in that master input file will be processed as follows: 


'''
class Command(BaseCommand):

    def validate_user(self, user, this_model):
        '''
        validation
        '''
        try:
            # do_something()
            pass
        except:
            return False

    def get_user_data(self, user, list_models):
        '''
        This gets all the instances of data elems from the json for each user
        '''
        return [ thismodel for thismodel in list_models if self.validate_user(user, thismodel)]

    def get_unique_modelinstances(self, user):
        '''This gets and returns all the unique instances'''
        # code to get only non-duplicates or do any other validation
        pass

    def handle(self, *args, **options):
        '''
        when the user calls python3 manage.py populate_db, this should run and populate the db
        with the data in the local file
        '''
        # data = get data from json file
        # users = User.objects.all()
        # for user in users:
            # do_validation()?
            # for i in list_mymodel:
                # do_stuff()
                # save()
