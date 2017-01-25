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

def parse_maybe_int(value):
    if value == '':
        return None
    else:
        return int(value)

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(value, '%Y-%m-%d')

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
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

for engagement in daily_engagement:
    engagement['account_key'] = parse_maybe_int(engagement['account_key'])
    engagement['utc_date'] = parse_date(engagement['utc_date'])
    engagement['num_courses_visited'] = parse_maybe_int(engagement['num_courses_visited'])
    engagement['total_minutes_visited'] = parse_maybe_int(engagement['total_minutes_visited'])
    engagement['lessons_completed'] = parse_maybe_int(engagement['lessons_completed'])
    engagement['projects_completed'] = parse_maybe_int(engagement['projects_completed'])

for submission in project_submissions:
    submission['creation_date'] = parse_date(submission['creation_date'])
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['assigned_rating'] = parse_maybe_int(submission['assigned_rating'])
    submission['account_key'] = parse_maybe_int(submission['account_key'])
    submission['lesson_key'] = parse_maybe_int(submission['lesson_key'])
    # submission['processing_state'] is a string

# Quiz : Refining the question
paid_students = dict()

# Find paid students
for enrollment in enrollments:
    if enrollment['days_to_cancel'] == None or enrollment['days_to_cancel'] > 7:
        paid_students[enrollment['account_key']] = enrollment['join_date']

print len(paid_students)

# Find paid students' engagements for the first week
for engagement in daily_engagement:
    if engagement['account_key'] in paid_students \
    and engagement['utc-date'] <
