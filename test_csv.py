from pandas import DataFrame
data = {'Programming language': ['Python','Java', 'C++'],
        'Designed by': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],
        'Appeared': ['1991', '1995', '1985'],
        'Extension': ['.py', '.java', '.cpp'],
    }

print(data["Programming language"][0])

df = DataFrame(data, columns= ['Programming language', 'Designed by', 'Appeared', 'Extension'])
export_csv = df.to_csv (r'pandaresult.csv', index = None, header=True)
print (df)