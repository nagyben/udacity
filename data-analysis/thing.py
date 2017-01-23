#!/usr/bin/python2

import unicodecsv
from datetime import datetime as dt

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def get_unique_students(dataset):
    unique_students = set()     # a set will only hold unique values
    for entry in dataset:
        unique_students.add(entry['account_key'])
    return unique_students

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

# Rename acct to account_key
for engagement in daily_engagement:
    engagement['account_key'] = engagement['acct']
    del[engagement['acct']]


# Remove udacity test accounts
enrollments_no_test = list()
for enrollment in enrollments:
    if enrollment['is_udacity'] != 'True':
        enrollments_no_test.append(enrollment)

enrollments = enrollments_no_test
del enrollments_no_test

# Fix data types
for enrollment in enrollments:
    enrollment['cancel_date'] = None if enrollment['cancel_date'] == '' else dt.strptime(enrollment['cancel_date'], '%Y-%m-%d')
    enrollment['days_to_cancel'] = None if enrollment['days_to_cancel'] == '' else int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = None if enrollment['join_date'] == '' else dt.strptime(enrollment['join_date'], '%Y-%m-%d')

print enrollments[0]

# Quiz : Refining the question
paid_students = dict()

for enrollment in enrollments:
    if enrollment['days_to_cancel'] == None or enrollment['days_to_cancel'] > 7:
        paid_students[enrollment['account_key']] = enrollment['join_date']

print len(paid_students)
