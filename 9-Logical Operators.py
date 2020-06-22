# if applicant has high income AND good credit
# Eligible for loan

has_high_income = False
has_good_credit = True
has_criminal_record = True

# if has_high_income and has_good_credit:   # both conditions has to be true
#     print('Eligible for loan')
# else:
#     print('Not Eligible for loan')

# if has_high_income or has_good_credit:  # at least one conditions has to true
#     print('Eligible for loan')
# else:
#     print('Not Eligible for loan')

'''if applicant has good credit and does have a criminal record'''
if has_good_credit and not has_criminal_record:  # reverse the boolean conditions
    print('Eligible for loan')
else:
    print('Not Eligible for loan')


