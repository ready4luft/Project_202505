albums = [
    '2004_anapa', '2005_anapa', '2007_school', '2010_school',
    '2013_spain', '2014_greece', '2019_turkey', '2021_turkey',
    '2023_moscow'
    ]

land_count = 0

for land in albums:
    if '_turkey' in land:
        land_count += 1

print(land_count)