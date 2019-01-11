from random import choice, random
from string import lowercase

class Resident:

    def get_random_group(self, names, chances):
        n = int(random() * 100)

        t = 0
        for i in range(len(chances)):
            t += chances[i]
            if n <= t:
                return names[i]
        return names[-1]

    def get_ses_type(self):
        names = ['rich', 'affluent', 'comfortable', 'struggling', 'poor']
        chances = [1, 10, 20, 40]

        return self.get_random_group(names, chances)

    def get_age_type(self):
        # For this, we're assuming that a child is someone too young to work,
        # so the percentage is fairly low.

        # Most children will be generated with a family, so there's only a small
        # chance for a child to be generated on their own
        age_types = ['elderly', 'adult', 'child']
        chances = [20, 78]

        return self.get_random_group(age_types, chances)

    def get_name(self):
        ''' One day, this will get a cool name. For now, everyone gets
            a few random letters
        '''
        f = ''
        for i in range(3):
            f += choice(lowercase)

        s = ''
        for i in range(4):
            s += choice(lowercase)

        return f, s

    def get_job(self):
        ses_jobs = {
            'rich': ['none'],
            'affluent': ['shopkeep', 'artisan', 'trader', 'landlord', 'service'],
            'comfortable': ['shopkeep', 'artisan', 'trader', 'service', 'guard'],
            'struggling': ['worker', 'field hand', 'guard', 'service'],
            'poor': ['worker', 'field hand', 'beggar', 'service']
        }

        return choice(ses_jobs[self.ses])



    def __init__(self, vals={}):

        self.ses = self.get_ses_type()
        self.age = self.get_age_type()
        self.first_name, self.family_name = self.get_name()

        # Overwrite any vals we sent in after wasting precious electrons
        for val in vals:
            setattr(self, val, vals[val])

        # Assume a child has no job. I'm using a more medieval use of the term
        # 'child' rather than a modern use. 
        if self.age != 'child' and not hasattr(self, 'job'):
            self.job = self.get_job()
        else:
            self.job = "none"

def get_random_group(names, chances):
    n = int(random() * 100)
    t = 0
    for i in range(len(chances)):
        t += chances[i]
        if n <= t:
            return names[i]
    return names[-1]

def generate_family(r, t):
    # How many?
    options = [0, 1, 2, 3]
    chances = [40, 30, 20]
    n = get_random_group(options, chances)
    
    if n == 0:
        return []

    fam = []
    for i in range(n):
        r = Resident({'age': t, 'family_name':r.family_name, 'ses': r.ses})
        fam.append(r)

    return fam


def generate_town(n=1000):
    ''' Generate a town of people! 

        For each resident, we check to see if that resident has any
        children. If so, we go ahead and create that child.
    '''
    residents = []

    while len(residents) < n:
        r = Resident()
        residents.append(r)
        if r.age == 'adult':
            fam = generate_family(r, 'child')
            residents.extend(fam)
        if r.age == 'elderly':
            # We need to generate a family for the adult children
            pass


    return residents


def generate_people(n=1000):
    ''' Just a test function for seeing how a town of 1000 people
        shakes out
    '''
    job = {}
    age = {}
    ses = {}

    for i in range(n):
        r = Resident()
        fields = ['job', 'age', 'ses']

        for field in fields:
            if not getattr(r, field) in locals()[field]:
                locals()[field][getattr(r, field)] = 1
            else:
                locals()[field][getattr(r, field)] += 1

    return job, age, ses
