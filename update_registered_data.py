# update_registered_data.py

# Your original registered data list
registered_data = [
    ('Abhijeeth', 'Student'),
    ('kohli', 'Student'),
    ('abhigna', 'Student'),
    ('Lionel Messi', 'Student'),
    ('Morgan_Freeman', 'Teacher'),
    ('Barack_Obama', 'Teacher'),
    ('Nihitha Vadlamuri', 'Student'),
    ('Scarlett Johansson', 'Student'),
    ('ronaldo', 'Student_21WU0102047'),
    ('Chris_Evans', 'Student'),
    ('Angelina Jolie', 'Student'),
    ('Hyunjin', 'Student'),
    ('Abhigna Ragala', 'Student_21WU0102051')
]

# Names to delete
names_to_delete = ['ronaldo', 'Abhigna Ragala']

# Create a new registered data list excluding the entries to delete
updated_registered_data = [(name, role) for name, role in registered_data if name not in names_to_delete]

# Display the updated registered data
print(updated_registered_data)
